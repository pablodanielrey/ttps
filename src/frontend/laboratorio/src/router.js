import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import Login from '@/components/Login/Login.vue'
import Paciente from '@/components/Paciente/nuevoPaciente.vue'
import ListaPacientes from '@/components/Paciente/listaPacientes.vue'
import ListaEstudios from '@/components/Estudio/listaEstudios.vue'

import NuevaObraSocial from '@/components/ObraSocial/nuevaObraSocial.vue'
import NuevoEstudio from '@/components/Estudio/nuevoEstudio.vue'
import DetalleDeUnEstudio from '@/components/Estudio/detalleDeUnEstudio.vue'

//estados de estudios
import EsperandoFactura from '@/components/EstadosEstudio/esperandoFactura.vue'
import EsperandoComprobantePago from '@/components/EstadosEstudio/esperandoComprobantePago.vue'
import EnviarConsentimientoInformado from '@/components/EstadosEstudio/enviarConsentimientoInformado.vue'
import EsperandoConsentimientoInformado from '@/components/EstadosEstudio/esperandoConsentimientoInformado.vue'
import EsperandoSeleccionDeTurnoExtraccion from '@/components/EstadosEstudio/esperandoSeleccionDeTurnoExtraccion.vue'
import EsperandoTomaDeMuestra from '@/components/EstadosEstudio/esperandoTomaDeMuestra.vue'
import EsperandoRetiroExtraccion from '@/components/EstadosEstudio/esperandoRetiroExtraccion.vue'



// lotes
import CrearLote from '@/components/Lotes/crearLote.vue'
import CargarResultadoLote from '@/components/Lotes/cargarResultadoLote.vue'

// configurador
import ConfigurarTurnos from '@/components/Turnos/configurarTurnos.vue'
import ConfigurarFechasSinTurno from '@/components/Turnos/configurarFechasSinTurno.vue'

// lo siguiente necesita que vue tenga el compilador de templates.
// const Foo = { template: '<div>superrr fooooo</div>' }

const routes = [
    { path: '/login', component: Login },
    { path: '/paciente', component: Paciente, name: 'paciente', props: true },
    { path: '/lista', component: ListaPacientes },
    { path: '/obraSocial', component: NuevaObraSocial },
    { path: '/estudio', component: NuevoEstudio },
    { path: '/listaEstudios', component: ListaEstudios },
    { path: '/esperandoFactura', component: EsperandoFactura },
    { path: '/esperandoComprobantePago', component: EsperandoComprobantePago },
    { path: '/enviarConsentimientoInformado', component: EnviarConsentimientoInformado },
    { path: '/esperandoConsentimientoInformado', component: EsperandoConsentimientoInformado },
    { path: '/esperandoSeleccionDeTurnoExtraccion', component: EsperandoSeleccionDeTurnoExtraccion, name:'seleccionTurno',props:true },
    { path: '/esperandoTomaDeMuestra', component: EsperandoTomaDeMuestra },
    { path: '/esperandoRetiroExtraccion', component: EsperandoRetiroExtraccion },

    { path: '/crearLote', component: CrearLote },
    { path: '/cargarResultadoLote', component: CargarResultadoLote },

    { path: '/configurarTurnos', component: ConfigurarTurnos },
    { path: '/configurarFechasSinTurnos', component: ConfigurarFechasSinTurno },

    { path: '/detalleDeEstudio', component: DetalleDeUnEstudio, name:'detalleDeEstudio',props: true  },
]

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: routes
})


export default router