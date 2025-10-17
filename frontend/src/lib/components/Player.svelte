<script lang="ts">
  import type { PlayerCharacter } from "$lib/state";
  import Agent from "./Agent.svelte";
  import Connections from "./Connections.svelte";

  export let playerCharacter: PlayerCharacter;
</script>

<div
  class="absolute bg-white border-2 border-gray-400 rounded-lg shadow-lg"
  style="left: {playerCharacter.position.x}px; top: {playerCharacter.position.y}px; width: 300px; height: 200px; transform: translate(-50%, -50%);"
>
  <div class="relative w-full h-full">
    <!-- Render Personality Agents -->
    {#each playerCharacter.personality_agents as agent}
      <Agent {agent} />
    {/each}

    <!-- Render Body Part Placeholders -->
    <div 
      id="right_hand"
      class="absolute w-10 h-10 bg-gray-200 border border-gray-400 rounded-md flex items-center justify-center"
      style="left: {playerCharacter.body_parts.right_hand.position.x}px; top: {playerCharacter.body_parts.right_hand.position.y}px; transform: translate(-50%, -50%);"
    >
      {playerCharacter.body_parts.right_hand.holding}
    </div>
    <div 
      id="feet"
      class="absolute w-10 h-10 bg-gray-200 border border-gray-400 rounded-md flex items-center justify-center"
      style="left: {playerCharacter.body_parts.feet.position.x}px; top: {playerCharacter.body_parts.feet.position.y}px; transform: translate(-50%, -50%);"
    >
      {playerCharacter.body_parts.feet.wearing}
    </div>

    <!-- Render Connections Overlay -->
    <!-- <Connections communications={playerCharacter.communications} parent={playerCharacter} /> -->
  </div>
</div>
