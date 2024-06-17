<template>
    <div>
      <form @submit.prevent="signup">
        <div class="mb-3">
          <label for="username">Username: </label>
          <input type="text" id="username" v-model="input.username" />
        </div>
        <div class="mb-3">
          <label for="email">Email: </label>
          <input type="email" id="email" v-model="input.email" />
        </div>
        <div class="mb-3">
          <label for="password">Password: </label>
          <input type="password" id="password" v-model="input.password" />
        </div>
        <button class="btn btn-outline-dark" type="submit">
          Sign Up
        </button>
      </form>
      <h3>Output: {{ output }}</h3>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Signup',
    data() {
      return {
        input: {
          username: '',
          email: '',
          password: ''
        },
        output: ''
      }
    },
    methods: {
      async signup() {
        try {
          const response = await axios.post('http://localhost:8000/api/signup/', {
            username: this.input.username,
            email: this.input.email,
            password: this.input.password
          });
          if (response.status === 201) {
            this.output = response.data.message;
            this.$router.push('/login');
          }
        } catch (error) {
          if (error.response) {
            this.output = error.response.data.message;
          } else {
            this.output = 'An error occurred';
          }
        }
      }
    }
  }
  </script>
  <style scoped>
  .signup-container {
    max-width: 400px;
    margin: 50px auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  .signup-form {
    display: flex;
    flex-direction: column;
  }
  
  .signup-form h2 {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .signup-form .mb-3 {
    margin-bottom: 15px;
  }
  
  .signup-form label {
    margin-bottom: 5px;
    font-weight: bold;
  }
  
  .signup-form input {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
    border: 1px solid #ddd;
    border-radius: 4px;
  }
  
  .signup-form .btn {
    padding: 10px 15px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    text-align: center;
  }
  
  .signup-form .btn:hover {
    background-color: #0056b3;
  }
  
  .signup-form .output {
    margin-top: 20px;
    text-align: center;
    font-weight: bold;
  }
  </style>