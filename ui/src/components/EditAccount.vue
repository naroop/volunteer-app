<template>
  <form class="w-full max-w-lg bg-base-300 p-4 shadow-lg rounded border-accent" @submit.prevent>
    <h3 class="text-center text-2xl">Edit Account</h3>
    <div class="divider mb-0 mt-1"></div>

    <div class="flex justify-evenly">
      <div :class="['form-control']">
        <label class="label">
          <span :class="['label-text', form.firstName.hasError ? 'text-error' : '']">First Name</span>
        </label>
        <input
          type="text"
          required
          :class="['input', 'input-bordered', form.firstName.hasError ? 'input-error' : '']"
          v-model="form.firstName.data"
        />
        <label class="label">
          <span :class="['label-text-alt', form.firstName.hasError ? 'text-error' : '']">{{ form.firstName.label }}</span>
        </label>
      </div>

      <div class="form-control">
        <label class="label">
          <span :class="['label-text', form.lastName.hasError ? 'text-error' : '']">Last Name</span>
        </label>
        <input type="text" required :class="['input', 'input-bordered', form.lastName.hasError ? 'input-error' : '']" v-model="form.lastName.data" />
        <label class="label">
          <span :class="['label-text-alt', form.lastName.hasError ? 'text-error' : '']">{{ form.lastName.label }}</span>
        </label>
      </div>
    </div>

    <div class="flex justify-evenly">
      <div :class="['form-control']">
        <label class="label">
          <span :class="['label-text', form.cellPhone.hasError ? 'text-error' : '']">Phone</span>
        </label>
        <input
          type="text"
          required
          :class="['input', 'input-bordered', form.cellPhone.hasError ? 'input-error' : '']"
          v-model="form.cellPhone.data"
        />
        <label class="label">
          <span :class="['label-text-alt', form.cellPhone.hasError ? 'text-error' : '']">{{ form.cellPhone.label }}</span>
        </label>
      </div>

      <div class="form-control">
        <label class="label">
          <span :class="['label-text', form.hoursPerMonth.hasError ? 'text-error' : '']">Hours Available per Month</span>
        </label>
        <input
          type="number"
          :class="['input', 'input-bordered', form.hoursPerMonth.hasError ? 'input-error' : '']"
          required
          v-model="form.hoursPerMonth.data"
          @input="if (form.hoursPerMonth.data < 0) form.hoursPerMonth.data = 0;"
        />
        <label class="label">
          <span :class="['label-text-alt', form.hoursPerMonth.hasError ? 'text-error' : '']">{{ form.hoursPerMonth.label }}</span>
        </label>
      </div>
    </div>

    <div :class="['form-control']">
      <label class="label">
        <span :class="['label-text', form.address.hasError ? 'text-error' : '']">Address</span>
      </label>
      <input type="text" required :class="['input', 'input-bordered', form.address.hasError ? 'input-error' : '']" v-model="form.address.data" />
      <label class="label">
        <span :class="['label-text-alt', form.address.hasError ? 'text-error' : '']">{{ form.address.label }}</span>
      </label>
    </div>

    <div class="flex items-center justify-between">
      <button class="btn btn-primary mt-4" @click="submitEditAccount">Save</button>
      <img src="@/assets/ducksLogo.svg.png" alt="Avatar" class="object-contain h-20 mt-4 mr-1" />
    </div>

    <p :class="form.general.label.length ? 'mt-4 text-error' : ''">
      {{ form.general.label }}
    </p>
  </form>
</template>

<script setup>
import { baseUrl } from "/src/main.js";
import { reactive, onMounted } from "vue";
import axios from "axios";
// import bcrypt from "bcryptjs";
import store from "@/store/index";
import router from "@/router/index";

const form = reactive({
  firstName: {
    data: "",
    label: "",
    hasError: false,
  },
  lastName: {
    data: "",
    label: "",
    hasError: false,
  },
  hoursPerMonth: {
    data: "",
    label: "",
    hasError: false,
  },
  cellPhone: {
    data: "",
    label: "",
    hasError: false,
  },
  address: {
    data: "",
    label: "",
    hasError: false,
  },
  general: {
    data: ":)",
    label: "",
    hasError: false,
  },
});

onMounted(async () => {
  axios.get(baseUrl + "getUserDetails/" + String(store.getters.emailAddress)).then((response) => {
    if (response.data.error) {
      console.log("Error occurred.");
    } else {
      form.firstName.data = response.data.userDetails.firstName;
      form.lastName.data = response.data.userDetails.lastName;
      form.cellPhone.data = response.data.userDetails.cellPhone;
      form.hoursPerMonth.data = response.data.userDetails.hoursPerMonth;
      form.address.data = response.data.userDetails.address;
    }
  });
});

function resetform() {
  for (let field in form) {
    form[field].label = "";
    form[field].hasError = false;
  }
}

function validateForm() {
  for (let field in form) {
    if (String(form[field].data).trim() === "") {
      form[field].hasError = true;
      form[field].label = "Please enter a valid input";
      return true;
    }
  }
}

function submitEditAccount() {
  resetform();
  if (validateForm()) return;
  axios
    .patch(baseUrl + "updateAccount", {
      emailAddress: store.getters.emailAddress,
      firstName: form.firstName.data,
      lastName: form.lastName.data,
      cellPhone: form.cellPhone.data,
      hoursPerMonth: form.hoursPerMonth.data,
      address: form.address.data,
    })
    .then((response) => {
      if (response.data.error) {
        form.general.hasError = true;
        form.general.label = response.data.message;
      } else {
        router.push("/");
      }
    })
    .catch((error) => {
      console.log(error);
    });
}
</script>
