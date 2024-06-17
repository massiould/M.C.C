<template>
  <header class="header">
    <div class="container">
      <h1 class="logo">MesChersConfrères</h1>
      <nav>
        <ul>
          <li><a href="#">Veille juridique</a></li>
          <li><a href="#">Postulation</a></li>
          <li><a href="#">Question Pratique</a></li>
          <li><a href="#">Question</a></li>
          <li><a href="#" class="btn">Mon Compte</a></li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<style scoped>
.header {
  background: #fff;
  border-bottom: 1px solid #ccc;
}
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
}
.logo {
  font-size: 24px;
  color: #007bff;
}
nav ul {
  list-style: none;
  display: flex;
  gap: 20px;
}
nav ul li a {
  text-decoration: none;
  color: #333;
}
nav ul li a.btn {
  background: #007bff;
  color: #fff;
  padding: 5px 10px;
  border-radius: 4px;
}
</style>
