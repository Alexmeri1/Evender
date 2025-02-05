<script customElements="PartyScreen">
</script>

<div id="html" style="background-color: black; width:100vw; height:100vh">
	<div id="head" style="background: black;">
		<span></span>
		<span></span>
	</div>

	<div id="body" style="background: black;">
		<span></span>
		<span></span>
	</div>
</div>

<style lang="scss">
	@mixin dots($count) {
		$colors: #faffec, #ff8c00, #ffc021, #ff0000, #000, #c44545, #ff1e1e, #ff0000;
		$text-shadow: ();
		@for $i from 0 through $count {
			$width: random(3) + 0.2 + em; // Random width between 1em and 3em
			$blur: 5px + (random() * 6px); // Random blur radius between 5px and 7px
			$color: nth($colors, random(length($colors)));
			$text-shadow:
				$text-shadow,
				(-0.5+ (random()) * 3) + em (-0.5+ (random()) * 3) + em $blur $color;
		}
		text-shadow: $text-shadow;
	}

	@keyframes gradient {
		0% {
			background: #000000;
		}
		10% {
			background: #4e4e4e;
		}
	}

	#html {
		font: 20vmin Serif;
		overflow: hidden;
		background-color: #000000;
		// animation: gradient 100s ease infinite;
	}

	#body,
	#head {
		display: block;
		font-size: 52px;
		color: transparent;
	}

	#head::before,
	#head::after,
	#body::before,
	#body::after {
		position: fixed;
		top: 50%;
		left: 50%;
		width: 3em;
		height: 3em;
		content: ':';
		mix-blend-mode: screen;
		will-change: transform, font-size;
		animation: 80s -27s move infinite ease-in-out alternate;
	}

	#body::before {
		@include dots(20);
		animation-duration: 64s;
		animation-delay: -27s;
	}

	#body::after {
		@include dots(20);
		animation-duration: 63s;
		animation-delay: -32s;
	}

	#head::before {
		@include dots(20);
		animation-duration: 62s;
		animation-delay: -23s;
	}

	#head::after {
		@include dots(20);
		animation-duration: 61s;
		animation-delay: -19s;
	}

	@keyframes move {
		from {
			transform: rotate(0deg) scale(12) translateX(-20px);
		}
		to {
			transform: rotate(360deg) scale(18) translateX(10px);
		}
	}

	// New animation for random dots expanding
	@keyframes expand {
		0%,
		100% {
			font-size: 52px;
		}
		50% {
			font-size: 72px; // Expand to 72px
		}
	}

	// Apply the expand animation to random dots
	@for $i from 1 through 10 {
		// Adjust the number of dots to animate
		#body::before,
		#body::after,
		#head::before,
		#head::after {
			&:nth-child(#{$i}) {
				animation:
					80s -27s move infinite ease-in-out alternate,
					5s expand infinite ease-in-out;
				animation-delay:
					-27s,
					random() * 10s; // Random delay for expansion
			}
		}
	}
</style>
