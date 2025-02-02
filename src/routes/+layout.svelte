<script>
	import LoadScreen from '$lib/resources/components/loadScreen.svelte';
	import { onMount } from 'svelte';
    import { fade } from 'svelte/transition';

	let loading = true;
	let loaded = false;

	onMount(() => {
		loaded = true;
		setTimeout(() => {
			loading = false;
		}, 5000); // Simulate a 2-second loading time
	});
</script>

{#if loading}
	<div out:fade id="load-screen" style="width: 100%; height:100%; padding:0; margin:0; z-index:99; display:flex; align-items: center; justify-content: center; backgeound-color:black">
		<LoadScreen status={loaded} />
	</div>
{:else}
	<slot style="z-index: 98;"/>
{/if}
