<script lang="ts">
  import { onMount } from "svelte";
  import type { Communication, PlayerCharacter } from "$lib/state";

  export let communications: Communication[];
  export let parent: PlayerCharacter;

  let parentElement: HTMLElement;
  let lineCoordinates: { from: { x: number; y: number }; to: { x: number; y: number } }[] = [];

  function getElementCenter(id: string) {
    const el = document.getElementById(id);
    if (!el) return { x: 0, y: 0 };

    const parentRect = parentElement.getBoundingClientRect();
    const rect = el.getBoundingClientRect();
    
    return {
      x: rect.left - parentRect.left + rect.width / 2,
      y: rect.top - parentRect.top + rect.height / 2,
    };
  }

  function calculateCoordinates() {
    if (!parentElement) return;

    lineCoordinates = communications.map(comm => {
      const fromCoords = getElementCenter(comm.from);
      const toCoords = getElementCenter(comm.to);
      return { from: fromCoords, to: toCoords };
    });
  }

  onMount(() => {
    // We need a slight delay to ensure the elements are rendered and have their positions.
    setTimeout(calculateCoordinates, 100);

    // Recalculate on window resize if needed
    window.addEventListener('resize', calculateCoordinates);
    return () => {
      window.removeEventListener('resize', calculateCoordinates);
    };
  });

</script>

<style>
  .marching-ants {
    stroke-dasharray: 4, 4;
    animation: marching 2s linear infinite;
  }

  @keyframes marching {
    0% {
      stroke-dashoffset: 0;
    }
    100% {
      stroke-dashoffset: -16;
    }
  }
</style>

<div class="absolute top-0 left-0 w-full h-full pointer-events-none" bind:this={parentElement}>
  <svg class="w-full h-full">
    {#each lineCoordinates as coords}
      <line
        x1={coords.from.x}
        y1={coords.from.y}
        x2={coords.to.x}
        y2={coords.to.y}
        class="stroke-current text-pink-500 marching-ants"
        stroke-width="2"
      />
    {/each}
  </svg>
</div>
