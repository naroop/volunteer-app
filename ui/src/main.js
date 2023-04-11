import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

export const baseUrl =
  process.env.NODE_ENV === "production"
    ? "http://18.218.117.37:8000/"
    : "http://127.0.0.1:8000/";

createApp(App).use(router).mount("#app");
