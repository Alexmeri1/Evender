<script lang="ts" customElements="nav-bar">
	import FullLogo from '$lib/resources/icons/FullLogo.png';
	import MiddleLogo from '$lib/resources/icons/MiddleLogo.png';

	import { slide } from 'svelte/transition';
	import { cubicOut, cubicIn } from 'svelte/easing';

	import '$root/global.scss';
	import { redirect } from '@sveltejs/kit';

	export let simpl_bar = true;

	setInterval(() => {
		simpl_bar = !simpl_bar;
	}, 5000);
</script>

<div
	id="nav-bar-container"
	style="width: 100vw; display:flex; position:absolute; height:100px; z-index:4; align-self:center; justify-self: center; align-items:center; justify-content: center;"
>
	{#if !simpl_bar}
		<div
			in:slide={{ axis: 'y', duration: 700, easing: cubicOut, delay: 700 }}
			out:slide={{ axis: 'y', duration: 700, easing: cubicIn }}
			style="position: absolute; width:80vw; height:80px; background-color:#00000070; z-index:4; display:flex; align-items:center; justify-content: center; border-radius:15px; backdrop-filter:blur(3px);"
		>
			<div class="wing left-wing">
				<a class="underlined-text" href="" style="--underline-color:#ffffff;">About Us</a>
				<a class="underlined-text" href="" style="--underline-color:#FF8C00;">Fill the form</a>
			</div>
			<a
				style="background: none; border: none; padding: 0; cursor: pointer;"
				href="/"
			>
				<img src={FullLogo} alt="fullLogo" height="50px" style="padding: 20px;" />
			</a>
			<div class="wing right-wing">
				<a class="underlined-text" href="" style="--underline-color:#4e7fcc;">Dashboard</a>
				<a class="underlined-text" href="" style="--underline-color:#ba3b3b;">Sign-In</a>
			</div>
		</div>
	{:else}
		<div
			in:slide={{ axis: 'y', duration: 700, delay: 700, easing: cubicOut }}
			out:slide={{ axis: 'y', duration: 700, easing: cubicIn }}
			style="position: absolute; width:40vw; height:80px; background-color:#00000050; z-index:4; display:flex; align-self:center; justify-self: center; align-items:center; justify-content: center; border-radius:15px; backdrop-filter:blur(6px);"
		>
			<a
				style="background: none; border: none; padding: 0; cursor: pointer;"
				href="/"
			>
				<img src={MiddleLogo} alt="middleLogo" height="35px" style="padding: 20px; margin-left:0" />
			</a>
			<div class="wing left-wing">
				<a class="underlined-text" href="" style="--underline-color:#ffffff;">About Us</a>
			</div>
			<div class="wing right-wing">
				<a class="underlined-text" href="" style="--underline-color:#4e7fcc;">Dashboard</a>
				<button
					id="sign-in-btn"
					style="background:linear-gradient(45deg, #d46b6b80, #ba3b3b70); border:none; border-radius:10px; color:white; font-size:15px; width:120px; height:40px; position:relative; margin-left:60px; cursor:pointer; transition:background .5s ease-out;"
				>
					Sign-In
				</button>
			</div>
		</div>
	{/if}
</div>

<style>
	.wing {
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
		height: 80px;
		position: relative;
	}

	.wing a {
		color: white;
		font-size: 15px;
		font-family: Tajawal, sans-serif;
		font-weight: 500;
		text-decoration: none;
		margin: 20px;
	}

	.left-wing {
		align-self: flex-start;
		margin-left: 20px;
	}

	.right-wing {
		align-self: flex-end;
		margin-right: 20px;
	}
</style>
