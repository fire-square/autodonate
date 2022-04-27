<script>
  export let modal;

  function close() {
    modal.classList.toggle("is-active");
  }
</script>

<div class="modal" bind:this={modal} id="modal">
  <div class="modal-background"></div>
  <div class="modal-content">
    <div class="box">
      test
    </div>
  </div>
  <button class="modal-close is-large" aria-label="close" on:click={close}></button>
</div>
