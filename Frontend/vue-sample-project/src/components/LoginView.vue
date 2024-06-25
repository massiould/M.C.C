<template>
  <div class="login">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div>
        <label for="username">Username:</label>
        <input type="text" v-model="form.username" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" v-model="form.password" required />
      </div>
      <button type="submit">Login</button>
    </form>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        username: '',
        password: ''
      },
      error: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://localhost:8000/api/login/', this.form);
        if (response.status === 200) {
          this.$store.dispatch('login', { username: this.form.username });
          this.$router.push(this.$route.query.redirect || '/home');
        }
      } catch (error) {
        this.error = error.response.data.message || 'An error occurred during login';
      }
    }
  }
};
</script>

<style scoped>
.login {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background: white;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.login h2 {
  margin-bottom: 20px;
}

.login form div {
  margin-bottom: 10px;
}

.login form label {
  display: block;
  margin-bottom: 5px;
}

.login form input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}

.login button {
  padding: 10px 15px;
  background: #333;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.login p {
  color: red;
}
</style>
