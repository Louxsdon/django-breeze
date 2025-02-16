import { createInertiaApp } from "@inertiajs/react";
import { createRoot } from "react-dom/client";
import "vite/modulepreload-polyfill";
import "./index.css";

const pages = import.meta.glob("./pages/**/*.jsx");

document.addEventListener("DOMContentLoaded", () => {
  createInertiaApp({
    resolve: async (name) => {
      const page = (await pages[`./pages/${name}.jsx`]()).default;
      page.layout = page.layout;
      return page;
    },
    setup({ el, App, props }) {
      createRoot(el).render(<App {...props} />);
    },
  });
});
