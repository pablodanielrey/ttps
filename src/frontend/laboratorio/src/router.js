
import { createRouter, createWebHistory } from 'vue-router'


const Prueba = {
    template: "<div>prueba</div>"
}

const routes = [
    { path:'/', component: Prueba }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})


export default router