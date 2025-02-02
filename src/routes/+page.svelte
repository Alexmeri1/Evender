<script lang="ts">
	import MainLogo from '$lib/resources/icons/MainLogo.png';
	import PartyScreen from '$lib/resources/components/partyBG.svelte';
    import { onMount } from 'svelte';
    import { redirect } from '@sveltejs/kit';

    onMount(() => {
        window.location.href = "https://evender.co/form"
        redirect(200, '/form')
    })
</script>

<div
	id="main"
	style="width: 100%; height: auto; display:block; justify-content: center; align-items: center; background-color: transparent; padding:0; margin:0;"
>
	<div
		id="main-parents"
		style="width: 100%; height:1080px; display:block; flex-direction: row; margin:0; padding:0;"
	>
		<PartyScreen /> 
	</div>

	<div style="display: flex; ">
		<img src={MainLogo} alt="logo" style="width: 100px; z-index:99;" />
	</div>
</div>
