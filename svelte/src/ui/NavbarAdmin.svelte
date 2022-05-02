<script lang="ts">
    import { onMount } from 'svelte';

    export let active: string;

    onMount(async () => {
        document.getElementById("nav-"+active).classList.add("active");
        document.getElementById("nav-"+active).classList.remove("text-white");
	});
</script>

<div class="d-flex flex-column flex-shrink-0 p-3 text-white bg-dark" style="width: 280px; height: 100%;">
  <a href="/admin/" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-white text-decoration-none ms-2">
    <i class="bi bi-gear-wide pe-1"></i>
    <span class="fs-4">Admin</span>
  </a>
  <hr>
  <ul class="nav nav-pills flex-column mb-auto">
    <li class="nav-item">
      <a href="/admin/" class="nav-link text-white" id="nav-index">
        <i class="bi bi-app pe-1"></i>
        Home
      </a>
    </li>
    <li>
      <a href="/admin/pages/" class="nav-link text-white" id="nav-pages">
        <i class="bi bi-book pe-1"></i>
        Pages
      </a>
    </li>
  </ul>
</div>