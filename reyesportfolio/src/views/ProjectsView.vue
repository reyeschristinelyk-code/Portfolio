
<script setup lang="ts">
import { ref } from 'vue'

interface Project {
  id: number
  title: string
  description: string
  image: string
  technologies: string[]
  category: string
  github: string
  demo: string
}

const projects = ref<Project[]>([
  {
    id: 1,
    title: 'Golden Harvest Smart Boarding House Manager',
    description:
        'A web-based platform for Golden Harvest Subdivision HOA that connects landlords and students through verified listings, bookings, ratings, and HOA approval.',
    image: '/images/golden-harvest.png',
    technologies: ['Vue.js', 'Django', 'Tailwind CSS', 'MySQL'],
    category: 'Web Development',
    github: '',
    demo: '',
  },
  {
    id: 2,
    title: 'Vue + Django Portfolio',
    description:
        'My personal portfolio built with Vue.js and Django REST Framework, featuring personal information, skills, hobbies, and project showcases.',
    image: '/images/portfolio.png',
    technologies: ['Vue.js', 'TypeScript', 'Django REST', 'Pinia'],
    category: 'Web Development',
    github: '',
    demo: '',
  },
  {
    id: 3,
    title: 'Sari-Sari Store System',
    description:
        'An inventory and sales management system designed to help a small store organize products, monitor stock, and manage sales records.',
    image: '/images/sari-sari.png',
    technologies: ['Microsoft Access', 'Database', 'Forms', 'Reports'],
    category: 'Database System',
    github: '',
    demo: '',
  },
  {
    id: 4,
    title: 'CSU Carig COEA Marketplace',
    description:
        'A research-based marketplace concept for COEA students, focusing on product listings, categories, and a simple buying process.',
    image: '/images/marketplace.png',
    technologies: ['HTML', 'CSS', 'JavaScript', 'PHP'],
    category: 'Web Development',
    github: '',
    demo: '',
  },
  {
    id: 5,
    title: 'Agoscoop (SEAGBIN)',
    description:
        'A solar-powered, Arduino-based river trash collector designed to help collect floating waste in the Cagayan River and support environmental protection.',
    image: '/images/agoscoop.png',
    technologies: ['Arduino', 'C/C++', 'I2C LCD', 'Solar Power'],
    category: 'Embedded Systems',
    github: '',
    demo: '',
  },
  {
    id: 6,
    title: 'Hobby Tracker',
    description:
        'An interactive hobby page where users can explore reading AUs, music, GL series, and anime through expandable cards.',
    image: '/images/hobby-tracker.png',
    technologies: ['Vue.js', 'TypeScript', 'CSS', 'Pinia'],
    category: 'Frontend Development',
    github: '',
    demo: '',
  },
])

const filters = [
  'All Projects',
  'Web Development',
  'Database System',
  'Embedded Systems',
  'Frontend Development',
]

const activeFilter = ref('All Projects')

const filteredProjects = () => {
  if (activeFilter.value === 'All Projects') {
    return projects.value
  }

  return projects.value.filter(
      (project) => project.category === activeFilter.value,
  )
}
</script>

