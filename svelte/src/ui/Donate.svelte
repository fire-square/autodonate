<script lang="ts">
  import { get } from './../api/getters';
  import type { Product } from './../types';
  import Modal from './Modal.svelte';

  let pay_form: HTMLFormElement;

  let elements = {};
  let groups: string[] = [];

  function pay(): void {
    for (let item in elements) {
      let input = document.createElement("input");
      pay_form.appendChild(input);
      input.value = elements[item];
      input.name = item;
      input.type = "hidden";
    }
  }

  function add(product: Product): void {
    let list = elements;
    let groups_our = groups;
    if (!list[product.id]) {
      if (groups_our.includes(product.group)) {
        return;
      }
      list[product.id] = 1;
      if (product.group != null)
      groups_our.push(product.group);
    } else {
      delete list[product.id];
      if (product.group != null)
        delete groups_our[groups_our.indexOf(product.group)];
    }
    elements = list;
    groups = groups_our;
  }

  function plus_one(id: string, max: number): void {
    let list = elements;
    ++list[id];
    if (list[id] > max)
      list[id] = max;
    elements = list;
  }

  function dash_one(product: Product): void {
    let list = elements;
    let groups_our = groups;
    --list[product.id];
    if (list[product.id] <= 0)
      delete list[product.id];
    if (product.group != null)
      delete groups_our[groups_our.indexOf(product.group)];
    groups = groups_our;
    elements = list;
  }

  // event.target haven't any right annotations. idk what do.
  function update(id: string, elem, max: number): void {
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
      elem.value = max.toString();
      list[id] = max;
    }
    elements = list;
  }

  function toggle_modal(id: string): void {
    let e = document.getElementById("modal-"+id);
    e.classList.toggle("show")
    e.classList.toggle("visually-hidden")
  }

  let products: Promise<Product[]> = get("/api/product/");
</script>

<div class="overflow-hidden px-2 pt-4 pb-5" id="donate">
  <h2 class="fw-bold text-center pb-3 pt-5">Донат</h2>
  <div class="row row-cols-1 row-cols-lg-2 row-cols-xxl-3 align-items-stretch g-4 py-5">
    {#await products}
      <!-- Show two 'Loading...' panels -->
      {#each [1,2] as _}
        <div class="col">
          <div class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow">
            <div class="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1">
              <h2 class="pt-5 mt-5 mb-2 display-6 lh-1 fw-bold">Loading...</h2>
            </div>
          </div>
        </div>
      {/each}
    {:then products}
      {#if products.length == 0}
        <div class="col">
          <div class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow">
            <div class="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1">
              <p class="display-6 lh-1 fw-bold">Нет предметов для отображения!</p>
            </div>
          </div>
        </div>
      {/if}
      {#each products as product}
        <div class="col">
          <div class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow" style="background-image: linear-gradient(rgba(255, 255, 255, 0), rgba(0, 0, 0, 0.6)), url('{product.image}'); background-size: cover;">
            <div class="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1">
              <h2 class="pt-5 mt-5 mb-2 display-6 lh-1 fw-bold">{product.name}</h2>
              <input type="hidden" value="{product.id}"/>
              <ul class="d-flex list-unstyled mt-auto">
                <li class="me-auto">
                  <h3>{product.price}₽</h3>
                </li>
                <li class="d-flex align-items-center">
                  <div class="btn-group" role="group">
                    {#if (elements[product.id])}
                        <button on:click={function() {add(product)}} type="button" class="btn btn-success" style="text-decoration: none">
                          <i class="bi bi-bag-check-fill"></i>
                          В корзине
                        </button>
                        {#if (product.max_in_cart > 1)}
                          <button on:click={function() {dash_one(product)}} type="button" class="btn btn-light" style="text-decoration: none">
                            <i class="bi bi-dash"></i>
                          </button>
                          <input on:change="{function(event) {update(product.id, event.target, product.max_in_cart)}}" class="btn btn-light small" style="text-decoration: none; width: 50px;" value="{elements[product.id]}" />
                          <button on:click={function() {plus_one(product.id, product.max_in_cart)}} type="button" class="btn btn-light" style="text-decoration: none">
                            <i class="bi bi-plus"></i>
                          </button>
                        {/if}
                    {:else}
                      {#if (product.long_description)}
                        <button on:click={function() {toggle_modal(product.id)}} type="button" class="btn btn-primary" style="text-decoration: none">
                          <i class="bi bi-app"></i>
                          Подробнее
                        </button>
                      {/if}
                      {#if groups.includes(product.group)}
                        <button on:click={function() {add(product)}} type="button" class="disabled btn btn-light" style="text-decoration: none">
                          <i class="bi bi-bag-plus"></i>
                          Добавить
                        </button>
                      {:else}
                        <button on:click={function() {add(product)}} type="button" class="btn btn-light" style="text-decoration: none">
                          <i class="bi bi-bag-plus"></i>
                          Добавить
                        </button>
                      {/if}
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
      <form>
        <button class="btn btn-link text-center disabled" style="text-decoration: none">Перейти к оплате</button>
      </form>
    </div>
  {/if}
</div>

{#await products then products}
  {#each products as product}
    <Modal title={product.name} id={product.id} md={product.long_description}/>
  {/each}
{/await}
