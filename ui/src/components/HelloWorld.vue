<template>
  <h1>{{ state.message }}</h1>
</template>

<script setup>
import { baseUrl } from "/src/main.js";
import { onMounted, reactive, defineComponent } from "vue";
const axios = require("axios");
const state = reactive({ message: "" });

onMounted(async () => {
  axios
    .get(baseUrl + "helloworld")
    .then((response) => (state.message = response.data));
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
<style scoped></style>
