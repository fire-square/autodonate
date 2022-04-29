<script>
  import {Toast as ToastBootstrap} from 'bootstrap';
  import Toast from './Toast.svelte';

  export let title;
  export let subtitle;
  export let players;
  export let ip;
  export let ip_elem;

  function copy() {
    if (!navigator.clipboard) {
      return
    }
    navigator.clipboard.writeText(ip_elem.innerText);
    new ToastBootstrap(document.getElementById("toast-copied-ip")).show();
  }

  setInterval(function () {
    players = Math.floor(Math.random() * 100);
  }, 5000)
</script>

<div class="px-4 py-5 my-5 text-center">
  <img class="d-block mx-auto mb-4" src="https://clipground.com/images/minecraft-block-png-1.png" alt="minecraft logo" width="72" height="72">
  <code class="h3 bg-secondary text-light rounded-1 px-2" bind:this={ip_elem}>{ip}</code>
  <h1 class="display-5 fw-bold">{title}</h1>
  <div class="col-lg-6 mx-auto">
    <p class="lead mb-4">{subtitle}</p>
    <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
      <button type="button" class="btn btn-primary btn-lg px-4 gap-3" on:click={copy}>Играть</button>
      <a href="/#donate"><button type="button" class="btn btn-outline-secondary btn-lg px-4">Донат</button></a>
    </div>
  </div>
</div>

<Toast name="Сервер" id="copied-ip">IP-адрес скопирован.</Toast>
