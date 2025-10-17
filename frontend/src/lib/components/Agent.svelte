<script lang="ts">
  import type { PersonalityAgent } from "$lib/state";

  export let agent: PersonalityAgent;
</script>

<div
  id={agent.id}
  class="absolute w-12 h-12 rounded-full flex items-center justify-center text-white font-bold shadow-md {agent.color}"
  style="left: {agent.position.x}px; top: {agent.position.y}px; transform: translate(-50%, -50%);"
>
  {agent.name}
</div>
