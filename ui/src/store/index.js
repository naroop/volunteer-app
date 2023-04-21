import { createStore } from "vuex";

export default createStore({
  state: {
    isLoggedIn: false,
  },
  getters: {
    isLoggedIn: (state) => state.isLoggedIn,
  },
  mutations: {
    login(state) {
      state.isLoggedIn = true;
    },
    logout(state) {
      state.isLoggedIn = false;
    },
  },
  modules: {},
});
