<script lang="ts">
  export let events: string[] = [];
</script>

<div class="bg-gray-800 p-4 text-white h-48 overflow-y-auto">
  <h2 class="text-xl font-bold mb-2">Event Log</h2>
  <ul>
    {#each events as event}
      <li>{event}</li>
    {/each}
  </ul>
</div>
