import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Login from '@/components/Login/Login.vue'
import Paciente from '@/components/Paciente/nuevoPaciente.vue'
import ListaPacientes from '@/components/Paciente/listaPacientes.vue'
import NuevaObraSocial from '@/components/ObraSocial/nuevaObraSocial.vue'

// lo siguiente necesita que vue tenga el compilador de templates.
// const Foo = { template: '<div>superrr fooooo</div>' }

const routes = [
    { path: '/login', component: Login },
    { path: '/paciente', component: Paciente,  name:'paciente' } ,
    { path: '/lista', component: ListaPacientes },
    { path: '/obraSocial', component: NuevaObraSocial },
   
]

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: routes
})


export default router