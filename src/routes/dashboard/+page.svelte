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

<div class="body">
  <ModelCard
    id="eventCard"
    height={"500px"}
    width={"400px"}
    intensity="-10, 5"
    background="linear-gradient(-45deg, cyan, blue)"
  />
</div>