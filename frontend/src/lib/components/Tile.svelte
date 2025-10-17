<script lang="ts">
  import type { Tile } from "$lib/types";

  export let tile: Tile;
</script>

<div class="w-24 h-24 bg-gray-700 flex items-center justify-center">
  {@html tile.svg}
</div>
