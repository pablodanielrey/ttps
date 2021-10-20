import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Paciente from '@/components/Paciente/nuevoPaciente.vue'
import ListaPacientes from '@/components/Paciente/listaPacientes.vue'
import NuevaObraSocial from '@/components/Paciente/nuevaObraSocial.vue'

// lo siguiente necesita que vue tenga el compilador de templates.
// const Foo = { template: '<div>superrr fooooo</div>' }

const routes = [
    { path: '/paciente', component: Paciente },
    { path: '/lista', component: ListaPacientes },
    { path: '/obraSocial', component: NuevaObraSocial },
   
]

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: routes
})


export default router