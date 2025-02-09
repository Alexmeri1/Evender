<script lang="ts" customElements="transition-screen">
	import { slide } from 'svelte/transition';

    let startAnim = false;

    setTimeout(() => {
        startAnim = !startAnim
    }, 100)
</script>

{#if startAnim}
	<div
		in:slide={{ axis: 'y', duration: 6000, delay:2000 }}
		class="wave"
		id="main"
		style="width: 200vw; position:absolute; top:0; height:150vh; display:flex; align-items: center; justify-content: center; background-color: #00000075; backdrop-filter: blur(5px); z-index:2; padding:0; margin:0;"
	></div>
{/if}

<style>
	.wave {
		--size: 70px;
		--m: 0.9;
		--p: calc(var(--m) * var(--size));
		--R: calc(var(--size) * sqrt(var(--m) * var(--m) + 1));

		mask:
			radial-gradient(var(--R) at 50% calc(100% - (var(--size) + var(--p))), #000 99%, #0000 101%)
				calc(50% - 2 * var(--size)) 0 / calc(4 * var(--size)) 100%,
			radial-gradient(var(--R) at 50% calc(100% + var(--p)), #0000 99%, #000 101%) 50%
				calc(100% - var(--size)) / calc(4 * var(--size)) 100% repeat-x;
		background: linear-gradient(0deg, rgb(39, 39, 39), black);
		opacity: 0.96;
		height: 200px;
	}

	#main {
        animation: moveBG 5s linear;
	}

	@keyframes moveBG {
		from {
			left: 0;
		}
		to {
			left: -100vw;
		}
	}
</style>
