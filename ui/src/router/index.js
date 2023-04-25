import { createRouter, createWebHistory } from "vue-router";
import LoginView from "../views/LoginView.vue";
import HomeView from "../views/HomeView.vue";
import CreateAccountView from "../views/CreateAccountView.vue";
import EditAccountView from "../views/EditAccountView.vue";
import store from "@/store/index";

const routes = [
  {
    path: "/",
    component: HomeView,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/login",
    component: LoginView,
  },
  {
    path: "/createAccount",
    component: CreateAccountView,
  },
  {
    path: "/editAccount",
    component: EditAccountView,
    meta: {
      requiresAuth: true,
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  const isLoggedIn = store.getters.isLoggedIn;
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!isLoggedIn) {
      next("/login");
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
