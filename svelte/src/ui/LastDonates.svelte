<script>
  import axios from 'axios';

  export let timestamp = 0;
  export let donates = [];

  async function update() {
    let last = (await axios.get("/api/donate/latest", {params: {"timestamp": timestamp}})).data.answer;
    for (let item of donates)
      last.push(item);
    if (last.length >= 10)
      last.pop()
    donates = last;
    timestamp = Date.now();
  }

  setInterval(update, 10000);
  update();
</script>

{#each donates as { nick, item }, i}
  <div class="box">
    <p>{nick} купил {item}</p>
  </div>
{/each}
