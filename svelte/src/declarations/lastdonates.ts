import LastDonates from '../ui/LastDonates.svelte';

const app = new LastDonates({
    target: document.getElementById("lastdonates-target"),
    props: JSON.parse(document.getElementById("lastdonates-props").textContent),
});

export default app;
