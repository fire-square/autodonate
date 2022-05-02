import Admin from '../pages/Admin.svelte';

const app = new Admin({
    target: document.getElementById("admin-target"),
    props: JSON.parse(document.getElementById("admin-props").textContent),
});

export default app;
