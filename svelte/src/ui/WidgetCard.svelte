<script lang="ts">
  import { spring } from 'svelte/motion';
  import { onMount } from 'svelte';

  let element: HTMLElement;
  let select: HTMLElement;
  let coords = spring({ x: 0, y: 0 }, {
        stiffness: 0.1,
        damping: 0.25
    });
  let active: boolean = false;
  let start_coords;
  const disableselect = () => {  
      return false
  }
  let selected: boolean = false;

  onMount(async () => {
    start_coords = element.getBoundingClientRect();
    coords = spring({ x: start_coords.left, y: start_coords.top }, {
        stiffness: 0.1,
        damping: 0.25
    });
    select = document.getElementById("select");
  });

  function move(e: MouseEvent) {
    if (active) {
        document.onselectstart = disableselect;
        coords.set({ x: e.clientX, y: e.clientY });
        let rect = select.getBoundingClientRect();

        if (rect.left < e.clientX && e.clientX < rect.left + rect.width &&
            rect.top < e.clientX && e.clientY < rect.top + rect.height ) {
            select.style.backgroundColor = "yellow";
            selected = true;
        } else {
            select.style.backgroundColor = "red";
            selected = false;
        }
    }
  }

  function mouseup() {
    if (active) {
        document.onselectstart = null;
        active = false;
        if (selected) {
            select.style.backgroundColor = "red";
            select.appendChild(element);
        } else {
            coords.set({ x: start_coords.left, y: start_coords.top });
            select.removeChild(element);
        }
    }
  }
</script>

<svelte:window on:mousemove="{move}" on:mouseup="{mouseup}"/>

<div class="card position-absolute" bind:this="{element}"
     style="width: 18rem; left: {$coords.x}; top: {$coords.y}">
  <div style="width: 100%; height: 50px;" class="bg-dark" on:mousedown="{() => active = true}"/>
  <div class="card-body">
    <h5 class="card-title">Заголовок</h5>
    <p class="card-text">Текст - рыба, показыающий насколько кофоб крутой.</p>
    <a href="#" class="btn btn-primary">Кофоб крут</a>
  </div>
</div>

<div id="select" style="width: 200px; height: 200px; background-color: red"></div>
