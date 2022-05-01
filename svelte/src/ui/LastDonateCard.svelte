<script lang="ts">
  import type { Donation } from './../types';

  export let id: string;
  export let donate: Donation;
</script>

<div class="col">
  <div class="card" style="width: 100%;" id="donation-{id}">
    <div class="card-body">
        <h5 class="card-title">
          <img width="20" class="rounded mb-1" alt="{donate.player.nickname} player head" src="https://cravatar.eu/avatar/{donate.player.nickname}.png"> {donate.player.nickname}
        </h5>
        <h6 class="card-subtitle mb-2 text-muted">Купил {donate.product.name} за {donate.product.price}.</h6>
    </div>
  </div>
</div>
