import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000'
// default port and address for django development server

createApp(App).use(store).use(router, axios).mount('#app')
// createApp(App).use(store).use(router).mount('#app')