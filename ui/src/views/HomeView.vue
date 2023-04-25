<template>
  <div class="flex flex-col h-screen items-center justify-center">
    <h1 class="text-2xl mb-3">Welcome!</h1>
    <button class="btn btn-primary" @click.prevent="$router.push('/editAccount')">Edit Account</button>
    <button class="btn btn-secondary mt-3" @click="logout">Sign Out</button>
  </div>
</template>

<script setup>
import store from "@/store/index";
import router from "@/router/index";

function logout() {
  store.commit("logout");
  router.push("/login");
}
</script>
