<template>
  <form class="w-full max-w-xs bg-base-200 p-4 shadow-md rounded" @submit.prevent>
    <h3 class="text-2xl">Login</h3>
    <div class="form-control">
      <label class="label">
        <span class="label-text">Email</span>
      </label>
      <input type="text" placeholder="name@site.com" class="input input-bordered" v-model="email" />
    </div>
    <div class="form-control">
      <label class="label">
        <span class="label-text">Password</span>
      </label>
      <input type="password" placeholder="•••••••••" class="input input-bordered input-" v-model="password" />
    </div>
    <div class="flex items-center mt-4 justify-between">
      <button class="btn btn-primary" @click="submitLoginForm">Sign In</button>
      <a class="mr-4 link link-hover" @click.prevent="$router.push('/createAccount')">Create an Account</a>
    </div>
  </form>
</template>

<script setup>
import { baseUrl } from "/src/main.js";
import { ref } from "vue";
import axios from "axios";
import bcrypt from "bcryptjs";
import store from "@/store/index";
import router from "@/router/index";

const email = ref("sgoggins@mail.com");
const password = ref("securepasswordforprof");

function submitLoginForm() {
  axios.post(baseUrl + "login", { email: email.value }).then((response) => {
    const hashedPassword = bcrypt.hashSync(password.value, response.data.salt);
    if (hashedPassword == response.data.password) {
      store.commit("login");
      router.push("/");
    }
  });
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
