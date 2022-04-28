<script>
  let elements = [];

  function add(event) {
    let list = elements;
    let id = event.target.parentElement.parentElement.parentElement.getElementsByTagName('input')[0].value;
    if (!list.includes(id)) {
      list.push(id);
      event.target.innerText = "В корзине";
      event.target.classList.add("btn-success");
      event.target.classList.remove("btn-light");
    } else {
      let index = list.indexOf(id);
      if (index !== -1) {
        list.splice(index, 1);
      }
      event.target.innerText = "Добавить";
      event.target.classList.add("btn-light");
      event.target.classList.remove("btn-success");
    }
    elements = list;
  }

  function generate_link() {
    let url = new URL(window.location.origin + "/pay/");
    url.searchParams.append("items", encodeURIComponent(JSON.stringify(elements)))
    return url
  }
</script>

<div class="overflow-hidden px-2 pt-4 pb-5" id="donate">
  <h2 class="fw-bold text-center pb-3 pt-5">Донат</h2>
  <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 align-items-stretch g-4 py-5">
    <div class="col">
      <div class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow" style="background-image: linear-gradient(rgba(255, 255, 255, 0), rgba(0, 0, 0, 0.6)), url('https://minecraftom.ru/uploads/posts/2021-06/1622893537_2019-09-06-14-1.png'); background-size: cover;">
        <div class="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1">
          <h2 class="pt-5 mt-5 mb-2 display-6 lh-1 fw-bold">Флай</h2>
          <input type="hidden" value="1"/>
          <ul class="d-flex list-unstyled mt-auto">
            <li class="me-auto">
              <h3>25$</h3>
            </li>
            <li class="d-flex align-items-center">
              <button on:click={add} type="button" class="btn btn-light" style="text-decoration: none">Добавить</button>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <div class="col">
      <div class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow-lg" style="background-image: linear-gradient(rgba(255, 255, 255, 0), rgba(0, 0, 0, 0.6)), url('https://creativus.do.am/mine/gorod/6xnUtKX_6388316_lrg.jpg'); background-size: cover;">
        <div class="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1">
          <h2 class="pt-5 mt-5 mb-2 display-6 lh-1 fw-bold">Креатив</h2>
          <input type="hidden" value="2"/>
          <ul class="d-flex list-unstyled mt-auto">
            <li class="me-auto">
              <h3>75$</h3>
            </li>
            <li class="d-flex align-items-center">
              <button on:click={add} type="button" class="btn btn-light" style="text-decoration: none">Добавить</button>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <div class="col">
      <div class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow-lg" style="background-image: linear-gradient(rgba(255, 255, 255, 0), rgba(0, 0, 0, 0.6)), url('http://www.gidizrail.ru/images/stories3/1000sheqalim-1983.jpg'); background-size: cover;">
        <div class="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1">
          <h2 class="pt-5 mt-5 mb-2 display-6 lh-1 fw-bold">1000 шекелей</h2>
          <input type="hidden" value="3"/>
          <ul class="d-flex list-unstyled mt-auto">
            <li class="me-auto">
              <h3>10$</h3>
            </li>
            <li class="d-flex align-items-center">
              <button on:click={add} type="button" class="btn btn-light" style="text-decoration: none">Добавить</button>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  {#if (elements.length >= 1)}
    <div class="text-center">
      <a href="{generate_link()}">
        <button class="btn btn-link text-center" style="text-decoration: none">Перейти к оплате</button>
      </a>
    </div>
  {/if}
</div>

