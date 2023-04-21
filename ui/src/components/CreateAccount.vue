<template>

<!-- Temporarily commented --
  <form class="w-full max-w-xs bg-base-200 p-4 shadow-md rounded" @submit.prevent>
    <h3 class="text-2xl">Create Account</h3>
-->
  <form action="/action_page.php" method="post">
    <div class="container">
      <label for="fname" style="font-size: 20px"><b>First Name</b></label>
      <input type="text" placeholder="Enter first name:" name="fname" required />

      <label for="lname" style="font-size: 20px"><b>Last Name</b></label>
      <input type="text" placeholder="Enter last name:" name="lname" required />

      <label for="email" style="font-size: 20px"><b>Email Address</b></label>
      <input type="text" placeholder="Enter email address:" name="email" required />

      <label for="cell" style="font-size: 20px"><b>Phone Number</b></label>
      <input type="text" placeholder="Enter phone number:" name="cell" required />

      <label for="hours" style="font-size: 20px"><b>Hours available to work</b></label>
      <input type="text" placeholder="Enter hours:" name="hours" required />

      <label for="address" style="font-size: 20px"><b>Address</b></label>
      <input type="text" placeholder="Enter address:" name="address" required />

      <!-- Password block
      <label for="psw" style="font-size:20px"><b>Password</b></label>
      <input type="password" placeholder="Enter password:" name="psw" required>
      -->

      <button type="submit">Login</button>
    </div>

    <div class="container">
      <img src="@/assets/ducksLogo.svg.png" alt="Avatar" class="avatar" />
    </div>
  </form>
</template>

<script setup>
import { baseUrl } from "/src/main.js";
import { onMounted, reactive, defineComponent } from "vue";
const axios = require("axios");
const state = reactive({ message: "" });

onMounted(async () => {
  axios.get(baseUrl + "helloworld").then((response) => (state.message = response.data));
});

defineComponent({
  name: "HelloWorld",
  setup() {
    return {
      message: state.message,
    };
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
body {
  font-family: Arial, Helvetica, sans-serif;
  background-color: #c1c6c8;
}
form {
  border: 3px solid #f47a38;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #f47a38;
  box-sizing: border-box;
  font-size: 18px;
}

button {
  background-color: #b9975b;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  font-size: 24px;
}

button:hover {
  opacity: 0.8;
}

img.avatar {
  width: 8%;
  padding-left: auto;
  padding-right: auto;
}

.container {
  padding: 7px;
}

span.psw {
  float: right;
  padding-top: 16px;
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
  span.psw {
    display: block;
    float: none;
  }
}
</style>
