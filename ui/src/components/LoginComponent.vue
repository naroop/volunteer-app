<template>
  <form class="w-full max-w-xs bg-base-300 p-4 shadow-md rounded" @submit.prevent>
    <h3 class="text-2xl">Login</h3>

    <div :class="['form-control', validation.emailAddress.hasError ? 'input-error' : '']">
      <label class="label">
        <span :class="['label-text', validation.emailAddress.hasError ? 'text-error' : '']">Email</span>
      </label>
      <input type="text" :class="['input', 'input-bordered', validation.emailAddress.hasError ? 'input-error' : '']" v-model="email" />
      <label class="label">
        <span :class="['label-text-alt', validation.emailAddress.hasError ? 'text-error' : '']">{{ validation.emailAddress.label }}</span>
      </label>
    </div>

    <div :class="['form-control']">
      <label class="label">
        <span :class="['label-text', validation.password.hasError ? 'text-error' : '']">Password</span>
      </label>
      <input type="password" :class="['input', 'input-bordered', validation.password.hasError ? 'input-error' : '']" v-model="password" />
      <label class="label">
        <span :class="['label-text-alt', validation.password.hasError ? 'text-error' : '']">{{ validation.password.label }}</span>
      </label>
    </div>

    <div class="flex items-center mt-4 justify-between">
      <button id="btnSubmitLogin" :class="['btn btn-primary', btnSubmitLoginLoading ? 'loading' : '']" @click="submitLoginForm">Sign In</button>
      <a class="mr-4 link link-hover" @click.prevent="$router.push('/createAccount')">Create an Account</a>
    </div>

    <p :class="validation.general.label.length ? 'mt-4 text-error' : ''">
      {{ validation.general.label }}
    </p>
  </form>
</template>

<script setup>
import { baseUrl } from "/src/main.js";
import { ref, reactive } from "vue";
import axios from "axios";
import bcrypt from "bcryptjs";
import store from "@/store/index";
import router from "@/router/index";

const email = ref("");
const password = ref("");
const btnSubmitLoginLoading = ref(false);

const validation = reactive({
  emailAddress: {
    label: "",
    hasError: false,
  },
  password: {
    label: "",
    hasError: false,
  },
  general: {
    label: "",
    hasError: false,
  },
});

function resetValidation() {
  for (let field in validation) {
    validation[field].label = "";
    validation[field].hasError = false;
  }
}

function submitLoginForm() {
  resetValidation();
  if (email.value.trim() === "") {
    validation.emailAddress.hasError = true;
    validation.emailAddress.label = "Please enter a valid email address.";
    return;
  }

  if (password.value.trim() === "") {
    validation.password.hasError = true;
    validation.password.label = "Please enter a valid password.";
    return;
  }

  btnSubmitLoginLoading.value = true;
  axios.post(baseUrl + "login", { emailAddress: email.value }).then((response) => {
    if (response.data.error) {
      btnSubmitLoginLoading.value = false;
      validation.general.label = response.data.message;
      return;
    }
    const hashedPassword = bcrypt.hashSync(password.value, response.data.salt);
    if (hashedPassword == response.data.password) {
      store.commit("login", email.value);
      router.push("/");
    } else {
      btnSubmitLoginLoading.value = false;
      validation.general.label = "Password incorrect.";
    }
  });
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
