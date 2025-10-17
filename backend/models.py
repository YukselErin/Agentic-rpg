from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class Item(BaseModel):
    name: str
    description: str
    svg: str

class BodyParts(BaseModel):
    hands: Item | None = None
    feet: Item | None = None
    body: Item | None = None

class Player(BaseModel):
    id: str
    name: str
    position: tuple[int, int]
    body_parts: BodyParts
    inventory: List[Item] = Field(default_factory=list)

class Tile(BaseModel):
    type: str
    svg: str
    entities: List[Player] = Field(default_factory=list) # Simplified, could be a union of Player, NPC, etc.

class GameState(BaseModel):
    grid: List[List[Tile]]
    players: Dict[str, Player]
    event_log: List[str]

class PlayerCommand(BaseModel):
    command: str
    args: List[str] = Field(default_factory=list)

class WebSocketMessage(BaseModel):
    type: str
    payload: dict
