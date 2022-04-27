<script>
  import static_path from '../api/static';
  import { is_authorized } from '../api/auth';

  export let burger
  export let menu
  function open(event) {
    for (let item of document.getElementsByClassName("nav-link"))
      item.classList.remove("active");
    event.target.classList.add("active");
  }
</script>

<header id="top">
  <div class="px-3 pb-3 text-white">
    <div class="container d-flex justify-content-center py-3">
      <ul class="nav nav-pills gap-1">
        <li class="nav-item"><a href="/#top" class="nav-link active" on:click={open}>Главная</a></li>
        <li class="nav-item"><a href="/#donate" class="nav-link" on:click={open}>Донат</a></li>
        <li class="nav-item"><a href="/#about" class="nav-link" on:click={open}>О сервере</a></li>
      </ul>
    </div>
  </div>
</header>
