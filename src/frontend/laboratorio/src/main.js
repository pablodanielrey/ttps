import { createApp } from 'vue'
import App from './App.vue'

import './bootstrap'
import './veevalidate'
import router from './router'

const vueApp = createApp(App)
vueApp.use(router)

vueApp.mount('#app')

