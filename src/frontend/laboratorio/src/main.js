import { createApp } from 'vue'
import App from './App.vue'

import './veevalidate'
import router from './router'

const vueApp = createApp(App)
vueApp.use(router)


// seteo bootstrap
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// Make BootstrapVue available throughout your project
vueApp.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
vueApp.use(IconsPlugin)


// monto la app
vueApp.mount('#app')

export default vueApp