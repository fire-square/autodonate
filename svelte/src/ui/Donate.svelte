<script>
  import { get_products } from '../api/getters.js';
  import media_path from '../api/media.js';
  import Modal from './Modal.svelte';

  let pay_form;

  $: elements = {};

  function pay() {
    for (let item in elements) {
      let input = document.createElement("input");
      pay_form.appendChild(input);
      input.value = elements[item];
      input.name = item;
      input.type = "hidden";
    }
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

  function plus_one(id, max) {
    let list = elements;
    ++list[id];
    if (list[id] > max)
      list[id] = max;
    elements = list;
  }

  function dash_one(id) {
    let list = elements;
    --list[id];
    if (list[id] <= 0)
      delete list[id];
    elements = list;
  }

  function update(id, elem, max) {
    let list = elements;
    let old = list[id];
    list[id] = elem.value;
    if (list[id] <= 0)
      delete list[id];
    if (parseInt(elem.value, 10).toString()===old.toString()) {
      elem.value = old;
      list[id] = old;
    }
    if (list[id] > max) {
      elem.value = max;
      list[id] = max;
    }
    elements = list;
  }

  function generate_link() {
    let url = new URL(window.location.origin + "/pay/");
    url.searchParams.append("items", JSON.stringify(elements));
    return url
  }

  function toggle_modal(id) {
    let e = document.getElementById("modal-"+id);
    e.classList.toggle("show")
    e.classList.toggle("visually-hidden")
  }

  let products = get_products();
</script>

<div class="overflow-hidden px-2 pt-4 pb-5" id="donate">
  <h2 class="fw-bold text-center pb-3 pt-5">Донат</h2>
  <div class="row row-cols-1 row-cols-lg-2 row-cols-xxl-3 align-items-stretch g-4 py-5">
    {#await products}
      {#each [1,2] as id}
        <div class="col">
          <div class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow">
            <div class="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1">
              <h2 class="pt-5 mt-5 mb-2 display-6 lh-1 fw-bold">Loading...</h2>
            </div>
          </div>
        </div>
      {/each}
    {:then products}
      {#each products as {pk, fields}}
        <div class="col">
          <div class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow" style="background-image: linear-gradient(rgba(255, 255, 255, 0), rgba(0, 0, 0, 0.6)), url('{media_path(fields.image)}'); background-size: cover;">
            <div class="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1">
              <h2 class="pt-5 mt-5 mb-2 display-6 lh-1 fw-bold">{fields.name}</h2>
              <input type="hidden" value="{pk}"/>
              <ul class="d-flex list-unstyled mt-auto">
                <li class="me-auto">
                  <h3>{fields.price}₽</h3>
                </li>
                <li class="d-flex align-items-center">
                  <div class="btn-group" role="group">
                    {#if (elements[pk])}
                        <button on:click={function() {add(pk)}} type="button" class="btn btn-success" style="text-decoration: none">
                          <i class="bi bi-bag-check-fill"></i>
                          В корзине
                        </button>
                        {#if (fields.max_in_cart > 1)}
                          <button on:click={function() {dash_one(pk)}} type="button" class="btn btn-light" style="text-decoration: none">
                            <i class="bi bi-dash"></i>
                          </button>
                          <input on:change="{function(event) {update(pk, event.target, fields.max_in_cart)}}" class="btn btn-light small" style="text-decoration: none; width: 50px;" value="{elements[pk]}" />
                          <button on:click={function() {plus_one(pk, fields.max_in_cart)}} type="button" class="btn btn-light" style="text-decoration: none">
                            <i class="bi bi-plus"></i>
                          </button>
                        {/if} 
                    {:else}
                      {#if (fields.long_description)}
                        <button on:click={function() {toggle_modal(pk)}} type="button" class="btn btn-primary" style="text-decoration: none">
                          <i class="bi bi-app"></i>
                          Подробнее
                        </button>
                      {/if}
                      <button on:click={function() {add(pk)}} type="button" class="btn btn-light" style="text-decoration: none">
                        <i class="bi bi-bag-plus"></i>
                        Добавить
                      </button>
                    {/if}
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      {/each}
    {/await}
  </div>

  {#if Object.keys(elements).length >= 1}
    <div class="text-center">
      <form method="post" action="/pay/" bind:this={pay_form}>
        <button type="submit" on:click={pay} class="btn btn-link text-center" style="text-decoration: none">Перейти к оплате</button>
      </form>
    </div>
  {:else}
    <div class="text-center">
      <button class="btn btn-link text-center disabled" style="text-decoration: none">Перейти к оплате</button>
    </div>
  {/if}
</div>

{#await products then products}
  {#each products as {pk, fields}}
    <Modal title={fields.name} id={pk}>
      <p>{fields.long_description}</p>
    </Modal>
  {/each}
{/await}
