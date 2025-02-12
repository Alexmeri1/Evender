<script lang="ts" customElements="mobile-warn">
	import '$root/global.scss';
	import MainLogo from '$lib/resources/icons/Webp/Low-FullLogo.webp';
</script>

<div
	id="mainCont"
	style="width: 100%; height:100%; z-index:2; background-color:#000; display:flex; align-items: center; justify-content: center; flex-direction: column; position:absolute; top:0; overflow:hidden; transform: scale(90%); transform-origin: center;"
>
	<div id="textCont" style="display: block; width: 90%; height:auto; padding:40px;">
		<h1 class="neonText flicker" style="text-align: center; font-family: Tajawal, sans-serif; font-size:20px; color:white; font-weight: bold; --neonStart-color:#ffffff85; --neonEnd-color:#ffffff50">
			Evender is still not available for this Platform or Browser
		</h1>
        <br/>
		<h1
			style="text-align: center; font-family: Tajawal, sans-serif; font-size:22px; color: white;"
		>
			(╥﹏╥)
		</h1>
	</div>
	<div
		id="logoCont"
		style="width: 100%; height:auto; display: flex; align-items: center; justify-content: center;"
	>
		<img src={MainLogo} alt="MainLogo" width="100px" style="opacity: .5;"/>
	</div>
</div>
