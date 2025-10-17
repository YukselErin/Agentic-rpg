export interface Item {
    name: string;
    description: string;
    svg: string;
}

export interface BodyParts {
    hands?: Item;
    feet?: Item;
    body?: Item;
}

export interface Player {
    id: string;
    name: string;
    position: [number, number];
    body_parts: BodyParts;
    inventory: Item[];
}

export interface Tile {
    type: string;
    svg: string;
    entities: Player[];
}

export interface GameState {
    grid: Tile[][];
    players: Record<string, Player>;
    event_log: string[];
}

export interface PlayerCommand {
    command: string;
    args?: string[];
}

export interface WebSocketMessage {
    type: string;
    payload: any;
}
