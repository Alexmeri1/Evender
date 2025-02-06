<script lang="ts">
	import calendarPlus from '$lib/resources/icons/calendar-plus.png';
	import calendarMinus from '$lib/resources/icons/calendar-minus.png';
	import person from '$lib/resources/icons/person.png';
	import location from '$lib/resources/icons/location.png';
	import city from '$lib/resources/icons/city.png';
	import lightning from '$lib/resources/icons/lightning.png';
	import MiddleLogo from '$lib/resources/icons/MiddleLogo.png';

	import { onMount } from 'svelte';
	import { fade } from 'svelte/transition';

	let testData = {
		location: {
			city: 'Toronto',
			country: 'CA'
		},
		dates: {
			beginning: '2025-01-01',
			end: '2025-02-20'
		},
		groupSize: '10'
	};

	let eventsLoad = false;

	onMount(() => {
		const CountrySel = document.getElementById('locationCountry');

		CountrySel?.addEventListener('input', (event) => {
			const selectedCountry = (event?.target as HTMLSelectElement)?.value;
			console.log(selectedCountry);
			if (selectedCountry == 'US' || selectedCountry == 'CA') {
				const citySelector = document.getElementById('citySelector');
				if (citySelector) {
					citySelector.innerHTML = '';
					while (citySelector.firstChild) {
						citySelector.removeChild(citySelector.firstChild);
					}

					const cities =
						selectedCountry == 'US'
							? [
									'New York',
									'Los Angeles',
									'Chicago',
									'Houston',
									'Phoenix',
									'Philadelphia',
									'San Antonio',
									'San Diego',
									'Dallas',
									'San Jose'
								]
							: [
									'Toronto',
									'Vancouver',
									'Montreal',
									'Calgary',
									'Edmonton',
									'Ottawa',
									'Winnipeg',
									'Quebec City',
									'Hamilton',
									'Kitchener'
								];
					cities.forEach((city) => {
						const option = document.createElement('option');
						option.value = city;
						option.textContent = city;
						citySelector.appendChild(option);
					});
				}
			}
		});
		// sendData(testData)
	});

	const sendData = async (data: any) => {
		const loadBar = document.getElementById('loadBar');

		if (loadBar) loadBar.style.width = `10%`;

		try {
			const response = await fetch('/form', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(data)
			});

			if (loadBar) loadBar.style.width = `40%`;

			const result: TicketEventObject[] = await response.json();

			if (loadBar) loadBar.style.width = '62%';

			if(result.length > 0) {

			}
			console.log(result);
		} catch (error) {
			console.error('Error:', error);
		}
	};
</script>

<main
	style="overflow: hidden; z-index:1; background: radial-gradient(circle, transparent, #ba3b3b); padding;0; margin:-10px; width:100vw; height:100vh;"
