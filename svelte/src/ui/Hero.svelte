<script lang="ts">
  import { get } from './../api/getters';
  import {Toast as ToastBootstrap} from 'bootstrap';
  import Toast from './Toast.svelte';

  let hero = get("/api/config/hero");
  let server = get("/api/config/server");
  export let ip_elem: undefined | HTMLElement;

  function copy() {
    if (!navigator.clipboard) {
      return
    }
    navigator.clipboard.writeText(ip_elem.innerText);
    new ToastBootstrap(document.getElementById("toast-copied-ip")).show();
  }
</script>

<div class="px-4 py-5 my-5 text-center">
  {#await hero}
    <code class="h3 bg-secondary text-light rounded-1 px-2">Загрузка...</code>
    <h1 class="display-5 fw-bold">Загрузка...</h1>
    <div class="col-lg-6 mx-auto">
      <p class="lead mb-4">Загрузка...</p>
      <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
        <button type="button" class="btn btn-primary btn-lg px-4 gap-3">Играть</button>
        <button on:click={function(){document.location="/#donate"}} type="button" class="btn btn-outline-secondary btn-lg px-4">Донат</button>
      </div>
    </div>
  {:then hero}
    <img class="d-block mx-auto mb-4" src="https://clipground.com/images/minecraft-block-png-1.png" alt="minecraft logo" width="72" height="72">
    {#await server}
      <code class="h3 bg-secondary text-light rounded-1 px-2">Загрузка...</code>
    {:then server}
      <code class="h3 bg-secondary text-light rounded-1 px-2" bind:this={ip_elem}>{JSON.parse(server.value).ip}</code>
    {/await}
    <h1 class="display-5 fw-bold">{JSON.parse(hero.value).title}</h1>
    <div class="col-lg-6 mx-auto">
      <p class="lead mb-4">{JSON.parse(hero.value).subtitle}</p>
      <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
        <button type="button" class="btn btn-primary btn-lg px-4 gap-3" on:click={copy}>Играть</button>
        <button on:click={function(){document.location="/#donate"}} type="button" class="btn btn-outline-secondary btn-lg px-4">Донат</button>
      </div>
    </div>
  {/await}
</div>

<Toast name="Сервер" id="copied-ip">IP-адрес скопирован.</Toast>
