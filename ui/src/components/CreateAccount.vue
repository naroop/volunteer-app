<template>
  <!-- Temporarily commented --
  <form class="w-full max-w-xs bg-base-200 p-4 shadow-md rounded" @submit.prevent>
    <h3 class="text-2xl">Create Account</h3>
-->
  <form @submit.prevent>
    <div class="container">
      <label for="email" style="font-size: 20px"><b>Email Address</b></label>
      <input type="text" placeholder="Enter email address:" name="email" v-model="emailAddress" required />

      <label for="psw" style="font-size: 20px"><b>Password</b></label>
      <input type="password" placeholder="Enter password:" name="psw" v-model="password" required />

      <label for="fname" style="font-size: 20px"><b>First Name</b></label>
      <input type="text" placeholder="Enter first name:" name="fname" v-model="firstName" required />

      <label for="lname" style="font-size: 20px"><b>Last Name</b></label>
      <input type="text" placeholder="Enter last name:" name="lname" v-model="lastName" required />

      <label for="cell" style="font-size: 20px"><b>Phone Number</b></label>
      <input type="text" placeholder="Enter phone number:" name="cell" v-model="cellPhone" required />

      <label for="hours" style="font-size: 20px"><b>Hours available to work</b></label>
      <input type="text" placeholder="Enter hours:" name="hours" v-model="hoursPerMonth" required />

      <label for="address" style="font-size: 20px"><b>Address</b></label>
      <input type="text" placeholder="Enter address:" name="address" v-model="address" required />

      <button @click="submitCreateAccount">Create Account</button>
    </div>

    <div class="container">
      <img src="@/assets/ducksLogo.svg.png" alt="Avatar" class="avatar" />
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

const emailAddress = ref("");
const password = ref("");
const firstName = ref("");
const lastName = ref("");
const cellPhone = ref("");
const hoursPerMonth = ref("");
const address = ref("");

function submitCreateAccount() {
  const passwordInfo = encryptPassword();
  axios
    .post(baseUrl + "createAccount", {
      emailAddress: emailAddress.value,
      firstName: firstName.value,
      lastName: lastName.value,
      cellPhone: cellPhone.value,
      hoursPerMonth: hoursPerMonth.value,
      address: address.value,
      passwordInfo,
    })
    .then((response) => {
      console.log(response);
      if (response.data.status == "OK") {
        store.commit("login");
        router.push("/");
      } else {
        console.log("Something went wrong");
      }
    })
    .catch((error) => {
      console.log(error);
    });
}

function encryptPassword() {
  const saltRounds = Math.floor(Math.random() * 10) + 1; // generate a random number of salt rounds between 1 and 10
  const salt = bcrypt.genSaltSync(saltRounds); // generate a salt using the specified number of rounds
  const hash = bcrypt.hashSync(password.value, salt); // hash the password using the generated salt

  return { password: hash, salt: salt };
}
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
