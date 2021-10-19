import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Paciente from '@/components/Paciente/nuevoPaciente.vue'

// lo siguiente necesita que vue tenga el compilador de templates.
// const Foo = { template: '<div>superrr fooooo</div>' }

const routes = [
    { path: '/', component: Paciente }
]

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: routes
})
export default router