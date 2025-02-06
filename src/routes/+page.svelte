<script lang="ts">
	import '$root/global.scss';

	import PartyScreen from '$lib/resources/components/partyBG.svelte';

	import FullLogo from '$lib/resources/icons/Webp/FullLogo.webp';
	import { onMount } from 'svelte';

	const typedTxtArray = [
		['Events', '#ffa494'],
		['Activities', '#7eff7e'],
		['Celebrations', '#ffcc00'],
		['Gatherings', '#ff66b2']
	];
	let typedPosition = 0;

	onMount(() => {
		let typeAnimator = () => {
			const typedText = document.getElementById('typeTxt');
			if (typedText) {
				typedText.style.animation = 'untyping 1s steps(20, end) forwards, blinking 0.8s infinite';
				setTimeout(() => {
					typedText.innerText = typedTxtArray[typedPosition][0];
					typedText.style.color = typedTxtArray[typedPosition][1];

					setTimeout(() => {
						typedText.style.animation = 'typing 1s steps(20, end) forwards, blinking 0.8s infinite';

						if (typedPosition == typedTxtArray.length - 1) typedPosition = 0;
						else typedPosition++;

						setTimeout(() => {
							typeAnimator();
						}, 5000);
					}, 150);
				}, 1100);
			}
		};

		typeAnimator();
	});
</script>

<svelte:head>
	<title>Evender • Home</title>
</svelte:head>

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
				style="font-size:26px; display:flex; color:white; text-align:center; display:flex; font-family:Quantico-regular, sans-serif; transition:all .5s cubic-bezier(0.19, 1, 0.22, 1)"
			>
				Live your <div class="container" style="margin-left:7px; margin-bottom:2px; width:auto; transition: width .5s ease-out;">
					<div
						class="typed-out"
						id="typeTxt"
						style="font-family:Lobster, sans-serif;"
					>
						
					</div>
				</div>
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
