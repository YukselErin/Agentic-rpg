<script lang="ts">
  import type { WorldObject } from "$lib/state";

  export let object: WorldObject;
</script>

<div
  class="absolute px-6 py-3 bg-green-500/20 border border-green-400 text-green-300 rounded-full shadow-lg flex items-center justify-center"
  style="left: {object.position.x}px; top: {object.position.y}px; transform: translate(-50%, -50%);"
>
  {object.name}
</div>
