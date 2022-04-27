<script>
  import static_path from '../api/static';
  import { is_authorized } from '../api/auth';

  export let burger
  export let menu
  function open() {
    burger.classList.toggle("is-active")
    menu.classList.toggle("is-active")
  }
</script>

<nav class="navbar" aria-label="main navigation">
  <div class="navbar-brand">
    <a class="navbar-item" href="/">
      <img src="{static_path('logo.png')}" style="border-radius: 9999px;" width="28" height="28" alt="logo">
    </a>

    <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" on:click={open} bind:this={burger}>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>

  <div class="navbar-menu" bind:this={menu}>
    <div class="navbar-start">
      <a class="navbar-item" href="/">
        Главная
      </a>

      <a class="navbar-item" href="/#donate">
        Донат
      </a>

      <a class="navbar-item" href="/#about">
        О сервере
      </a>
    </div>

    <div class="navbar-end">
      <div class="navbar-item">
        <div class="buttons">
          {#if (is_authorized())}
            <a class="button is-light" href="/profile/">
              Личный кабинет
            </a>
          {:else}
            <a class="button is-primary" href="/auth/">
              <strong>Войти</strong>
            </a>
          {/if}
        </div>
      </div>
    </div>
  </div>
</nav>
