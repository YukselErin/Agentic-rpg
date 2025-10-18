import { writable } from 'svelte/store';
import type { GameState } from './types';

const initial_state: GameState = {
    world_objects: [],
    players: {},
    event_log: []
};

export const gameState = writable<GameState>(initial_state);
export const socketConnected = writable<boolean>(false);