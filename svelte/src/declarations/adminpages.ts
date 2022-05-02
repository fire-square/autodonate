import Admin from '../pages/AdminPages.svelte';

const app = new Admin({
    target: document.getElementById("adminpages-target"),
    props: JSON.parse(document.getElementById("adminpages-props").textContent),
});

export default app;
