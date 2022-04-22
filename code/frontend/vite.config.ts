import { fileURLToPath, URL } from "url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueJsx from "@vitejs/plugin-vue-jsx";
// import EnvironmentPlugin from "vite-plugin-environment";
// import path from "path";
// import ImportMetaEnvPlugin from "@import-meta-env/unplugin";

const viteEnv = {};
Object.keys(process.env).forEach((key) => {
  if (key.startsWith(`VITE_`)) {
    viteEnv[`import.meta.env.${key}`] = process.env[key];
  }
});

// https://vitejs.dev/config/
export default defineConfig({
  define: viteEnv,
  plugins: [
    vue(),
    vueJsx(),
    // EnvironmentPlugin("all"),
    // ImportMetaEnvPlugin.vite({
    //   example: ".env.local",
    // }),
  ],
  resolve: {
    alias: {
      "@": require("path").resolve(__dirname, "src"),
    },
  },
});
