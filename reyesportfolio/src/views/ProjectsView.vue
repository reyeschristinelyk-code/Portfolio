<script setup lang="ts">
import { ref, onMounted } from 'vue'

interface Project {
  id: number
  title: string
  description: string
  technologies: string
  project_url: string
  github_url: string
}

const projects = ref<Project[]>([])

onMounted(async () => {
  try {
    const response = await fetch(
        'http://127.0.0.1:8000/api/projects/'
    )

    if (!response.ok) {
      throw new Error('Failed to load projects')
    }

    projects.value = await response.json()
  } catch (error) {
    console.error(error)
  }
})
</script>

<template>
  <section>
    <h1>My Projects</h1>

    <article v-for="project in projects" :key="project.id">
      <h2>{{ project.title }}</h2>
      <p>{{ project.description }}</p>
      <p>Technologies: {{ project.technologies }}</p>

      <a
          v-if="project.project_url"
          :href="project.project_url"
          target="_blank"
          rel="noopener noreferrer"
      >
        View Project
      </a>

      <a
          v-if="project.github_url"
          :href="project.github_url"
          target="_blank"
          rel="noopener noreferrer"
      >
        GitHub
      </a>
    </article>

    <p v-if="projects.length === 0">
      No projects available yet.
    </p>
  </section>
</template>
<style scoped>

</style>