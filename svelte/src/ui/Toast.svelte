<script>
    export let src = false;
    export let id;
    export let name;
    export let time = "Сейчас";
</script>

<div class="toast-container position-fixed bottom-0 end-0 p-3" id="toastPlacement">
  <div class="toast" role="alert" aria-live="assertive" aria-atomic="true" id="toast-{id}">
    <div class="toast-header">
      {#if !src}
        <img {src} class="rounded me-2" width="16" alt="avatar">
      {/if}
      <strong class="me-auto">{name}</strong>
      <small class="text-muted">{time}</small>
      <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
    </div>
    <div class="toast-body">
      <slot/>
    </div>
  </div>
</div>
