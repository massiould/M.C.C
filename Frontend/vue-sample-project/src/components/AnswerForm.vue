<template>
    <div>
      <h3>Répondre à cette Question</h3>
      <form @submit.prevent="submitAnswer">
        <div>
          <label for="content">Réponse:</label>
          <textarea v-model="form.content" required></textarea>
        </div>
        <button type="submit">Envoyer la Réponse</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'AnswerForm',
    props: {
      questionId: {
        type: Number,
        required: true
      }
    },
    data() {
      return {
        form: {
          content: ''
        }
      };
    },
    methods: {
      async submitAnswer() {
        try {
          await axios.post(`http://localhost:8000/api/create-response/${this.questionId}/`, this.form);
          this.$emit('answered');
        } catch (error) {
          console.error('Error submitting answer:', error);
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
  