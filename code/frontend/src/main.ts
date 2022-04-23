import { createApp } from "vue";
import { createPinia } from "pinia";
import { library, dom } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";
import GAuth from "vue3-google-oauth2";

import App from "./App.vue";
import "./index.css";
import router from "./router";

library.add(fas, far, fab);
dom.watch();

const app = createApp(App);
// const client_id = "placeholder";
// const client_id = import.meta.env.VITE_GOOGLE_CLIENT_ID;

const gAuthOptions = {
  clientId: import.meta.env.VITE_GOOGLE_CLIENT_ID,
  scope: "email",
  prompt: "consent",
  // TODO: set to false once we get data from backend
  fetch_basic_profile: true,
};

app.component("font-awesome-icon", FontAwesomeIcon);
app.use(createPinia());
app.use(router);
app.use(GAuth, gAuthOptions);

app.mount("#app");
