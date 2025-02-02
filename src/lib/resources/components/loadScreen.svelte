<script lang="ts" customElements="load-screen">
	import MiddleLogo from '$lib/resources/icons/MiddleLogo.png';
	import LeftLogo from '$lib/resources/icons/LeftLogo.png';
	import RightLogo from '$lib/resources/icons/RightLogo.png';

	import { onMount } from 'svelte';
	import { slide } from 'svelte/transition';
	import { cubicInOut } from 'svelte/easing';

	export let status: boolean;

	let ready = false;
	let rotation = 0;
	let animationFrame: number;
	let animStart = false;

	onMount(function () {
        setTimeout(() => {
            ready = true;
        }, 2000)
		// animate();
	});

	$: if (ready && status) {
		const middleLog = document.getElementById('mid-log');
        const parentContainer = document.getElementById("logo-parent")
        
        if(parentContainer) parentContainer.style.borderColor = "#ffffff"
		if (middleLog) middleLog.style.transform = `rotate(90deg)`;
		setTimeout(() => {
			animStart = true;
		}, 1000);
	}
</script>

<div
	id="main"
	style="width: 100vw; height:100vh; display:flex; align-items: center; justify-content: center; background-color: %00000075; backdrop-filter: blur(5px); z-index:99;"
>
	<div
		id="logo-parent"
		style="height: 70px; width:auto; align-items:center; justify-content: center; transition: all .5s cubic-bezier(0.25, 0.46, 0.45, 0.94); display:flex; flex-direction: row; padding:20px; border-style:solid; border-color:white; border-radius:15px; border-color:#ffffff30; background-color:#00000025;"
	>
		{#if animStart}
			<img
                in:slide={{ axis: 'x', duration: 500, easing: cubicInOut}}
				src={LeftLogo}
				alt="LeftLogo"
				width="175px"
				style="transform-origin: left; margin-right:-20px;"
				id="left-log"
			/>
		{/if}
		<div id="middlelogo-container" style="display: flex; align-items: center; justify-content: center; transform-origin: center center; transition: all .5s cubic-bezier(0.25, 0.46, 0.45, 0.94); width: 70px; position:relative; padding-left:15px">
			<img
				src={MiddleLogo}
				id="mid-log"
				alt="mainLogo"
				width="70px"
				style="transform-origin: center center; margin-left:-20px; transition: all .5s cubic-bezier(0.25, 0.46, 0.45, 0.94);"
			/>
		</div>
		{#if animStart}
			<img
				in:slide={{ axis: 'x', duration: 500, easing: cubicInOut, delay: 500 }}
				src={RightLogo}
				alt="rightLogo"
				id="right-log"
				width="65px"
				style="transform-origin: center center; margin-left:-25px"
			/>
		{/if}
	</div>
</div>
