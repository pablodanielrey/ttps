import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)
//home
import container from '@/components/Home/Container.vue'

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
            { path: '/paciente', component: Paciente, name: 'paciente', props: true },
            { path: '/lista', component: ListaPacientes  ,name:'listaPacientes'},
            { path: '/obraSocial', component: NuevaObraSocial },
            { path: '/estudio', component: NuevoEstudio , name:'nuevoEstudio'},
            { path: '/listaEstudios', component: ListaEstudios, name:'listaEstudios' },
            { path: '/esperandoFactura', component: EsperandoFactura },
            { path: '/esperandoComprobantePago', component: EsperandoComprobantePago , name:'esperandoComprobantePago' ,props:true},
            { path: '/enviarConsentimientoInformado', component: EnviarConsentimientoInformado },
            { path: '/esperandoConsentimientoInformado', component: EsperandoConsentimientoInformado , name:'esperandoConsentimientoInformado' ,props:true },
            { path: '/esperandoSeleccionDeTurnoExtraccion', component: EsperandoSeleccionDeTurnoExtraccion, name:'seleccionTurno',props:true },
            { path: '/esperandoTomaDeMuestra', component: EsperandoTomaDeMuestra , name:'esperandoTomaDeMuestra',props:true },
            { path: '/esperandoRetiroExtraccion', component: EsperandoRetiroExtraccion , name:'esperandoRetiroExtraccion',props:true },

            { path: '/crearLote', component: CrearLote, name:'crearLote' },
            { path: '/cargarResultadoLote', component: CargarResultadoLote, name:'cargarResultadoLote'},

            { path: '/configurarTurnos', component: ConfigurarTurnos },
            { path: '/configurarFechasSinTurnos', component: ConfigurarFechasSinTurno },

            { path: '/detalleDeEstudio', component: DetalleDeUnEstudio, name:'detalleDeEstudio',props: true  }
        ]
    },
    {
     path: '/login', component: Login },
    ],
})




export default router