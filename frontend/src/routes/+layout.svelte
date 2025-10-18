<script>
  import "../app.css";
  import { onMount } from 'svelte';
  import { connectWebSocket } from '$lib/websocket';

  onMount(() => {
    const clientId = crypto.randomUUID();
    connectWebSocket(clientId);
  });
</script>

<slot />
