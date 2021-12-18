import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)
//home
import container from '@/components/Home/Container.vue'
import home from '@/components/Home/Home.vue'
import Login from '@/components/Login/Login.vue'
import Registrar from '@/components/Login/Registrar.vue'

import Paciente from '@/components/Paciente/nuevoPaciente.vue'
import ListaPacientes from '@/components/Paciente/listaPacientes.vue'
import ListaEstudios from '@/components/Estudio/listaEstudios.vue'
import ListaConfiugradores from '@/components/Paciente/listaConfiguradores.vue'
import NuevoConfigurador from '@/components/Paciente/altaConfigurador.vue'
import ListaMedicoInformante from '@/components/Paciente/listaMedicoInformante.vue'
import NuevoInformante from '@/components/Paciente/nuevoInformante.vue'
import ListaDerivante from '@/components/Paciente/listaDerivante.vue'
import NuevoDerivante from '@/components/Paciente/nuevoDerivante.vue'
import Estadisticas from '@/components/Estadisticas/estadisticas.vue'

import ListaEmpleado from '@/components/Paciente/listaEmpleado.vue'
import NuevoEmpleado from '@/components/Paciente/nuevoEmpleado.vue'



import NuevaObraSocial from '@/components/ObraSocial/nuevaObraSocial.vue'
import ListaObrasSociales from '@/components/ObraSocial/listaObrasSociales.vue'
import editarTemplateConsentimiento from '@/components/TemplateConsentimiento/editarTemplateConsentimiento'

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
import EsperandoLoteDeMuestraParaProcesamientoBiotecnologico from '@/components/EstadosEstudio/esperandoLoteDeMuestraParaProcesamientoBiotecnologico.vue'
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

const router = new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [{
        path: '/',
       
        component: container ,
        meta: { 
        requireAuth: true
        },
        children: [  
          {
            path: '/', name: 'home', component: home},  
            { path: '/paciente', component: Paciente, name: 'paciente', props: true },
            { path: '/configuradores', component: NuevoConfigurador ,name:'configuradores' , props: true},
            { path: '/listaConfiguradores', component: ListaConfiugradores ,name:'listaConfiguradores' },
            { path: '/medicoInformante', component: NuevoInformante ,name:'medicoInformante' , props: true},
            { path: '/listaMedicoInformante', component: ListaMedicoInformante ,name:'listaMedicoInformante' },
            { path: '/medicoDerivante', component: NuevoDerivante ,name:'medicoDerivante' , props: true},
            { path: '/listaDerivante', component: ListaDerivante ,name:'listaDerivante' },
            { path: '/empleado', component: NuevoEmpleado ,name:'empleado' , props: true},
            { path: '/listaEmpleado', component: ListaEmpleado ,name:'listaEmpleado' },
            { path: '/lista', component: ListaPacientes  ,name:'listaPacientes'},
            { path: '/obraSocial', component: NuevaObraSocial ,name:'obraSocial', props:true },
            { path: '/listaObrasSociales', component: ListaObrasSociales ,name:'listaObrasSociales' },
            { path: '/templateConsentimiento', component: editarTemplateConsentimiento ,name:'editarTemplateConsentimiento' },
            
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

            
            { path: '/detalleDeEstudio', component: DetalleDeUnEstudio, name:'detalleDeEstudio',props: true  },
            { path: '/estadisticas', component: Estadisticas, name:'estadisticas'  }

        ]
    },
    {
     path: '/login', component: Login, name:'Login'},
     {
      path: '/registrar', component: Registrar, name:'registrar'},
     
    ],
})
router.beforeEach((to, from, next) => {
    const requireAuth = to.matched.some(record => record.meta.requireAuth)

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