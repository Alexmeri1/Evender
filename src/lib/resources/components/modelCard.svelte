<script lang="ts" customElements="model-card">
	import { onMount } from 'svelte';
	import CardBody from '$lib/resources/components/cardeff/CardBody.svelte';
	import CardContainer from './cardeff/CardContainer.svelte';
	import CardItem from './cardeff/CardItem.svelte';
	import { scale } from 'svelte/transition';

	export let id: string;
	export let style: string = '';
	export let height: number | string = '300px';
	export let width: number | string = '300px';
	export let background: string = 'blue';
	export let color: string = 'white';
	export let ButtonReactivity: object = {
		invert: ['65%', '100%'],
		scale: [1, 1.1]
	};

	export let intensity: string;
	// export let transition:
	// 	| {
	// 			in: {
	// 				type: object;
	// 				duration: number;
	// 				delay: number | undefined;
	// 				opacity: number | undefined;
	// 				start: number | undefined;
	// 			};

	// 			out: {
	// 				type: object;
	// 				duration: number;
	// 				delay: number | undefined;
	// 				opacity: number | undefined;
	// 				start: number | undefined;
	// 			};
	// 	  }
	// 	| undefined;

	let loadState: boolean = true;
	let isMouseEntered = false;
	let mainId = id;

	try {
		if (intensity.split(',').map(Number).length != 2) {
			throw new Error("The intensity property must be of dimension 2 in the form '(x, y)'");
		}
	} catch (e) {
		throw new Error("The intensity property must be of dimension 2 in the form '(x, y)'");
	}

	if (!id) {
		throw new Error('You must have a id prop');
	}

	if (ButtonReactivity) {
		Object.entries(ButtonReactivity).forEach(([_, value]) => {
			if (value.length != 2) {
				throw new Error(
					'The ButtonReactivity object must have a length of 2 for each key-value pair'
				);
			}
		});
	}

	// try {
	// 	if (transition) {
	// 		if (!transition?.in?.type && !transition?.out?.type) {
	// 			throw new Error(
	// 				'The transition prop must have at least one valid Svelte transformation object'
	// 			);
	// 		} else if (!transition?.in?.duration && !transition?.out?.duration) {
	// 			throw new Error('The transition prop must have at least one valid duration object');
	// 		}
	// 	}
	// } catch (e) {
	// 	console.log(e);
	// }

	// function dynamicTransition(node, params) {
	// 	let { type, duration, delay, easing, start, opacity } = params;

	// 	if (!type) {
	// 		type = scale;
	// 		duration = 0;
	// 		delay = 0;
	// 		start = 0;
	// 		opacity = 0;
	// 	}

	// 	const transformRequest = (type) => {
	// 		return type ? type : null;
	// 	};

	// 	const tr = transformRequest(type);
	// 	return tr(node, { duration, delay, easing, start, opacity });
	// }
</script>

{#if loadState}
	<div
		id="main-container-transition"
		style="width: {width}; height: {height}; background:none"
	>
		<CardContainer
			bind:isMouseEntered
			{intensity}
			style="border-radius: 20px; z-index:95; width:400px; height:500px; margin:0; margin-bottom:10px; color: {color}; transition: all 1s ease-in-out; transform: scale(1); opacity:1;"
			id={mainId}
			className={"yes"}
		>
			<CardBody
				className=" "
				style="width:{width ? width + 'px' : width}; background-color: {background}; height:{height
					? height + 'px'
					: height}; font-family: gilroy, sans-serif; transition: all 1s ease-in-out; {style}; margin-left:0px;"
				id="model-card-body"
			>
				<CardItem
					translateZ={-50}
					style="font-size:23px; position:absolute; top:35px; left:30px; font-family: gilroy, sans-serif; transition:all 1s ease-in-out;"
					id="model-name"
				>
					yes
				</CardItem>
				<CardItem
					{isMouseEntered}
					translateZ={-60}
					style="position:absolute; bottom:0; left:0; width:100%; height:60px; display:flex;"
				>
					<div style="width: 100%; height:100%">
						<div
							style="width:100%; height:100%; display:flex; justify-content:center; align-items:center; font-family: gilroy, sans-serif; transition:all .2s ease-out; position:absolute; bottom:0; pointer-events:none; user-select:none;"
							id="user-content"
						></div>
					</div>
				</CardItem>
				<div
					style="position: absolute; right:0; top:0; height:100%; width:auto; font-family: gilroy, sans-serif; align-items:center; justify-content:center; display:flex;"
				>
					<CardItem
						{isMouseEntered}
						translateZ={-20}
						style="font-family: gilroy, sans-serif; max-width:300px; max-height:65px; padding:10px; margin-right:25px; text-align: right; -webkit-line-clamp: 2; -webkit-box-orient: vertical; display:-webkit-box;overflow:hidden; text-overflow:ellipsis; transition:all .5s ease-out; pointer-events:none; user-select:none;"
						id="model-context"
					>
						description
					</CardItem>
				</div>
				<div
					id="importance-layer"
					style="width:auto; height:auto; display:flex; justify-content:center; align-items:center; position:absolute; bottom:0; right:0; z-index:99;"
				></div>

				<CardItem
					translateZ={-20}
					style="width:0%; height:100%;position:absolute; top:0; right:0; transform-origin: right; transition: all 1s ease-in-out; background-image:linear-gradient(to left, black 50%, transparent 100%); pointer-events:none; user-select:none; opacity:0; "
					id="del-transition"
				></CardItem>
			</CardBody>
		</CardContainer>
	</div>
{/if}

<style>
	@font-face {
		font-family: 'gilroy';
		src: url('./src/lib/assets/fonts/Gilroy-Light.otf') format('truetype');
	}
</style>
