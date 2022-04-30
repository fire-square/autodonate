import Navbar from '../ui/Navbar.svelte';

const app = new Navbar({
    target: document.getElementById("navbar-target"),
    props: JSON.parse(document.getElementById("navbar-props").textContent),
});

export default app;
