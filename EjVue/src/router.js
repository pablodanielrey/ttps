import Vue from 'vue'
import Router from 'vue-router'
import Perfil from '@/components/Usuario/Perfil.vue'
import container from '@/components/menu/Container.vue'
import home from '@/components/Home/Home.vue'
import Login from '@/components/Inicio/Login.vue'
import newPaciente from '@/components/Paciente/newPaciente.vue'

Vue.use(Router)
const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [{
    path: '/',
    component: container ,
    meta: { 
      requireAuth: false
    },
    children: [
      {
        path: '/',
        name: 'Home',
        component: home               
       },     
       {
        path: '/perfil',
         name: 'perfil',
        component: Perfil,   
        props: true      
       },
       {
        path: '/nuevoPaciente',
         name: 'newPaciente',
        component: newPaciente,   
        props: true      
       },
    ]
    },
    {
      path: '/login',    
      component: () => import('@/components/Inicio/BaseLogin.vue'), 
      meta: {
        requireAuth: false
      },
      children: [{
          path: '/login',
          name: 'login',
          component: Login,
        },
      
      ]
    }, 
  ]
})
export default router

