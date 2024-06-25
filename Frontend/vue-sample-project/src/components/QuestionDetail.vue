<template>
    <div>
      <h2>{{ question.title }}</h2>
      <p>{{ question.content }}</p>
      <h3>Réponses</h3>
      <ul>
        <li v-for="answer in answers" :key="answer.id">{{ answer.content }}</li>
      </ul>
      <AnswerForm :questionId="question.id" @answered="fetchAnswers" />
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import AnswerForm from './AnswerForm.vue';
  
  export default {
    name: 'QuestionDetail',
    components: {
      AnswerForm
    },
    data() {
      return {
        question: {},
        answers: []
      };
    },
    created() {
      this.fetchQuestion();
      this.fetchAnswers();
    },
    methods: {
      async fetchQuestion() {
        try {
          const response = await axios.get(`http://localhost:8000/api/questions/${this.$route.params.questionId}/`);
          this.question = response.data;
        } catch (error) {
          console.error('Error fetching question:', error);
        }
      },
      async fetchAnswers() {
        try {
          const response = await axios.get(`http://localhost:8000/api/answers/${this.$route.params.questionId}/`);
          this.answers = response.data;
        } catch (error) {
          console.error('Error fetching answers:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  ul {
    list-style: none;
    padding: 0;
  }
  li {
    margin-bottom: 10px;
  }
  </style>
  