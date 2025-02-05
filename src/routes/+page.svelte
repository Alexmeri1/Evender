<script lang="ts">
	import '../global.scss';

	import PartyScreen from '$lib/resources/components/partyBG.svelte';

	import FullLogo from '$lib/resources/icons/FullLogo.png';
	import MiddleLogo from '$lib/resources/icons/MiddleLogo.png';
	import LeftLogo from '$lib/resources/icons/LeftLogo.png';
	import RightLogo from '$lib/resources/icons/RightLogo.png';

	import { onMount } from 'svelte';
	import { redirect } from '@sveltejs/kit';
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

<style>
	.underlined-text {
		color: inherit;
		text-decoration: none;
	}

	/* Underline styles */
	.underlined-text {
		display: block;
		position: relative;
		padding: 0.2em 0;
	}

	/* Fade in */
	.underlined-text::after {
		content: '';
		position: absolute;
		bottom: 5px;
		left: 0;
		width: 100%;
		height: 0.1em;
		background-color: #ffa494;
		opacity: 0;
		transition:
			opacity 300ms,
			transform 300ms;
	}

	.underlined-text:hover::after,
	.underlined-text:focus::after {
		opacity: 1;
		transform: translate3d(0, 0.2em, 0);
	}

	/* Scale from center */
	.middle-scale-und::after {
		opacity: 1;
		transform: scale(0);
		transform-origin: center;
	}

	.middle-scale-und:hover::after,
	.middle-scale-und:focus::after {
		transform: scale(1);
	}
</style>
