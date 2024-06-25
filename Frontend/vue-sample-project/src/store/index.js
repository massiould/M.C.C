import { createStore } from 'vuex';

export default createStore({
  state: {
    isAuthenticated: false,
    username: ''
  },
  mutations: {
    SET_AUTHENTICATION(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated;
    },
    SET_USERNAME(state, username) {
      state.username = username;
    }
  },
  getters: {
    isAuthenticated: state => state.isAuthenticated,
    username: state => state.username
  },
  actions: {
    login({ commit }, user) {
      commit('SET_AUTHENTICATION', true);
      commit('SET_USERNAME', user.username);
    },
    logout({ commit }) {
      commit('SET_AUTHENTICATION', false);
      commit('SET_USERNAME', '');
    }
  },
  modules: {}
});
