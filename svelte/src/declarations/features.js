import Hero from '../ui/Features.svelte';

const app = new Hero({
	target: document.getElementById("features-target"),
	props: JSON.parse(document.getElementById("features-props").textContent),
});

export default app;
