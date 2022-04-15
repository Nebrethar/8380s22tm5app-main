import { createRouter, createWebHashHistory } from 'vue-router'
import DashboardHome from '@/components/DashboardHome.vue'
import Base from '@/components/Base.vue'
import NotFoundComponent from '@/components/NotFoundComponent.vue'
import LoggedInDashboard from '@/components/LoggedInDashboard.vue'
import PreferencesView from '../views/PreferencesView.vue'
import PlaylistView from '../views/PlaylistView.vue'
import Auth from '@/components/Auth.vue'
import Signup from '@/components/Signup.vue'

const routes = [
  {
    path: '/Base',
    name: 'base',
    component: Base
  },
  {
    path: '/',
    name: 'home',
    component: DashboardHome
  },
  {
    path: '/home',
    name: 'loggedinhome',
    component: LoggedInDashboard
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
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
