<script lang="ts">
	import './styles.css';
	import '$root/global.scss';
	import ModelCard from '$lib/resources/components/modelCard.svelte';
	import leftArrow from '$lib/resources/icon/img/left_icon.svg';
	import rightArrow from '$lib/resources/icon/img/right_icon.svg';
	import deco01 from '$lib/resources/icon/img/circles2.svg';
</script>

<svelte:head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="initial-scale=1.0" />

	<title>Dashboard</title>
</svelte:head>

<div class="body" style="overflow:hidden;">
	<div id="modelcard-container">
		<ModelCard
			id="eventCard"
			height={'500px'}
			width={'400px'}
			intensity="-10, 5"
			background="black;"
			border="solid"
			style="border-color: var(--pink);
    border-radius: 20px;
    border-width:10px;
    box-shadow: 0px 0px 10px var(--pink);"
		/>
	</div>
</div>

<div class="bg">
	<img id="bg-deco01" src={deco01} alt="Decorative Circles" />
</div>
<div class="bg">
	<img id="bg-deco02" src={deco01} alt="Decorative Circles" />
</div>

<button type="button" class="arrows">
	<img id="right-arrow" src={rightArrow} alt="right arrow" />
</button>

<button type="button" class="arrows">
	<img id="left-arrow" src={leftArrow} alt="left arrow" />
</button>

<div class="decks">
	<button><h2>DOWNLOAD</h2></button>
</div>
