import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Login from '@/components/Login/Login.vue'
import Paciente from '@/components/Paciente/nuevoPaciente.vue'
import ListaPacientes from '@/components/Paciente/listaPacientes.vue'
import NuevaObraSocial from '@/components/ObraSocial/nuevaObraSocial.vue'
import NuevoEstudio from '@/components/Estudio/nuevoEstudio.vue'

//estados de estudios
import EsperandoFactura from '@/components/EstadosEstudio/esperandoFactura.vue'
import EsperandoComprobantePago from '@/components/EstadosEstudio/esperandoComprobantePago.vue'
import EnviarConsentimientoInformado from '@/components/EstadosEstudio/enviarConsentimientoInformado.vue'
import EsperandoConsentimientoInformado from '@/components/EstadosEstudio/esperandoConsentimientoInformado.vue'
import EsperandoSeleccionDeTurnoExtraccion from '@/components/EstadosEstudio/esperandoSeleccionDeTurnoExtraccion.vue'


// configurador
import ConfigurarTurnos from '@/components/Turnos/configurarTurnos.vue'

// lo siguiente necesita que vue tenga el compilador de templates.
// const Foo = { template: '<div>superrr fooooo</div>' }

const routes = [
    { path: '/login', component: Login },
    { path: '/paciente', component: Paciente, name: 'paciente', props: true },
    { path: '/lista', component: ListaPacientes },
    { path: '/obraSocial', component: NuevaObraSocial },
    { path: '/estudio', component: NuevoEstudio },
    { path: '/esperandoFactura', component: EsperandoFactura },
    { path: '/esperandoComprobantePago', component: EsperandoComprobantePago },
    { path: '/enviarConsentimientoInformado', component: EnviarConsentimientoInformado },
    { path: '/esperandoConsentimientoInformado', component: EsperandoConsentimientoInformado },
    { path: '/esperandoSeleccionDeTurnoExtraccion', component: EsperandoSeleccionDeTurnoExtraccion },

    { path: '/configurarTurnos', component: ConfigurarTurnos }
]

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: routes
})


export default router