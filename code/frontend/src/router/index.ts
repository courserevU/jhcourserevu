import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import WriteView from "@/views/WriteView.vue";
import ReadView from "@/views/ReadView.vue";
import PageNotFound from "@/views/PageNotFound.vue";
import LoginView from "@/views/LoginView.vue";
import RegisterView from "@/views/RegisterView.vue";
import CourseView from "@/views/CourseView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/course-search",
      name: "CourseSearch",
      component: CourseView,
    },
    {
      path: "/write/:course",
      name: "write",

      component: WriteView,
    },
    {
      path: "/read/:course",
      name: "read",
      component: ReadView,
    },
    {
      path: "/register",
      name: "register",
      component: RegisterView,
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/:catchAll(.*)*",
      name: "PageNotFound",
      component: PageNotFound,
    },
  ],
});

export default router;
