
import { createRouter, createWebHistory } from 'vue-router'
// import nuevoPaciente from '@/components/Paciente/nuevoPaciente'

const routes = [
    // {path:'/', component: nuevoPaciente}
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router