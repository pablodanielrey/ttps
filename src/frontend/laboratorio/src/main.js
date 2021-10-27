import Vue from 'vue'

import router from './router'
import './bootstrap'
import './veevalidate'

import App from './App.vue'
import vSelect from "vue-select";
import "vue-select/dist/vue-select.css";
Vue.component("v-select", vSelect);

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
