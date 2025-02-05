<script>
	import LoadScreen from '$lib/resources/components/loadScreen.svelte';
	import { onMount } from 'svelte';
    import { fade } from 'svelte/transition';
    import NavBar from '$lib/resources/components/nav-bar.svelte';

	let loading = true;
    let loaded = false;

	onMount(() => {
        loaded = true
		setTimeout(() => {
			loading = false;
		}, 4000);
	});
</script>

<div style="position: absolute; top:0; width:100vw; height:100px; display:flex; align-items: center; justify-content: center; z-index:2">
    <NavBar/>
</div>

{#if loading}
	<div
		out:fade={{delay:1000}}
		id="load-screen"
		style="width: 100vw; height:100vh; padding:0; margin:0; z-index:3; display:flex; align-items: center; justify-content: center; background-color:black"
	>
		<LoadScreen status={loaded} />
	</div>
{/if}

{#if loaded}
  <div style="z-index: 1; overflow:hidden;">
    <slot />
  </div>
{/if}
