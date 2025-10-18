<script lang="ts">
  import type { WorldObject } from '$lib/types';

  export let object: WorldObject;
</script>

<div 
  class="absolute w-12 h-12 flex items-center justify-center"
  style="left: {object.position[0]}px; top: {object.position[1]}px; transform: translate(-50%, -50%);"
>
  {@html object.svg}
</div>