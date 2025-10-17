<script lang="ts">
  import type { Player } from "$lib/types";

  export let players: Record<string, Player> = {};

  // For now, we just display the first player.
  $: currentPlayer = Object.values(players)[0];
</script>

<div class="bg-gray-800 p-4 text-white">
  <h2 class="text-xl font-bold mb-2">{currentPlayer?.name || 'Player'}</h2>
  {#if currentPlayer}
    <div>
      <strong>Right Hand:</strong>
      <div class="ml-4 p-2 bg-gray-700 rounded">{currentPlayer.body_parts.hands?.name || 'Empty'}</div>
    </div>
    <div class="mt-2">
      <strong>Left Hand:</strong>
      <div class="ml-4 p-2 bg-gray-700 rounded">{'Empty'}</div>
    </div>
    <div class="mt-2">
      <strong>Body:</strong>
      <div class="ml-4 p-2 bg-gray-700 rounded">{currentPlayer.body_parts.body?.name || 'Empty'}</div>
    </div>
    <div class="mt-2">
      <strong>Feet:</strong>
      <div class="ml-4 p-2 bg-gray-700 rounded">{currentPlayer.body_parts.feet?.name || 'Empty'}</div>
    </div>
  {/if}
</div>
