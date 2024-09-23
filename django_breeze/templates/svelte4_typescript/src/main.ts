import { createInertiaApp } from "@inertiajs/svelte";
import "./index.css";

createInertiaApp({
  resolve: (name) => {
    const pages = import.meta.glob("./pages/**/*.svelte", { eager: true });
    return pages[`./pages/${name}.svelte`];
  },
  setup({ el, App, props }) {
    new App({ target: el, props });
  },
});

