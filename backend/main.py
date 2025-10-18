from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
import json
import random

from models import GameState, Player, BodyParts, Item, PlayerCommand, WebSocketMessage, WorldObject
from agents.game_master import WorldStateManager, StorytellerAgent
from agents.arbiter import ArbiterAgent
from agents.personality import PersonalityAgent
from agents.body_part import BodyPartAgent
from agents.svg_bard import SVGBard

app = FastAPI()

import os

raw_origins = os.getenv("CORS_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173")
origins = [origin.strip() for origin in raw_origins.split(",")]

print(f"Allowed CORS origins: {origins}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Agent and Game State Initialization
game_state = GameState(
    world_objects=[],
    players={},
    event_log=["Welcome to Agentic RPG!"]
)

world_manager = WorldStateManager(game_state)
storyteller = StorytellerAgent()
arbiter = ArbiterAgent()
body_part_agent = BodyPartAgent()

try:
    svg_bard = SVGBard()
    personalities = [
        PersonalityAgent("brave and reckless"),
        PersonalityAgent("cautious and observant")
    ]

    def initialize_world():
        for i in range(20): # Create 20 random world objects
            game_state.world_objects.append(
                WorldObject(
                    id=f"tree_{i}",
                    name="tree",
                    position=(random.uniform(-500, 500), random.uniform(-500, 500)),
                    svg=svg_bard.get_svg("tree")
                )
            )

    initialize_world()
except Exception as e:
    print(f"Could not connect to Redis or initialize world: {e}")
    class FallbackSVGBard:
        def get_svg(self, asset_description: str) -> str:
            return f"<svg width='100' height='100'><text>{asset_description}</text></svg>"
    svg_bard = FallbackSVGBard()
    initialize_world()

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, client_id: str):
        await websocket.accept()
        self.active_connections[client_id] = websocket
        player_name = f"Player {client_id[:5]}"
        game_state.players[client_id] = Player(
            id=client_id,
            name=player_name,
            position=(random.uniform(-100, 100), random.uniform(-100, 100)),
            body_parts=BodyParts(),
            inventory=[]
        )
        game_state.event_log.append(f"{player_name} has joined the game.")
        await self.broadcast_state()

    def disconnect(self, client_id: str):
        player_name = game_state.players[client_id].name
        del self.active_connections[client_id]
        del game_state.players[client_id]
        game_state.event_log.append(f"{player_name} has left the game.")

    async def broadcast_state(self):
        message = WebSocketMessage(type="game_state_update", payload=game_state.dict())
        for connection in self.active_connections.values():
            await connection.send_text(message.json())

manager = ConnectionManager()

async def game_turn(player_id: str, player_command: PlayerCommand):
    # This function will need to be updated to handle movement in a continuous space
    # For now, we'll just broadcast the state
    # 1. Personalities generate intentions
    intentions = [p.generate_intention(game_state) for p in personalities]
    game_state.event_log.extend(intentions)

    # 2. Arbiter decides action
    action = arbiter.decide_action(intentions)
    game_state.event_log.append(f"Arbiter decides: {action}")

    # 3. Body part executes action
    body_part_agent.execute_action(action, game_state)

    # 4. Storyteller generates narrative
    narrative = storyteller.generate_narrative(game_state)
    game_state.event_log.append(narrative)

    # 5. World state is updated (placeholder)
    world_manager.update_world()

    await manager.broadcast_state()

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_text()
            command = PlayerCommand.parse_raw(data)
            # Simple movement for testing
            player = game_state.players[client_id]
            if command.command == "move_north":
                player.position = (player.position[0], player.position[1] - 10)
            elif command.command == "move_south":
                player.position = (player.position[0], player.position[1] + 10)
            elif command.command == "move_east":
                player.position = (player.position[0] + 10, player.position[1])
            elif command.command == "move_west":
                player.position = (player.position[0] - 10, player.position[1])
            
            game_state.event_log.append(f"{game_state.players[client_id].name} commanded: {command.command}")
            await game_turn(client_id, command)
    except WebSocketDisconnect:
        manager.disconnect(client_id)
        await manager.broadcast_state()

@app.get("/api/healthcheck")
def health_check():
    return {"status": "ok", "message": "Backend is running!"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)