>
	{#if eventsLoad}
		<div
			in:fade={{ duration: 500 }}
			style="position:absolute; width: 100vw; height:100vh; z-index:1; background-color: #00000080; backdrop-filter: blur(3px) saturate(20%); transition:all 1s ease-out, width 0s, height 0s; margin:0; padding:0; display: flex; align-items: center; justify-content: center;"
		>
			<div
				style="width: 100%; height:100px; display: flex; align-items: center; justify-content: center;"
			>
				<div
					id="LogoCont"
					style="width: 100px; height:100px; display: flex; position: relative; height:auto; align-content: center; justify-content: center;"
				>
					<img
						src={MiddleLogo}
						alt="logo"
						width="80px"
						style="display: flex; position: relative;"
					/>
					<div
						id="loadBar"
						style="position: absolute; width:0%; bottom:10.5px; left:20px; height:15px; background-color:#D9D9D9; border-radius:5px; border-top-left-radius: 10px; border-bottom-left-radius: 10px; transition: width .5s cubic-bezier(0.215, 0.610, 0.355, 1);"
					></div>
				</div>
			</div>
		</div>
	{/if}
	<div
		id="header"
		style="width: 100vw; height:100vh; position:absolute; top:0; pointer-events:none; user-select:none;"
	>
		<h1
			style="transform: rotate(-90deg); top:20%; left:1%; font-size:130px; font-family: Quantico-bold, sans-serif; color:#ba3b3b3b"
		>
			SEARCH YOUR
		</h1>

		<h1
			style="top:50%; left:60%; transform:rotate(90deg); font-family: Quantico-regular, sans-serif; color:#ff8c0060"
		>
			EVENTS
		</h1>
	</div>

	<form>
		<div id="locationBoxes" style="display: flex">
			<div class="form-group">
				<label for="locationCity">City</label>
				<div
					id="locationCity"
					style="border-top-right-radius: 0; border-bottom-right-radius: 0; border-right-width: 1px; display: flex; flex-direction: row;"
				>
					<img src={city} width="25px" height="25px" />
					<select
						id="citySelector"
						style="width: 460px; height: 100%; border-top-right-radius:0; border-bottom-right-radius:0"
					>
						<option value="">None</option>
					</select>
				</div>
			</div>
			<div class="form-group">
				<label for="locationCountry">Country</label>
				<div
					id="locationCountry"
					style="border-top-left-radius: 0; border-bottom-left-radius: 0; border-left-width: 1px; display: flex; flex-direction: row;"
				>
					<img src={location} width="25px" height="25px" />
					<select
						style="width: 470px; height: 100%; border-top-left-radius:0; border-bottom-left-radius:0"
					>
						<option value="">None</option>
						<option value="US">US</option>
						<option value="CA">Canada</option>
					</select>
				</div>
			</div>
		</div>

		<div class="form-group">
			<label for="datesBeginning">Beginning Date</label>
			<div id="datesBeginning" style="display: flex; flex-direction: row;">
				<img src={calendarPlus} width="25px" height="25px" />
				<input type="date" style="width: 470px; height: 100%;" />
			</div>
		</div>
		<div class="form-group">
			<label for="datesEnd">End Date</label>
			<div id="datesEnd" style="display: flex; flex-direction: row;">
				<img src={calendarMinus} width="25px" height="25px" />
				<input type="date" style="width: 470px; height: 100%;" />
			</div>
		</div>
		<div class="form-group">
			<label for="groupSize">Group Size</label>
			<div id="groupSize" style="display: flex; flex-direction: row;">
				<img src={person} width="25px" height="25px" />
				<input type="number" style="width: 470px; height: 100%;" />
			</div>
		</div>
		<button
			style="display: flex; align-items: center; justify-content: center;"
			on:click|preventDefault={() => {
				const city = (document.getElementById('citySelector') as HTMLSelectElement)?.value;
				const country = (document.querySelector('#locationCountry select') as HTMLSelectElement)
					?.value;
				const beginningDate = (document.querySelector('#datesBeginning input') as HTMLInputElement)
					?.value;
				const endDate = (document.querySelector('#datesEnd input') as HTMLInputElement)?.value;
				const groupSize = (document.querySelector('#groupSize input') as HTMLInputElement)?.value;

				let data = {
					location: {
						city,
						country
					},
					dates: {
						beginning: beginningDate,
						end: endDate
					},
					groupSize
				};

				eventsLoad = true;

				setTimeout(() => {
					sendData(data);
				}, 500);
			}}><img src={lightning} alt="submit" width="30px" /></button
		>
	</form>
</main>

<style>
	main {
		display: flex;
		justify-content: center;
		align-items: center;
		height: 100vh;
	}

	form {
		display: flex;
		flex-direction: column;
		gap: 1rem;
	}

	.form-group {
		display: flex;
		flex-direction: column;
	}

	label {
		margin-bottom: 0.5rem;
	}

	.form-group div {
		width: 500px;
		height: 50px;
		border-radius: 20px;
		border-color: rgba(139, 69, 19, 0.5);
		border-width: 5px;
		background-color: rgba(245, 222, 179, 0.7);
		border-style: solid;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	#locationBoxes div {
		width: 250px;
	}

	img {
		border-top-left-radius: 18px;
		border-bottom-left-radius: 18px;
		border-color: transparent;
		border-style: none;
		align-self: center;
		justify-self: center;
		display: flex;
		padding: 10px;
	}

	input,
	select {
		border-top-right-radius: 18px;
		border-bottom-right-radius: 18px;
		border-style: none;
		border-color: transparent;
		background-color: transparent;
	}

	button {
		width: 100px;
		height: 50px;
		border-radius: 15px;
		border-style: solid;
		color: white;
		background-color: #eb7f2c55;
		border-width: 3px;
		cursor: pointer;
		border-color: #00000030;
	}

	button:hover {
		cursor: pointer;
	}

	#header h1 {
		font-size: 80px;
		position: absolute;
	}

	html,
	main,
	body {
		padding: 0;
		margin: 0;
		overflow: hidden;
		width: 100vw;
		height: 100vh;
	}

	label {
		font-family: Tajawal, sans-serif;
		font-weight: lighter;
		margin-bottom: 5px;
	}
</style>
