<script lang="ts">
	import './styles.css';
	import '../../global.css';
	import ModelCard from '$lib/resources/components/modelCard.svelte';
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
    height={"500px"}
    width={"400px"}
    intensity="-10, 5"
    background=black;
    border= "solid"
    style="border-color: var(--pink);
    border-radius: 20px;
    border-width:10px;
    box-shadow: 0px 0px 10px var(--pink);"
    
  />
  </div>

  
</div>




<div class="bg">
 <img id="bg-deco01" src="/src/lib/resources/icon/img/circles2.svg" alt="Decorative Circles"/>
</div>
<div class="bg">
<img id="bg-deco02" src="/src/lib/resources/icon/img/circles2.svg" alt="Decorative Circles"/>
</div>



<button type="button" class="arrows">
  <img id="right-arrow" src="/src/lib/resources/icon/img/right_icon.svg" alt="right arrow"/>
</button>

<button type="button" class="arrows">
  <img id="left-arrow" src="/src/lib/resources/icon/img/left_icon.svg" alt="left arrow"/>
</button>

<div class="decks">
  <!-- to finish -->
<!-- <h1>DECKS</h1> -->
</div>