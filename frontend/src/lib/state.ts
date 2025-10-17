import { writable } from 'svelte/store';

// TypeScript Types
export interface Position {
  x: number;
  y: number;
}

export interface PersonalityAgent {
  id: string;
  name: string;
  position: Position;
  color: string;
}

export interface BodyPart {
  id: string;
  position: Position;
  holding?: string;
  wearing?: string;
}

export interface Communication {
  from: string;
  to: string;
  type: string;
}

export interface PlayerCharacter {
  position: Position;
  personality_agents: PersonalityAgent[];
  body_parts: {
    right_hand: BodyPart;
    feet: BodyPart;
  };
  communications: Communication[];
}

export interface WorldObject {
  id: string;
  name: string;
  position: Position;
}

export interface GameState {
  player_character: PlayerCharacter;
  world_objects: WorldObject[];
}

// Initial State Packet Data
const initialState: GameState = {
  "player_character": {
    "position": { "x": 500, "y": 400 },
    "personality_agents": [
      { "id": "agent_brave", "name": "Brave", "position": { "x": -40, "y": 0 }, "color": "bg-orange-500" },
      { "id": "agent_cautious", "name": "Cautious", "position": { "x": 40, "y": 0 }, "color": "bg-sky-400" }
    ],
    "body_parts": {
      "right_hand": { "id": "right_hand", "position": { "x": 100, "y": 0 }, "holding": "sword" },
      "feet": { "id": "feet", "position": { "x": 0, "y": 80 }, "wearing": "boots" }
    },
    "communications": [
      { "from": "agent_brave", "to": "right_hand", "type": "PROPOSAL" }
    ]
  },
  "world_objects": [
    { "id": "quest_1", "name": "Find the Lost Cat", "position": { "x": 1200, "y": 250 } },
    { "id": "enemy_goblin", "name": "Goblin Scout", "position": { "x": 450, "y": 800 } }
  ]
};

// Svelte Store
export const gameState = writable<GameState>(initialState);
