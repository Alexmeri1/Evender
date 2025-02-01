<script customElements="PartyScreen">
	import './tempBG.scss';

	// Function to randomly expand dots
	function animateRandomDots() {
		// Select all pseudo-elements (dots)
		const dots = [
			document.querySelector('body::before'),
			document.querySelector('body::after'),
			document.querySelector('head::before'),
			document.querySelector('head::after')
		];

		// Filter out null values (if pseudo-elements are not accessible)
		const validDots = dots.filter((dot) => dot !== null);

		// Randomly select some dots to animate
        console.log(validDots)
		validDots.forEach((dot) => {
			if (Math.random() < 0.3) {
				// 30% chance to animate each dot
				// Add the expand class to trigger the animation
				dot.classList.add('expand');

				// Remove the class after the animation ends (5 seconds)
				setTimeout(() => {
					dot.classList.remove('expand');
				}, 5000); // 5 seconds
			}
		});

		// Repeat the process at random intervals
		setTimeout(animateRandomDots, Math.random() * 10000); // Random delay up to 10 seconds
	}

	// Start the animation
	animateRandomDots();
</script>

<head> </head>

<body> </body>
