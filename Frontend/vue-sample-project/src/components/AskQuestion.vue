<template>
    <div>
      <h2>Posez une Question</h2>
      <form @submit.prevent="askQuestion">
        <div>
          <label for="title">Titre:</label>
          <input type="text" v-model="form.title" required />
        </div>
        <div>
          <label for="content">Contenu:</label>
          <textarea v-model="form.content" required></textarea>
        </div>
        <button type="submit">Poser la Question</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'AskQuestion',
    data() {
      return {
        form: {
          title: '',
          content: ''
        }
      };
    },
    methods: {
      async askQuestion() {
        try {
          await axios.post('http://localhost:8000/api/ask-question/', this.form);
          this.$router.push('/');
        } catch (error) {
          console.error('Error asking question:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  form {
    max-width: 500px;
    margin: 0 auto;
  }
  div {
    margin-bottom: 10px;
  }
  </style>
  