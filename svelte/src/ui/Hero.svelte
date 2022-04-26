<script>
  export let title;
  export let subtitle;
  export let players;

  setInterval(function () {
    players = Math.floor(Math.random() * 100);
  }, 5000)
</script>

<section class="hero is-large bg">
  <div class="hero-body">
    <div class="container">
      <div class="columns">
        <div class="column">
          <p class="title has-text-white has-text-right">{title}</p>
          <p class="subtitle has-text-white has-text-right">{subtitle}</p>
        </div>
        <div class="column">
          <p class="title has-text-white">Сичас в сити {players} играков</p>
        </div>
      </div>
    </div>
  </div>
</section>

<style>
  .bg {
    background-image: url("https://i.redd.it/l2idgwv1e9n31.jpg");
    background-size: cover;
  }
</style>
