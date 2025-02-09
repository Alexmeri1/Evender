<script lang="ts">
	import { onMount } from 'svelte';
	import { cubicOut } from 'svelte/easing';
	import { slide } from 'svelte/transition';

	import '$root/global.scss';

	let isConnected = false;
	let showSetup = false;
	let showQuestions = false;

	let messages = [
		{
			text: 'Welcome to <span class="neonText" style="color:#ba3b3b; font-family: Quantico-bold, sans-serif; font-size: 27px; --neonStart-color:#ba3b3b; --neonEnd-color:#ba3b3b; margin-left:5px">Evender</span>',
			style: {
				color: 'white',
				fontSize: '24px',
				fontFamily: 'Quantico-bold, sans-serif',
				alignSelf: 'center',
				justifySelf: 'center',
				padding: '20px'
			}
		},
		{
			text: 'Do you already have an account?',
			style: {
				color: 'white',
				fontSize: '17px',
				marginBottom: '40px',
				paddingTop: '-30px',

				fontFamily: 'Quantico-regular, sans-serif'
			}
		},
		{
			buttons: [
				{
					text: 'I do ;)',
					style: {
						width: '130px',
						height: '100%',
						backgroundColor: 'black',
						color: 'white',
						borderRadius: '10px',
						borderStyle: 'solid',
						borderColor: 'white',
						cursor: 'pointer',
						fontSize: '16px',
						margin: '5px',
						transition:
							'background-color 0.3s, color 0.3s, scale 0.2s cubic-bezier(0.55, 0.055, 0.675, 0.19)',
						boxShadow: '0 4px 8px rgba(255, 255, 255, 0.2)',
						scale: '1',
						transform: ''
					}
				},
				{
					text: 'Nope',
					style: {
						width: '130px',
						height: '100%',
						backgroundColor: 'black',
						color: 'white',
						borderRadius: '10px',
						borderStyle: 'solid',
						borderColor: 'white',
						cursor: 'pointer',
						fontSize: '16px',
						margin: '5px',
						transition:
							'background-color 0.3s, color 0.3s, scale .2s cubic-bezier(0.55, 0.055, 0.675, 0.19)',
						boxShadow: '0 4px 8px rgba(255, 255, 255, 0.2)',
						scale: '1',
						transform: ''
					}
				}
			]
		}
	];

	function styleObjectToString(styleObj: any) {
		return Object.entries(styleObj)
			.map(([key, value]) => `${key.replace(/([A-Z])/g, '-$1').toLowerCase()}: ${value}`)
			.join('; ');
	}

	onMount(() => {
		if (isConnected) {
			return;
		}

		setTimeout(() => {
			showSetup = true;
			setTimeout(() => {
				showQuestions = true;
			}, 2000);
		}, 3000);
	});
</script>

<div
	id="main"
	style="overflow: hidden; z-index:1; background-color:#2f2f2f; padding:0; width:100vw; height:100vh;"
>
	<div
		id="section-chooser"
		style="width:65%; height:100vh; position:absolute; top:0; right:0;  background:linear-gradient(to left, #2f2f2f 98%, black)"
	></div>
	<div
		id="section-question"
		style="width: 100%; height:100vh; background: black; transition:width 1s ease-out; position:absolute;  top:0; left:0; "
	>
		{#if showSetup}
			<div
				id="mainSetup"
				style="height: 100%; width:100vw; display:flex; align-items: center; justify-content: center; flex-direction: column;"
			>
				{#each messages as msg, index}
					{#if showQuestions}
						<div
							in:slide={{ axis: 'y', duration: 700, easing: cubicOut, delay: 1500 * index }}
							id="cont-msg"
							style="width: 100vw; display:flex; align-items: center; justify-content: center; flex-direction: column;"
						>
							{#if msg.text}
								{#if index == 0}
									<div
										class=""
										style="align-items: center; justify-content: center; display: flex; text-align: center;
                                    "
									>
										<h1
											class="container typed-out"
											style="{styleObjectToString(msg.style)}; --cursorBarStyle:none;"
										>
											{@html msg.text}
										</h1>
									</div>
								{:else}
									<h1 style={styleObjectToString(msg.style)}>{msg.text}</h1>
								{/if}
							{/if}
							{#if msg.buttons}
								<div
									style="display: flex; flex-direction: row; align-items: center; justify-content: center; width: 500px; height: 60px;"
								>
									{#each msg.buttons as button}
										<button
											in:slide={{ axis: 'x', duration: 700, easing: cubicOut, delay: 500 }}
											class="click_animation-expand"
											style={styleObjectToString(button.style)}
											on:click={() => {
												button.style.transform = 'translate3d(0, -1px, 10px)';
												setTimeout(() => {
													button.style.transform = 'translate3d(0, 0, 0)';
												}, 200);
											}}
											on:mouseover={() => {
												button.style.backgroundColor = 'white';
												button.style.color = 'black';
												button.style.borderColor = 'transparent';
												button.style.scale = '.95';
											}}
											on:focus={() => {
												button.style.backgroundColor = 'white';
												button.style.color = 'black';
												button.style.borderColor = 'transparent';
												button.style.scale = '.95';
											}}
											on:mouseout={() => {
												button.style.backgroundColor = 'black';
												button.style.color = 'white';
												button.style.borderColor = 'white';
												button.style.scale = '1';
											}}
											on:blur={() => {
												button.style.backgroundColor = 'black';
												button.style.color = 'white';
												button.style.borderColor = 'white';
												button.style.scale = '1';
											}}
										>
											{button.text}
										</button>
									{/each}
								</div>
							{/if}
						</div>
					{/if}
				{/each}
			</div>
		{/if}
	</div>
</div>