<template>
  <section class="projects-section">
    <div class="projects-container">
      <!-- Page Heading -->
      <header class="projects-header">
        <p class="eyebrow">MY WORK</p>
        <h1>My Projects</h1>
        <p class="subtitle">
          Here are some of the projects I've worked on, showcasing my skills
          in web development, system design, and problem solving.
        </p>
        <div class="heading-line"></div>
      </header>

      <!-- Project Filters -->
      <nav class="project-filters" aria-label="Filter projects">
        <button
            v-for="filter in filters"
            :key="filter"
            type="button"
            :class="{ active: activeFilter === filter }"
            @click="activeFilter = filter"
        >
          {{ filter }}
        </button>
      </nav>

      <!-- Project Cards -->
      <div class="projects-grid">
        <article
            v-for="project in filteredProjects()"
            :key="project.id"
            class="project-card"
        >
          <!-- Project Image -->
          <div class="project-image">
            <img
                :src="project.image"
                :alt="project.title + ' preview'"
                loading="lazy"
                @error="($event.target as HTMLImageElement).style.display = 'none'"
            />

            <span class="project-number">
              {{ String(project.id).padStart(2, '0') }}
            </span>
          </div>

          <!-- Project Details -->
          <div class="project-content">
            <span class="project-category">
              {{ project.category }}
            </span>

            <h2>{{ project.title }}</h2>

            <p class="project-description">
              {{ project.description }}
            </p>

            <!-- Technology Tags -->
            <div class="technology-list">
              <span
                  v-for="technology in project.technologies"
                  :key="technology"
                  class="technology-tag"
              >
                {{ technology }}
              </span>
            </div>

            <!-- Project Links -->
            <div class="project-actions">
              <a
                  v-if="project.demo"
                  :href="project.demo"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="project-button primary-button"
              >
                <svg
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    aria-hidden="true"
                >
                  <path d="M14 3h7v7" />
                  <path d="M10 14 21 3" />
                  <path d="M19 13v7a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h7" />
                </svg>
                View Project
              </a>

              <span v-else class="project-button primary-button disabled-button">
                Project Preview
              </span>

              <a
                  v-if="project.github"
                  :href="project.github"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="project-button github-button"
              >
                <svg
                    viewBox="0 0 24 24"
                    fill="currentColor"
                    aria-hidden="true"
                >
                  <path
                      d="M12 .9a11.1 11.1 0 0 0-3.51 21.63c.55.1.76-.24.76-.54v-2.1c-3.1.67-3.75-1.32-3.75-1.32-.5-1.28-1.23-1.62-1.23-1.62-1.01-.69.08-.68.08-.68 1.12.08 1.71 1.15 1.71 1.15.99 1.7 2.6 1.21 3.23.92.1-.72.39-1.21.7-1.49-2.48-.28-5.08-1.24-5.08-5.5 0-1.22.44-2.21 1.15-2.99-.12-.28-.5-1.42.11-2.95 0 0 .94-.3 3.05 1.14a10.6 10.6 0 0 1 5.55 0c2.11-1.44 3.05-1.14 3.05-1.14.61 1.53.23 2.67.11 2.95.72.78 1.15 1.77 1.15 2.99 0 4.27-2.6 5.22-5.09 5.49.4.35.75 1.02.75 2.06v3.09c0 .3.2.65.77.54A11.1 11.1 0 0 0 12 .9Z"
                  />
                </svg>
                GitHub
              </a>

              <span v-else class="project-button github-button disabled-button">
                GitHub
              </span>
            </div>
          </div>
        </article>
      </div>

      <!-- Empty State -->
      <div
          v-if="filteredProjects().length === 0"
          class="empty-state"
      >
        No projects found in this category.
      </div>

      <!-- Footer -->
      <footer class="projects-footer">
        <p>More projects and ideas are still in progress.</p>
        <span>Designed and developed by me.</span>
      </footer>
    </div>
  </section>
</template>

<style scoped>
.projects-section {
  min-height: 100vh;
  padding: 55px 24px 35px;
  background-color: #879f78;
  color: #f9faf6;
}

.projects-container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
}

/* Heading */
.projects-header {
  max-width: 720px;
  margin: 0 auto 35px;
  text-align: center;
}

.eyebrow {
  margin-bottom: 10px;
  color: #d0e7b5;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: 4px;
}

.projects-header h1 {
  margin: 0;
  color: #ffffff;
  font-size: clamp(32px, 5vw, 46px);
  font-weight: 800;
  letter-spacing: -1.5px;
}

.subtitle {
  max-width: 650px;
  margin: 15px auto 20px;
  color: #f0f3ec;
  font-size: 16px;
  line-height: 1.8;
}

.heading-line {
  width: 65px;
  height: 5px;
  margin: 0 auto;
  border-radius: 10px;
  background-color: #b2dba1;
}

/* Filters */
.project-filters {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  margin-bottom: 32px;
}

.project-filters button {
  padding: 9px 16px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 30px;
  background: rgba(40, 65, 52, 0.35);
  color: #ffffff;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s, color 0.2s, transform 0.2s;
}

.project-filters button:hover {
  transform: translateY(-2px);
  background: #536c57;
}

.project-filters button.active {
  border-color: #b2dba1;
  background: #b2dba1;
  color: #263d2e;
}

/* Grid */
.projects-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 24px;
  align-items: stretch;
}

/* Card */
.project-card {
  display: flex;
  min-width: 0;
  flex-direction: column;
  overflow: hidden;
  border: 1px solid rgba(220, 237, 210, 0.16);
  border-radius: 20px;
  background: #40594a;
  box-shadow: 0 8px 24px rgba(30, 49, 37, 0.12);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.project-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 15px 30px rgba(30, 49, 37, 0.22);
}

