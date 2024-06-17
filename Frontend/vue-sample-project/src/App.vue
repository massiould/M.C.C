<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
  <!-- <LoginView/> -->
  <RouterView /> 
  <div id="app">

  </div>
</template>

<script>

import Header from './components/Layout/Header/Header.vue';
import Footer from './components/Layout/Footer/Footer.vue';

export default {
  name: 'App',
  components: {
    //HelloWorld,
    // LoginView
    Header,
    Footer

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
