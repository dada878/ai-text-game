import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import GameViewVue from '../views/GameView.vue'
import GameView from '../views/GameView.vue'
import StartViewVue from '../views/StartView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'start',
    component: StartViewVue
  },
  {
    path: '/game',
    name: 'game',
    component: GameViewVue
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
