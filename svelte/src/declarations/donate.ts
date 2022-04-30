import Hero from '../ui/Donate.svelte';

const app = new Hero({
    target: document.getElementById("donate-target"),
    props: JSON.parse(document.getElementById("donate-props").textContent),
});

export default app;
