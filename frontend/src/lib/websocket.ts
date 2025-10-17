import { gameState, socketConnected } from './store';
import type { PlayerCommand, WebSocketMessage } from './types';

let socket: WebSocket;

export function connectWebSocket(clientId: string) {
    if (socket && socket.readyState === WebSocket.OPEN) {
        return;
    }

    socket = new WebSocket(`ws://localhost:8000/ws/${clientId}`);

    socket.onopen = () => {
        console.log('WebSocket connection opened');
        socketConnected.set(true);
    };

    socket.onmessage = (event) => {
        const message: WebSocketMessage = JSON.parse(event.data);
        if (message.type === 'game_state_update') {
            gameState.set(message.payload);
        }
        console.log('WebSocket message received:', message);
    };

    socket.onclose = () => {
        console.log('WebSocket connection closed');
        socketConnected.set(false);
    };

    socket.onerror = (error) => {
        console.error('WebSocket error:', error);
        socketConnected.set(false);
    };
}

export function sendCommand(command: string, args: string[] = []) {
    if (socket && socket.readyState === WebSocket.OPEN) {
        const playerCommand: PlayerCommand = { command, args };
        socket.send(JSON.stringify(playerCommand));
    } else {
        console.error('WebSocket is not connected.');
    }
}
