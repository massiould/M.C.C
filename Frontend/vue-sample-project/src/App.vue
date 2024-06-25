<template>
  <div id="app" class="app-container">
    <Header />
    <router-view />
    
  </div>
</template>

<script>
import Header from './components/Layout/Header.vue';
import Footer from './components/Layout/Footer.vue';

export default {
  name: 'App',
  components: {
    Header,
    
  }
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  margin: 0;
  padding: 0;
}

.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

router-view {
  flex: 1;
}

.footer {
  background: #333;
  color: #fff;
  padding: 20px 0;
  text-align: center;
}
</style>
