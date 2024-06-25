<template>
    <div>
      <h2>Questions</h2>
      <ul>
        <li v-for="question in questions" :key="question.id">
          <router-link :to="{ name: 'QuestionDetail', params: { questionId: question.id }}">{{ question.title }}</router-link>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'QuestionList',
    data() {
      return {
        questions: []
      };
    },
    created() {
      this.fetchQuestions();
    },
    methods: {
      async fetchQuestions() {
        try {
          const response = await axios.get('http://localhost:8000/api/questions/');
          this.questions = response.data;
        } catch (error) {
          console.error('Error fetching questions:', error);
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
  