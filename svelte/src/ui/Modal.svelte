<script lang="ts">
  // @ts-expect-error
  import { Remarkable } from 'remarkable';

  export let title: string;
  export let id: string;
  export let md: string | null = null;

  let renderer = new Remarkable();
  let text = "";
  if (md != null) {
    text = renderer.render(md);
  }

  let element: Element;

  function toggle() {
    element.classList.toggle("show");
    setTimeout(function () {
      element.classList.toggle("visually-hidden");
    }, 500)
  }
</script>

<div bind:this={element} class="modal fade visually-hidden text-dark" tabindex="-1" style="display: block;" aria-modal="true" role="dialog"
      id="modal-{id}" data-backdrop="static" data-keyboard="false">
  <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLiveLabel">{title}</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" on:click={toggle}></button>
      </div>
      <div class="modal-body">
        {#if (md != null)}
          {@html text}
        {:else}
          <slot></slot>
        {/if}
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" on:click={toggle}>Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
