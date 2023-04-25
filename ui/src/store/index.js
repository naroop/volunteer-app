import { createStore } from "vuex";

export default createStore({
  state: {
    isLoggedIn: false,
    emailAddress: "",
  },
  getters: {
    isLoggedIn: (state) => state.isLoggedIn,
    emailAddress: (state) => state.emailAddress,
  },
  mutations: {
    login(state, emailAddress) {
      state.isLoggedIn = true;
      state.emailAddress = emailAddress;
    },
    logout(state) {
      state.isLoggedIn = false;
      state.emailAddress = "";
    },
  },
  modules: {},
});
