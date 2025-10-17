<script lang="ts">
  import type { Tile as TileType } from '$lib/types';
  import Tile from './Tile.svelte';

  export let grid: TileType[][] = [];
</script>

<div class="grid grid-cols-10 gap-1 bg-gray-800 p-1">
  {#each grid as row}
    {#each row as tile}
      <Tile {tile} />
    {/each}
  {/each}
</div>
