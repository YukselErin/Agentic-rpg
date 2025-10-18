<script lang="ts">
  import { onMount } from 'svelte';
  import { tweened } from 'svelte/motion';
  import { cubicOut } from 'svelte/easing';
  import { gameState } from '$lib/store';
  import { connectWebSocket, sendCommand } from '$lib/websocket';
  import Player from '$lib/components/Player.svelte';
  import WorldObject from '$lib/components/WorldObject.svelte';

  // --- Camera Settings ---
  const RENDER_DISTANCE = 800;
  const camera = tweened({ x: 0, y: 0 }, {
    duration: 2000,
    easing: cubicOut
  });

  // --- State ---
  let viewport: { width: number, height: number } = { width: 0, height: 0 };
  let clientId: string;

  // --- Derived State ---
  $: currentPlayer = $gameState.players[clientId];
  $: if (currentPlayer) {
    camera.set({ x: currentPlayer.position[0], y: currentPlayer.position[1] });
  }

  $: visibleObjects = $gameState.world_objects.filter(obj => {
    if (!viewport.width) return false;
    const dx = obj.position[0] - $camera.x;
    const dy = obj.position[1] - $camera.y;
    return Math.abs(dx) < RENDER_DISTANCE && Math.abs(dy) < RENDER_DISTANCE;
  });

  // --- Lifecycle ---
  onMount(() => {
    clientId = crypto.randomUUID();
    connectWebSocket(clientId);

    const handleKeyDown = (e: KeyboardEvent) => {
      const commands: Record<string, string> = {
        'w': 'move_north',
        's': 'move_south',
        'a': 'move_west',
        'd': 'move_east'
      };
      if (commands[e.key]) {
        sendCommand(commands[e.key]);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  });

</script>

<div class="w-screen h-screen bg-gray-900 text-white overflow-hidden" bind:clientWidth={viewport.width} bind:clientHeight={viewport.height}>
  <div class="absolute w-full h-full">
    <div 
      class="absolute transition-transform duration-500 ease-out"
      style="transform: translate({viewport.width / 2 - $camera.x}px, {viewport.height / 2 - $camera.y}px)"
    >
      <!-- Render Players -->
      {#each Object.values($gameState.players) as player}
        <Player {player} />
      {/each}

      <!-- Render World Objects -->
      {#each visibleObjects as object}
        <WorldObject {object} />
      {/each}
    </div>
  </div>

  <!-- UI Overlay -->
  <div class="absolute top-0 left-0 p-4">
    <h1 class="text-2xl font-bold">Agentic RPG</h1>
    {#if currentPlayer}
      <p>Player: {currentPlayer.name}</p>
      <p>Position: ({Math.round(currentPlayer.position[0])}, {Math.round(currentPlayer.position[1])})</p>
    {/if}
    <div class="mt-4">
      <h2 class="font-bold">Controls:</h2>
      <p>W, A, S, D to move</p>
    </div>
  </div>

  <div class="absolute bottom-0 left-0 p-4 bg-black bg-opacity-50 w-full h-48 overflow-y-auto">
    <h2 class="font-bold">Event Log</h2>
    <ul>
      {#each $gameState.event_log as event}
        <li>{event}</li>
      {/each}
    </ul>
  </div>
</div>
