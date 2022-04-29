import { createRouter, createWebHistory } from 'vue-router'
import DashboardHome from '@/components/DashboardHome.vue'
import Base from '@/components/Base.vue'
import NotFoundComponent from '@/components/NotFoundComponent.vue'
import LoggedInDashboard from '@/components/LoggedInDashboard.vue'
import PreferencesView from '../views/PreferencesView.vue'
import PlaylistView from '../views/PlaylistView.vue'
import Auth from '@/components/Auth.vue'
import LogOut from '@/components/LogOut.vue'
import SocialPost from '@/components/SocialPost.vue'
import Signup from '@/components/Signup.vue'
import Random from "@/components/Random"
import Weather from "@/components/Weather"
import Genre from "@/components/Genre"

const Vue = window.vue;
import VueRouter from 'vue-router';

const routes = [
  {
    path: '/Base',
    name: 'base',
    component: Base
  },
  {
    path: '/404/',
    name: 'notfound',
    component: NotFoundComponent
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
    path: '/social-post',
    name: 'socialpost',
    component: SocialPost
  },
  /*
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ //'../views/AboutView.vue')
  //},
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
    path: '/authout',
    name: 'Authout',
    component: DashboardHome
  },
  {
    path: '/authin',
    name: 'Authin',
    component: LoggedInDashboard
  },
  {
    path: '/logout',
    name: 'LogOut',
    component: LogOut
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/random',
    name: 'Random',
    component: Random
  },
  {
    path: '/weather',
    name: 'Weather',
    component: Weather
  },
  {
    path: '/genre',
    name: 'Genre',
    component: Genre
  },
  {
    path: '/404', name: 'NotFound', component: NotFoundComponent
  },
  {
    path: '/:catchAll(.*)', redirect:'404'
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})
export default router
