<script lang="ts">
	import { cn } from './cn.ts';

	export let className: string | undefined = undefined;
	export let translateX: number | string | undefined = 0;
	export let translateY: number | string | undefined = 0;
	export let translateZ: number | string | undefined = 0;
	export let rotateX: number | string | undefined = 0;
	export let rotateY: number | string | undefined = 0;
	export let rotateZ: number | string | undefined = 0;
	export let isMouseEntered: boolean = false;
	export let style: string | undefined = undefined;
	export let id: string | undefined = undefined;

	let ref: HTMLDivElement;
	
	$: isMouseEntered, handleAnimations();

	const handleAnimations = () => {
		if (!ref) return;
		ref.style.transition = 'transform 2s ease-in-out';			
		ref.style.transform = `translateX(0px) translateY(0px) translateZ(0px) rotateX(0deg) rotateY(0deg) rotateZ(0deg)`;

		if (isMouseEntered) {
			ref.style.transform = `translateX(${translateX}px) translateY(${translateY}px) translateZ(${translateZ}px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) rotateZ(${rotateZ}deg)`;
		} else {
			ref.style.transform = `translateX(0px) translateY(0px) translateZ(0px) rotateX(0deg) rotateY(0deg) rotateZ(0deg)`;
		}
	};
</script>

<div style="{style ? style : ''}"
	bind:this={ref}
	class={cn('w-fit transition duration-200 ease-linear', className)}
	id={id}
	{...$$props}
>
	<slot />
</div>