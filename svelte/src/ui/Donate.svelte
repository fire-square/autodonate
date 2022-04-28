<script>
  export let btn_pay;

  $: elements = {};

  function pay() {
    document.location = generate_link();
  }

  function add(id) {
    let list = elements;
    if (!list[id]) {
      list[id] = 1;
    } else {
      delete list[id];
    }
    elements = list;
  }

  function plus_one(id) {
    let list = elements;
    ++list[id];
    if (list[id] > 20)
      list[id] = 20;
    elements = list;
  }

  function dash_one(id) {
    let list = elements;
    --list[id];
    if (list[id] <= 0)
      delete list[id];
    elements = list;
  }

  function update(id, elem) {
    let list = elements;
    let old = list[id];
    list[id] = elem.value;
    if (list[id] <= 0)
      delete list[id];
    if (parseInt(elem.value, 10).toString()===old.toString()) {
      elem.value = old;
      list[id] = old;
    }
    if (list[id] > 20) {
      elem.value = 20;
      list[id] = 20;
    }
    elements = list;
  }

  function generate_link() {
    let url = new URL(window.location.origin + "/pay/");
    url.searchParams.append("items", JSON.stringify(elements));
    return url
  }
</script>

<div class="overflow-hidden px-2 pt-4 pb-5" id="donate">
  <h2 class="fw-bold text-center pb-3 pt-5">Донат</h2>
  <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 align-items-stretch g-4 py-5">
    {#each [1,2,3] as id}
      <div class="col">
        <div class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow" style="background-image: linear-gradient(rgba(255, 255, 255, 0), rgba(0, 0, 0, 0.6)), url('https://minecraftom.ru/uploads/posts/2021-06/1622893537_2019-09-06-14-1.png'); background-size: cover;">
          <div class="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1">
            <h2 class="pt-5 mt-5 mb-2 display-6 lh-1 fw-bold">Флай</h2>
            <input type="hidden" value="{id}"/>
            <ul class="d-flex list-unstyled mt-auto">
              <li class="me-auto">
                <h3>25$</h3>
              </li>
              <li class="d-flex align-items-center">
                {#if (elements[id])}
                  <div class="btn-group" role="group">
                    <button on:click={function() {add(id)}} type="button" class="btn btn-success" style="text-decoration: none">
                      <i class="bi bi-bag-check-fill"></i>
                      В корзине
                    </button>
                    <button on:click={function() {plus_one(id)}} type="button" class="btn btn-light" style="text-decoration: none">
                      <i class="bi bi-plus"></i>
                    </button>
                    <input on:change="{function(event) {update(id, event.target)}}" class="btn btn-light small" style="text-decoration: none; width: 50px;" value="{elements[id]}" />
                    <button on:click={function() {dash_one(id)}} type="button" class="btn btn-light" style="text-decoration: none">
                      <i class="bi bi-dash"></i>
                    </button>
                  </div>
                {:else}
                  <button on:click={function() {add(id)}} type="button" class="btn btn-light" style="text-decoration: none">
                    <i class="bi bi-bag-plus"></i>
                    Добавить
                  </button>
                {/if}
              </li>
            </ul>
          </div>
        </div>
      </div>
    {/each}
  </div>

  {#if Object.keys(elements).length >= 1}
    <div class="text-center">
      <button on:click={pay} class="btn btn-link text-center" style="text-decoration: none">Перейти к оплате</button>
    </div>
  {:else}
    <div class="text-center">
      <button class="btn btn-link text-center disabled" style="text-decoration: none">Перейти к оплате</button>
    </div>
  {/if}
</div>

