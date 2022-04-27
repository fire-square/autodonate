<script>
  let elements = [];

  function add(event) {
    event.target.innerText = "Добавлено";
    event.target.classList.add("btn-success");
    event.target.classList.remove("btn-light");
    let list = elements;
    list.push(event.target.parentElement.parentElement.parentElement.getElementsByClassName("fw-bold")[0].innerText);
    elements = list;
    console.log(event.target.parentElement.parentElement.parentElement.getElementsByClassName("fw-bold")[0].innerText);
    console.log(list);
  }
</script>

<div class="overflow-hidden px-2 pt-4" id="donate">
  <h2 class="fw-bold text-center pb-3 pt-5">Донат</h2>
  <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 align-items-stretch g-4 py-5">
    <div class="col">
      <div class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow" style="background-image: linear-gradient(rgba(255, 255, 255, 0), rgba(0, 0, 0, 0.6)), url('https://minecraftom.ru/uploads/posts/2021-06/1622893537_2019-09-06-14-1.png'); background-size: cover;">
        <div class="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1">
          <h2 class="pt-5 mt-5 mb-2 display-6 lh-1 fw-bold">Флай</h2>
          <ul class="d-flex list-unstyled mt-auto">
            <li class="me-auto">
              <h3>25$</h3>
            </li>
            <li class="d-flex align-items-center">
              <button on:click={add} type="button" class="btn btn-light" style="text-decoration: none"><i class="bi bi-bag-plus"></i> Добавить</button>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <div class="col">
      <div class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow-lg" style="background-image: linear-gradient(rgba(255, 255, 255, 0), rgba(0, 0, 0, 0.6)), url('https://creativus.do.am/mine/gorod/6xnUtKX_6388316_lrg.jpg'); background-size: cover;">
        <div class="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1">
          <h2 class="pt-5 mt-5 mb-2 display-6 lh-1 fw-bold">Креатив</h2>
          <ul class="d-flex list-unstyled mt-auto">
            <li class="me-auto">
              <h3>75$</h3>
            </li>
            <li class="d-flex align-items-center">
              <button on:click={add} type="button" class="btn btn-light" style="text-decoration: none"><i class="bi bi-bag-plus"></i> Добавить</button>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <div class="col">
      <div class="card card-cover h-100 overflow-hidden text-white bg-dark rounded-5 shadow-lg" style="background-image: linear-gradient(rgba(255, 255, 255, 0), rgba(0, 0, 0, 0.6)), url('http://www.gidizrail.ru/images/stories3/1000sheqalim-1983.jpg'); background-size: cover;">
        <div class="d-flex flex-column h-100 p-5 pb-3 text-white text-shadow-1">
          <h2 class="pt-5 mt-5 mb-2 display-6 lh-1 fw-bold">1000 шекелей</h2>
          <ul class="d-flex list-unstyled mt-auto">
            <li class="me-auto">
              <h3>10$</h3>
            </li>
            <li class="d-flex align-items-center">
              <button on:click={add} type="button" class="btn btn-light" style="text-decoration: none"><i class="bi bi-bag-plus"></i> Добавить</button>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>

Вы выбрали:
<ul>
  {#each elements as name, i}
    <li>{name}</li>
  {/each}
</ul>
