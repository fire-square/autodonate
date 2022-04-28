<script>
  import axios from 'axios';

  export let timestamp = 0;
  export let donates = [];

  async function update() {
    let list = (await axios.get("/api/donate/latest", {params: {"timestamp": timestamp}})).data.donates.slice(4);
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
    {#each donates as { id, name, price, player }, i}
      <div class="col">
        <div class="card" style="width: 100%;">
          <div class="card-body">
            <h5 class="card-title">
              <img width="20" class="rounded mb-1" alt="{player.nick} player head" src="https://cravatar.eu/avatar/{player.nick}.png">
              {player.nick}
            </h5>
            <h6 class="card-subtitle mb-2 text-muted">Купил {name} за {price}$.</h6>
          </div>
        </div>
      </div>
    {/each}
  </div>
</div>
