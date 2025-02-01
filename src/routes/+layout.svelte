<script lang="ts">
    import { onMount } from "svelte";
    import { fade } from "svelte/transition";
  
    // import Loading from "$lib/resources/components/load_scr.svelte";
    import "../global.css";
    import NavBar from "$lib/resources/components/nav-bar.svelte";
  
    // export let data: {
    //   lang: string;
    //   release: boolean;
    // };
  
    // let navbar_scrolled = false;
    // let navbar_height = "100%";
    // let navbar_position = "absolute";
    let loaded: boolean = false;
  
    // Go in +layout.server.ts to change the boolean!!!
    let release: boolean = true; //
    // Go in +layout.server.ts to change the boolean!!!
  
    const wait_for_load = new Promise((resolve, _) => {
      let interval = setInterval(() => {
        if (loaded) {
          clearInterval(interval);
          resolve(null);
        }
      }, 1000);
    });
  
    onMount(() => {
      let win_load_t_out: [boolean, number] = [false, 400];
      console.log("onMount loaded");
  
      let interval = setInterval(() => {
        win_load_t_out[1]--;
        if (win_load_t_out[1] < 1 && !win_load_t_out[0]) {
          clearInterval(interval);
          console.error("window load timeout");
          load_paths();
        } else if (win_load_t_out[0]) {
          clearInterval(interval);
        }
      }, 0);
  
      const load_paths = () => {
        // if (
        //   window.location.pathname == "/coming_soon" ||
        //   window.location.pathname == "/terms" ||
        //   window.location.pathname == "/privacy"
        // )
        //   release = false;
  
        loaded = true;
      };
  
      window.addEventListener("load", () => {
        win_load_t_out[0] = true;
        console.log("Document loaded");
        load_paths();
      });
  
    //   navbar_position = "absolute";
    //   window.addEventListener("scroll", function () {
    //     let scrollPos = Math.round(window.scrollY);
    //     const navBarElement = document.querySelector("#nav-bar");
  
    //     if (window.scrollY < 40) {
    //       requestAnimationFrame(() => {
    //         (navBarElement as HTMLDivElement).style.opacity =
    //           `${1 - window.scrollY / 40}`;
    //       });
    //     }
  
    //     if (scrollPos >= 42 && !navbar_scrolled) {
    //       console.log("Open");
    //       (navBarElement as HTMLDivElement).style.opacity = "1";
  
    //       navBarElement.animate(
    //         [
    //           { transform: "scale(0.7)", top: "-75px" },
    //           { transform: "scale(1)", top: "0px" },
    //         ],
    //         {
    //           duration: 700,
    //           easing: "cubic-bezier(0.25, 0.1, 0.25, 1)",
    //         }
    //       );
    //       navbar_position = "fixed";
    //     } else if (scrollPos <= 41 && navbar_scrolled) {
    //       console.log("Close");
    //       navbar_position = "absolute";
    //     }
  
    //     navbar_scrolled = window.scrollY > 41 ? true : false;
    //   });
    });
  </script>
  
  {#await wait_for_load}
    <div
      in:fade={{ duration: 500 }}
      out:fade={{ duration: 1000 }}
      style="background-color: rgba(0,0,0,95); width:100%; height:100%; display:block; position:absolute; top:0;"
    >
      <!-- <Loading /> -->
    </div>
  {:then loaded}
    <div
      in:fade={{ duration: 1000, delay: 500 }}
      id="main"
      style="height:100%; width:100%; display: block; position:relative; background-color: black; overflow:hidden; overflow-y:visible;"
    >
      {#if release}
        <div
          id="nav-bar"
          style="width: auto; height:100%; position:absolute; top:0; left:0; z-index:99; user-select:none; pointer-events: none; transition:all 1s cubic-bezier(0.25, 0.1, 0.25, 1), opacity .3s cubic-bezier(0.25, 0.1, 0.25, 1); transform-origin:top; overflow:hidden"
        >
          <NavBar
          />
        </div>
      {/if}
  
      <div
        id="content"
        style="position: relative; width:100%; height:100%; display:flex; overflow-y:scroll"
      >
        <slot style="width: 100%; height:100%; position:relative" />
      </div>
    </div>
  {/await}
  
  <style>
    *{
        margin: 0;
    }
  </style>