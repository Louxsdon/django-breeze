import { createInertiaApp } from "@inertiajs/react";
import { createRoot } from "react-dom/client";
import "vite/modulepreload-polyfill";
import "./index.css";

const pages = import.meta.glob("./pages/**/*.tsx");

document.addEventListener("DOMContentLoaded", () => {
  createInertiaApp({
    resolve: async (name) => {
      const page = (await pages[`./pages/${name}.tsx`]()).default;
      page.layout = page.layout;
      return page;
    },
    setup({ el, App, props }) {
      createRoot(el).render(<App {...props} />);
    },
  });
});
