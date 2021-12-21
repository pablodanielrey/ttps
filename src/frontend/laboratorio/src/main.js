import Vue from 'vue'
import store from './store'
import router from './router'
import './bootstrap'
import './veevalidate'

import App from './App.vue'
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";
Vue.component("v-select", vSelect);
import VueCrontab from 'vue-crontab'
 
Vue.use(VueCrontab)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
