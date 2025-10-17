<script lang="ts">
  import { gameState } from '$lib/state';
  import Player from '$lib/components/Player.svelte';
  import WorldObject from '$lib/components/WorldObject.svelte';
</script>

<div class="relative w-full h-screen bg-gray-900 overflow-hidden">
  <Player playerCharacter={$gameState.player_character} />

  {#each $gameState.world_objects as worldObject}
    <WorldObject object={worldObject} />
  {/each}
</div>