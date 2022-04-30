<script lang="ts">
  import { get } from '../api/getters';

  export let id;
  export let donate;
</script>

<div class="col">
  <div class="card" style="width: 100%;" id="donation-{id}">
    <div class="card-body">
      {#await donate}
        Загрузка...
      {:then donate}
        <h5 class="card-title">
          {#await get(donate.player)}
            <img width="20" class="rounded mb-1" alt="loading player head" src="https://cravatar.eu/avatar/steve.png"> Загрузка...
          {:then player}
            <img width="20" class="rounded mb-1" alt="{player.nickname} player head" src="https://cravatar.eu/avatar/{player.nickname}.png"> {player.nickname}
          {/await}
        </h5>
        {#await get(donate.product)}
          <h6 class="card-subtitle mb-2 text-muted">Купил ... за ...</h6>
        {:then product}
          <h6 class="card-subtitle mb-2 text-muted">Купил {product.name} за {product.price}.</h6>
        {/await}
      {/await}
    </div>
  </div>
</div>
