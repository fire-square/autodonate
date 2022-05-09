import Hero from '../ui/Hero.svelte';

const app = new Hero({
    target: document.getElementById("hero-target"),
    props: JSON.parse(document.getElementById("hero-props").textContent),
});

export default app;
