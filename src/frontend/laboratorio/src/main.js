import { createApp } from 'vue'
import App from './App.vue'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// import './veevalidate'
import router from './router'


const vueApp = createApp(App)
vueApp.use(BootstrapVue)
vueApp.use(IconsPlugin)
vueApp.use(router)

vueApp.mount('#app')

