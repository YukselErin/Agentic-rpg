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
    position: tuple[float, float]
    body_parts: BodyParts
    inventory: List[Item] = Field(default_factory=list)

class WorldObject(BaseModel):
    id: str
    name: str
    position: tuple[float, float]
    svg: str

class GameState(BaseModel):
    world_objects: List[WorldObject]
    players: Dict[str, Player]
    event_log: List[str]

class PlayerCommand(BaseModel):
    command: str
    args: List[str] = Field(default_factory=list)

class WebSocketMessage(BaseModel):
    type: str
    payload: dict