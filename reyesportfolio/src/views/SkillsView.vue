
<script setup lang="ts">
import { ref, onMounted } from 'vue'

interface Skill {
  id: number
  name: string
  category: string
}

const skills = ref<Skill[]>([])
const loading = ref(true)

const personalSkills = [
  {
    name: 'Fast Learner',
    description: 'Quick to learn new skills, tools, and technologies.',
    image: '/images/fast-learning.png',
  },
  {
    name: 'Leadership',
    description: 'Able to guide a team and work toward shared goals.',
    image: '/images/leadership.png',
  },
  {
    name: 'Working Under Pressure',
    description: 'Can stay focused and complete tasks under pressure.',
    image: '/images/under-pressure.png',
  },
]

onMounted(async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/api/skills/')

    if (!response.ok) {
      throw new Error('Failed to load skills')
    }

    skills.value = await response.json()
  } catch (error) {
    console.error('Error loading skills:', error)
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <section class="skills-section">
    <h1>My Skills</h1>
    <p class="subtitle">
      Skills and qualities that help me learn, work, and grow.
    </p>

    <!-- Personal Skills with Pictures -->
    <div class="personal-skills">
      <article
          v-for="skill in personalSkills"
          :key="skill.name"
          class="skill-card"
      >
        <img :src="skill.image" :alt="skill.name" />

        <h2>{{ skill.name }}</h2>
        <p>{{ skill.description }}</p>
      </article>
    </div>

    <!-- Skills Loaded from Django -->
    <div class="technical-skills">
      <h2>Technical Skills</h2>

      <p v-if="loading">Loading skills...</p>

      <p v-else-if="skills.length === 0">
        No technical skills available yet.
      </p>

      <div v-else class="skill-list">
        <div
            v-for="skill in skills"
            :key="skill.id"
            class="skill-item"
        >
          <span class="skill-name">{{ skill.name }}</span>
          <span class="skill-category">{{ skill.category }}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.skills-section {
  min-height: 100vh;
  padding: 40px 24px;
  background-color: #879f78;
  color: #f9fafb;
}

.skills-section > h1,
.subtitle,
.technical-skills {
  max-width: 1000px;
  margin-left: auto;
  margin-right: auto;
}

.skills-section > h1 {
  font-size: 30px;
  font-weight: 700;
}

.subtitle {
  margin-top: 8px;
  margin-bottom: 30px;
  color: #cbd5e1;
}

.personal-skills {
  max-width: 1000px;
  margin: 0 auto 45px;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 24px;
}

.skill-card {
  padding: 24px;
  text-align: center;
  background-color: #5E5694;
  border: 1px solid #525252;
  border-radius: 14px;
  transition: transform 0.2s, border-color 0.2s;
}

.skill-card:hover {
  transform: translateY(-5px);
  border-color: #b2dba1;
}

.skill-card img {
  width: 100px;
  height: 100px;
  margin: 0 auto 18px;
  object-fit: contain;
}

.skill-card h2 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 10px;
  color: #b2dba1;
}

.skill-card p {
  color: #cbd5e1;
  font-size: 14px;
  line-height: 1.7;
}

.technical-skills {
  margin-top: 20px;
}

.technical-skills h2 {
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 20px;
}

.skill-list {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
}

.skill-item {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
  padding: 16px;
  background-color: #b2dba1;
  border: 1px solid #b9def0;
  border-radius: 10px;
  color: #263326;
}

.skill-name {
  font-weight: 600;
  color: #263326;
}

.skill-category {
  color: #405640;
  font-size: 13px;
}

@media (max-width: 700px) {
  .personal-skills {
    grid-template-columns: 1fr;
  }

  .skill-list {
    grid-template-columns: 1fr;
  }
}
</style>
