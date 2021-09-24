import Vue from 'vue'
import App from './App.vue'
import router from './router'
import { BootstrapVue,BootstrapVueIcons   } from 'bootstrap-vue'
Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'




new Vue({
   router,
  render: h => h(App), 
}).$mount('#app')
