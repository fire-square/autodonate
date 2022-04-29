<script>
  export let fields;
  export let product;
  export let pk;
</script>

<div class="col">
  <div class="card" style="width: 100%;" id="donation-{pk}">
    <div class="card-body">
      {#await product}
        Loading...
      {:then product}
        <h5 class="card-title">
          <img width="20" class="rounded mb-1" alt="{fields.player} player head" src="https://cravatar.eu/avatar/{fields.player}.png">
          {fields.player}
        </h5>
        <h6 class="card-subtitle mb-2 text-muted">Купил {product.fields.name} за {product.fields.price}.</h6>
      {/await}
    </div>
  </div>
</div>
