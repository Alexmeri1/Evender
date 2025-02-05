<script lang="ts">
	import '$root/global.scss';

	import PartyScreen from '$lib/resources/components/partyBG.svelte';
	
	import FullLogo from '$lib/resources/icons/FullLogo.png';
	// import MiddleLogo from '$lib/resources/icons/MiddleLogo.png';
	// import LeftLogo from '$lib/resources/icons/LeftLogo.png';
	// import RightLogo from '$lib/resources/icons/RightLogo.png';

	// import { onMount } from 'svelte';
	// import { redirect } from '@sveltejs/kit';
</script>

<div
	id="main"
	style="width: 100%; height: auto; display:block; justify-content: center; align-items: center; background-color: transparent; padding:0; margin:0;  z-index:1"
>
	<div
		id="main-parents"
		style="width: 100%; height:1080px; display:block; flex-direction: row; margin:0; padding:0;"
	>
		<PartyScreen />
	</div>

	<div
		style="display: flex; width:100vw; height:100vh; position:absolute; top:0; align-items: center; justify-content: center;"
	>
		<div
			id="announcer"
			style="width: auto; height:100vh; display:flex; flex-direction: column; align-items:center; justify-content: center;"
		>
			<h1
				style="font-size:26px; display:flex; color:white; text-align:center; display:flex; font-family:Quantico-regular, sans-serif;"
			>
				Live your <span
					style="font-family:Lobster, sans-serif; color:#ffa494; margin-left:7px; margin-bottom:6px; display:flex; position:relative;"
					>Events</span
				>
				<span
					style="margin-top:-5px; margin-left:7px; font-family:Quantico-regular, sans-serif; font-size:26px"
					class="middle-scale-und underlined-text">like never before</span
				>
			</h1>

			<div
				id="bottom-section"
				style="display: flex; flex-direction: row; width:100vw; align-items:flex-start; justify-content: center; height:auto;"
			>
				<h1
					style="transform:rotate(-90deg); font-size:9px; padding:0; margin-right:-10px; margin-top:10px; color:#fce575; font-family:Quantico-bold, sans-serif; font-weight:bold;"
				>
					THE
				</h1>
				<div id="Logo-anim">
					<img
						src={FullLogo}
						alt="Evender Logo"
						width="auto"
						height="40px"
						style="border-color:black; opacity:.7"
					/>
				</div>
			</div>
		</div>
	</div>
</div>
