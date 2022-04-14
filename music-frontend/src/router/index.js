import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '@/components/DashboardHome.vue'
import PreferencesView from '../views/PreferencesView.vue'
import PlaylistView from '../views/PlaylistView.vue'
import Auth from '@/components/Auth.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/user-preferences',
    name: 'preferences',
    component: PreferencesView
  },
  {
    path: '/playlists',
    name: 'playlists',
    component: PlaylistView
  },
  {
    path: '/auth',
    name: 'Auth',
    component: Auth
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
