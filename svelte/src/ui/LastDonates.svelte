<script>
  import { get_latest_donations, get_product } from '../api/getters';
  import LastDonateCard from './LastDonateCard.svelte';

  export let timestamp = 0;
  export let donates = [];

  async function update() {
    let list = await get_latest_donations();
    console.log(list);
    for (let item of donates)
      list.push(item);
    if (list.length > 6)
      list.pop()
    donates = list;
    timestamp = Date.now();
  }

  update();
</script>

<div class="overflow-hidden">
  <h2 class="fw-bold text-center pb-3 pt-5">Последние донаты</h2>
  <div class="row row-cols-1 row-cols-lg-6 row-cols-md-3 row-cols-2 g-2 g-lg-3 px-2">
    {#if donates.length == 0}
      <div class="col">
        <div class="card" style="width: 100%;">
          <div class="card-body">
            Пока донатов не было!
          </div>
        </div>
      </div>
    {/if}
    {#each donates as { pk, fields }, i}
      <LastDonateCard fields={fields} product={get_product(fields.product)} pk={pk} />
    {/each}
  </div>
</div>
