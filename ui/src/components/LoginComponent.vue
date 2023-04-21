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
      <input type="text" placeholder="password" class="input input-bordered" v-model="password" />
    </div>
    <div class="flex">
      <button class="btn btn-primary mt-4" @click="submitLoginForm">Sign In</button>
    </div>
    <p class="mt-4">
      {{ message }}
    </p>
  </form>
</template>

<script setup>
import { baseUrl } from "/src/main.js";
import { ref } from "vue";
import axios from "axios";
import bcrypt from "bcryptjs";

const email = ref("sgoggins@mail.com");
const password = ref("securepasswordforprof");
const message = ref("");

function submitLoginForm() {
  axios.post(baseUrl + "login", { email: email.value }).then((response) => {
    const hashedPassword = bcrypt.hashSync(password.value, response.data.salt);
    if (hashedPassword == response.data.password) {
      message.value = "Password correct.";
    } else {
      message.value = "Password incorrect.";
    }
  });
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
