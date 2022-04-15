import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import './static/css/styles.css'
import './static/js/scripts.js'

createApp(App).use(store, axios).use(router).mount('#app')
