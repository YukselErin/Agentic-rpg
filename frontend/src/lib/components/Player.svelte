<script lang="ts">
  import type { Player } from '$lib/types';

  export let player: Player;
</script>

<div 
  class="absolute w-10 h-10 bg-blue-500 rounded-full shadow-lg flex items-center justify-center"
  style="left: {player.position[0]}px; top: {player.position[1]}px; transform: translate(-50%, -50%);"
>
  <div class="text-white font-bold">P</div>
</div>