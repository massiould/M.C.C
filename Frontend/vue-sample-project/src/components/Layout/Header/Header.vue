<template>
    <header>
      <nav>
        <ul>
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/login">Login</router-link></li>
          
        </ul>
      </nav>
    </header>
  </template>
  
  <script>
  export default {
    name: 'Header'
  }
  </script>
  
  <style scoped>
  /* Ajoutez du style pour le header si nécessaire */
  header {
    background-color: #333;
    color: white;
    padding: 10px 0;
  }
  nav ul {
    list-style: none;
    display: flex;
    justify-content: space-around;
  }
  nav ul li {
    display: inline;
  }
  nav ul li a {
    color: white;
    text-decoration: none;
  }
  </style>