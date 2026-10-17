
<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <div class="app-container">
    <nav>
      <div class="logo">Christine Lyka Reyes</div>

      <div class="nav-links">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/projects">Projects</RouterLink>
        <RouterLink to="/skills">Skills</RouterLink>
        <RouterLink to="/hobbies">Hobbies</RouterLink>
      </div>
    </nav>

    <main>
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
.app-container {
  min-height: 100vh;
}

nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 20px;
  padding: 20px 8%;
  background-color: #f9fafb;
}

.logo {
  color: #15803d;
  font-size: 18px;
  font-weight: 800;
}

.nav-links {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: flex-end;
  gap: 25px;
}

.nav-links a {
  color: #333;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s ease;
}

.nav-links a:hover,
.nav-links a.router-link-active {
  color: #15803d;
  font-weight: bold;
}

main {
  padding: 0;
}

@media (max-width: 600px) {
  nav {
    flex-direction: column;
    align-items: center;
  }

  .nav-links {
    justify-content: center;
    gap: 15px;
  }
}
</style>
