<script lang="ts">
  import { get } from '../api/getters';
  import LastDonateCard from './LastDonateCard.svelte';
</script>

<div class="overflow-hidden">
  <h2 class="fw-bold text-center pb-3 pt-5">Последние донаты</h2>
  <div class="row row-cols-1 row-cols-lg-6 row-cols-md-3 row-cols-2 g-2 g-lg-3 px-2">
    {#await get("/api/donation/")}
      <div class="col">
        <div class="card" style="width: 100%;">
          <div class="card-body">
            Загрузка...
          </div>
        </div>
      </div>
    {:then donates}
      {#if donates.length == 0}
        <div class="col">
          <div class="card" style="width: 100%;">
            <div class="card-body">
              Пока донатов не было!
            </div>
          </div>
        </div>
      {/if}
      {#each donates as donate}
        <LastDonateCard {donate} id={donate.id} />
      {/each}
    {/await}
  </div>
</div>