/* Image */
.project-image {
  position: relative;
  display: flex;
  min-height: 190px;
  aspect-ratio: 16 / 9;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  margin: 12px 12px 0;
  border-radius: 13px;
  background: linear-gradient(135deg, #dce9d4, #b2c9a8);
}

.project-image img {
  width: 100%;
  height: 100%;
  position: absolute;
  inset: 0;
  object-fit: cover;
  transition: transform 0.4s ease;
}

.project-card:hover .project-image img {
  transform: scale(1.04);
}

.project-number {
  position: absolute;
  right: 10px;
  bottom: 10px;
  padding: 5px 10px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 20px;
  background: rgba(35, 59, 44, 0.85);
  color: #ffffff;
  font-size: 12px;
  font-weight: 700;
}

/* Details */
.project-content {
  display: flex;
  flex: 1;
  flex-direction: column;
  padding: 20px;
}

.project-category {
  align-self: flex-start;
  margin-bottom: 10px;
  color: #c6e6b6;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 1.1px;
  text-transform: uppercase;
}

.project-content h2 {
  margin: 0 0 12px;
  color: #ffffff;
  font-size: 19px;
  font-weight: 750;
  line-height: 1.4;
  overflow-wrap: anywhere;
}

.project-description {
  margin: 0 0 18px;
  color: #e2e9e0;
  font-size: 14px;
  line-height: 1.75;
}

/* Technology tags */
.technology-list {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 22px;
}

.technology-tag {
  padding: 6px 11px;
  border: 1px solid rgba(178, 219, 161, 0.22);
  border-radius: 30px;
  background: #b2dba1;
  color: #294432;
  font-size: 11px;
  font-weight: 700;
}

/* Buttons */
.project-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: auto;
}

.project-button {
  display: inline-flex;
  min-height: 40px;
  flex: 1;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 12px;
  border: 1px solid transparent;
  border-radius: 30px;
  font-family: inherit;
  font-size: 12px;
  font-weight: 700;
  text-align: center;
  text-decoration: none;
  transition: background 0.2s, color 0.2s, border-color 0.2s;
}

.project-button svg {
  width: 17px;
  height: 17px;
  flex-shrink: 0;
}

.primary-button {
  background: #b2dba1;
  color: #263d2e;
}

.primary-button:hover {
  background: #d0eabb;
}

.github-button {
  border-color: rgba(230, 240, 225, 0.5);
  background: transparent;
  color: #ffffff;
}

.github-button:hover {
  border-color: #b2dba1;
  background: rgba(178, 219, 161, 0.12);
}

.disabled-button {
  cursor: default;
  opacity: 0.7;
}

/* Empty state */
.empty-state {
  padding: 35px;
  border-radius: 15px;
  background: #40594a;
  color: #ffffff;
  text-align: center;
}

/* Footer */
.projects-footer {
  margin-top: 45px;
  padding-top: 22px;
  border-top: 1px solid rgba(255, 255, 255, 0.2);
  color: #f0f3ec;
  text-align: center;
}

.projects-footer p {
  margin: 0 0 8px;
  font-size: 14px;
}

.projects-footer span {
  color: #d3e1cc;
  font-size: 12px;
}

/* Tablet */
@media (max-width: 1000px) {
  .projects-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 20px;
  }

  .project-image {
    min-height: 170px;
  }

  .project-content {
    padding: 18px;
  }
}

/* Mobile */
@media (max-width: 600px) {
  .projects-section {
    padding: 35px 16px 25px;
  }

  .projects-header {
    margin-bottom: 28px;
  }

  .projects-header h1 {
    letter-spacing: -0.8px;
  }

  .subtitle {
    font-size: 14px;
    line-height: 1.7;
  }

  .project-filters {
    gap: 8px;
    margin-bottom: 24px;
  }

  .project-filters button {
    padding: 8px 12px;
    font-size: 12px;
  }

  .projects-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }

  .project-image {
    min-height: 190px;
  }

  .project-content {
    padding: 20px;
  }

  .project-content h2 {
    font-size: 18px;
  }

  .project-description {
    font-size: 14px;
  }

  .project-button {
    min-height: 42px;
    font-size: 12px;
  }

  .projects-footer {
    margin-top: 30px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .project-card,
  .project-image img,
  .project-filters button,
  .project-button {
    transition: none;
  }

  .project-card:hover,
  .project-filters button:hover {
    transform: none;
  }
}
</style>
