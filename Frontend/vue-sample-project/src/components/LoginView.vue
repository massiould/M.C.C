<template>
  <form name="login-form">
    <div class="mb-3">
      <label for="username">Username: </label>
      <input type="text" id="username" v-model="input.username" />
    </div>
    <div class="mb-3">
      <label for="password">Password: </label>
      <input type="password" id="password" v-model="input.password" />
    </div>
    <button class="btn btn-outline-dark" type="submit" v-on:click.prevent="login">
      Login
    </button>
  </form>
  <h3>Output: {{ output }}</h3>
</template>

<script>
import axios from 'axios';
import { SET_AUTHENTICATION, SET_USERNAME } from "../store/storeconstants";

export default {
  name: 'LoginView',
  data() {
    return {
      input: {
        username: "",
        password: ""
      },
      output: "",
    }
  },
  
  methods: {
    async login() {
      try {
        console.log("massi*******************************************************************")
        const response = await axios.post('http://localhost:8000/api/login/', {
          username: this.input.username,
          password: this.input.password
        });
        console.log(response)
        console.log("massi*******************************************************************")
        if (response.status === 200) {
          this.output = response.data.message;
          this.$store.commit(`auth/${SET_AUTHENTICATION}`, true);
          this.$store.commit(`auth/${SET_USERNAME}`, this.input.username);
          this.$router.push('/home');
        }
      } catch (error) {
        this.output = error.response.data.message || 'Error during authentication';
        this.$store.commit(`auth/${SET_AUTHENTICATION}`, false);
      }
    },
  },
}
</script>

<style scoped>
/* Style for form container *//* Style for form container */
.form-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #fff;
  box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
}

/* Style for form labels */
label {
  display: block;
  margin-bottom: 5px;
  color: #333;
  text-align: left;
  font-size: 16px;
  font-weight: 500;
}

/* Style for form inputs */
input[type="text"],
input[type="password"] {
  width: calc(100% - 20px);
  padding: 12px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 3px;
}

/* Style for submit button */
button[type="submit"] {
  width: 100%;
  padding: 12px;
  border: none;
  border-radius: 3px;
  background-color: #0073b1; /* LinkedIn Blue */
  color: #fff;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s ease;
  font-size: 14px;
}

button[type="submit"]:hover {
  background-color: #005a8d; /* Darker Blue */
}

/* Style for output message */
.output-message {
  margin-top: 10px;
  font-weight: bold;
  color: #333;
}
</style>