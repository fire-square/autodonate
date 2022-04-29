<script>
  export let title;
  export let element;
  export let id;
  import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

  function close() {
    element.classList.toggle("show");
    setTimeout(function() {
      element.remove();
      dispatch('modalclose', {
        id
      });
    }, 500)
  }
</script>

<div bind:this={element} class="modal fade show text-dark" tabindex="-1" style="display: block;" aria-modal="true" role="dialog"
      id="modal-{id}">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLiveLabel">{title}</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <slot></slot>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" on:click={close}>Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
