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
import ListaObrasSociales from '@/components/ObraSocial/listaObrasSociales.vue'


import NuevoEstudio from '@/components/Estudio/nuevoEstudio.vue'
import DetalleDeUnEstudio from '@/components/Estudio/detalleDeUnEstudio.vue'

//estados de estudios
import EsperandoFactura from '@/components/EstadosEstudio/esperandoFactura.vue'
import EsperandoComprobantePago from '@/components/EstadosEstudio/esperandoComprobantePago.vue'
import AnuladorPorFaltaDePago from '@/components/EstadosEstudio/AnuladorPorFaltaDePago.vue'

import EnviarConsentimientoInformado from '@/components/EstadosEstudio/enviarConsentimientoInformado.vue'
import EsperandoConsentimientoInformado from '@/components/EstadosEstudio/esperandoConsentimientoInformado.vue'
import EsperandoSeleccionDeTurnoExtraccion from '@/components/EstadosEstudio/esperandoSeleccionDeTurnoExtraccion.vue'
import EsperandoTomaDeMuestra from '@/components/EstadosEstudio/esperandoTomaDeMuestra.vue'
import EsperandoRetiroExtraccion from '@/components/EstadosEstudio/esperandoRetiroExtraccion.vue'
import EsperandoLoteDeMuestraParaProcesamientoBiotecnologico from '@/components/EstadosEstudio/EsperandoLoteDeMuestraParaProcesamientoBiotecnologico.vue'
import EsperandoInterpretacionDeResultados from '@/components/EstadosEstudio/EsperandoInterpretacionDeResultados.vue'
import EsperandoProcesamientoDeLoteBiotecnologico from '@/components/EstadosEstudio/EsperandoProcesamientoDeLoteBiotecnologico.vue'
import EsperandoEntregaAMedicoDerivante from '@/components/EstadosEstudio/EsperandoEntregaAMedicoDerivante.vue'
import ResultadoDeEstudioEntregado from '@/components/EstadosEstudio/ResultadoDeEstudioEntregado.vue'




import EsperandoInterpretacionDeResultadosInformante from '@/components/Estudio/EsperandoInterpretacionDeResultadosInformante.vue'
import listaEstudiosEsperandoInforme from '@/components/Estudio/listaEstudiosEsperandoInforme.vue'



// lotes
import CrearLote from '@/components/Lotes/crearLote.vue'
import CargarResultadoLote from '@/components/Lotes/cargarResultadoLote.vue'

// configurador
import ConfigurarTurnos from '@/components/Turnos/configurarTurnos.vue'
import ConfigurarFechasSinTurno from '@/components/Turnos/configurarFechasSinTurno.vue'

//turnos
import TurnosOcupados from '@/components/Turnos/turnosOcupados.vue'

// lo siguiente necesita que vue tenga el compilador de templates.
// const Foo = { template: '<div>superrr fooooo</div>' }

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [{
        path: '/',
        name:'home',
        component: container ,
        meta: { 
        requireAuth: true
        },
        children: [    
            { path: '/paciente', component: Paciente, name: 'paciente', props: true },
            { path: '/lista', component: ListaPacientes  ,name:'listaPacientes'},
            { path: '/obraSocial', component: NuevaObraSocial ,name:'obraSocial' },
            { path: '/listaObrasSociales', component: ListaObrasSociales ,name:'listaObrasSociales' },
            
            { path: '/estudio', component: NuevoEstudio , name:'nuevoEstudio'},
            { path: '/listaEstudios', component: ListaEstudios, name:'listaEstudios' },
            { path: '/esperandoFactura', component: EsperandoFactura },
            { path: '/esperandoComprobantePago', component: EsperandoComprobantePago , name:'EsperandoComprobanteDePago' ,props:true},
            { path: '/anuladoFaltaPago', component: AnuladorPorFaltaDePago , name:'AnuladorPorFaltaDePago' },
            { path: '/enviarConsentimientoInformado', component: EnviarConsentimientoInformado, name:'EnviarConsentimientoInformado', props:true },
            { path: '/esperandoConsentimientoInformado', component: EsperandoConsentimientoInformado , name:'EsperandoConsentimientoInformado' ,props:true },
            { path: '/esperandoSeleccionDeTurnoExtraccion', component: EsperandoSeleccionDeTurnoExtraccion, name:'EsperandoSeleccionDeTurnoParaExtraccion',props:true },
            { path: '/esperandoTomaDeMuestra', component: EsperandoTomaDeMuestra , name:'EsperandoTomaDeMuestra',props:true },
            { path: '/esperandoRetiroExtraccion', component: EsperandoRetiroExtraccion , name:'EsperandoRetiroDeExtaccion',props:true },
            { path: '/EsperandoLoteDeMuestraParaProcesamientoBiotecnologico', component: EsperandoLoteDeMuestraParaProcesamientoBiotecnologico , name:'EsperandoLoteDeMuestraParaProcesamientoBiotecnologico',props:true },
            { path: '/EsperandoInterpretacionDeResultados', component: EsperandoInterpretacionDeResultados , name:'EsperandoInterpretacionDeResultados',props:true },
            { path: '/EsperandoProcesamientoDeLoteBiotecnologico', component: EsperandoProcesamientoDeLoteBiotecnologico , name:'EsperandoProcesamientoDeLoteBiotecnologico',props:true },
            { path: '/EsperandoEntregaAMedicoDerivante', component: EsperandoEntregaAMedicoDerivante , name:'EsperandoEntregaAMedicoDerivante',props:true },
           
            { path: '/ResultadoDeEstudioEntregado', component: ResultadoDeEstudioEntregado , name:'ResultadoDeEstudioEntregado',props:true },
            
            
            { path: '/crearLote', component: CrearLote, name:'crearLote' },
            { path: '/cargarResultadoLote', component: CargarResultadoLote, name:'cargarResultadoLote'},

            { path: '/configurarTurnos', component: ConfigurarTurnos ,name:'configurarTurnos'},
            { path: '/configurarFechasSinTurnos', component: ConfigurarFechasSinTurno },
            { path: '/turnosOcupados', component: TurnosOcupados , name:'turnosOcupados'},

            { path: '/EsperandoInterpretacionDeResultadosInformante', component: EsperandoInterpretacionDeResultadosInformante , name:'EsperandoInterpretacionDeResultadosInformante',props:true },
            { path: '/listaEstudiosEsperandoInforme', component: listaEstudiosEsperandoInforme , name:'listaEstudiosEsperandoInforme',props:true },

            
            { path: '/detalleDeEstudio', component: DetalleDeUnEstudio, name:'detalleDeEstudio',props: true  }
        ]
    },
    {
     path: '/login', component: Login, name:'Login'},
    ],
})
router.beforeEach((to, from, next) => {
    const requireAuth = to.matched.some(record => record.meta.requireAuth)
  console.log(requireAuth)
  console.log(window.localStorage.getItem('credenciales'))
    if (requireAuth && !window.localStorage.getItem('credenciales')) {
      next('/login')
    } else if (window.localStorage.getItem('credenciales') && to.name == 'Login') {   
      next('/')
    } else {
      if (!to.matched.length) {     
        next('/');
      } else {     
        next();
      }
     
    }
  })



export default router