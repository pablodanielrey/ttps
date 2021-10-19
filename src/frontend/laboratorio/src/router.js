import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Paciente from '@/components/Paciente/nuevoPaciente.vue'
import ListaPacientes from '@/components/Paciente/listaPacientes.vue'
import Buscar from '@/components/Paciente/pruebaService.vue'

// lo siguiente necesita que vue tenga el compilador de templates.
// const Foo = { template: '<div>superrr fooooo</div>' }

const routes = [
    { path: '/buscar', component: Buscar },
    { path: '/paciente', component: Paciente },
    { path: '/lista', component: ListaPacientes },
   
]

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: routes
})


export default router