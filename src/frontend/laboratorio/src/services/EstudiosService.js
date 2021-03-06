import Api from "@/services/Api"
import axios from 'axios'
const API_USER = ''
const API_URL = '/estudio_api/'

export default {
    obtenerEstudios() {
        return Api().get(API_URL + API_USER + "tiposEstudio/")
    },
    obtenerEstudio(id) {
        return Api().get(API_URL + API_USER + "estudios/" + id)
    },   
    obtenerTurnos() {
        return Api().get(API_URL + API_USER + "listaTurnos/")
    },
    crearEstudio(estudio){
        return Api().post(API_URL + API_USER + "estudios/", estudio);
    },
    obtenerDiagnosticos() {
        return Api().get(API_URL + API_USER + "diagnosticos/")
    },
    obtenerListaEstudios() {
        return Api().get(API_URL + API_USER + "estudios/")
    },
    actualizarUltimoEstado(datos,id_ultimo_estado){           
        return Api().put(API_URL + API_USER + "estados/"+id_ultimo_estado +'/',datos)
    },
    obtenerListaEstudiosParaInformes(){
        return Api().get(API_URL + API_USER + "estudios/buscar/?e=EsperandoInterpretacionDeResultados")
    },
    obtenerConsentimientoInformado(idEstudio){      
      return Api().get(API_URL + API_USER + "estudios/"+idEstudio+"/consentimiento_informado/")

    },
    descargarPresupuesto(id){
        let credenciales = JSON.parse(window.localStorage.getItem('credenciales'));       
        axios({
            method: 'get',
            url: process.env.VUE_APP_API_URL + API_URL + API_USER + "estudios/" + id + "/presupuesto/",
            responseType: 'arraybuffer',
            auth: {
                'username': credenciales.usuario,
                'password': credenciales.clave
            }
           
          }).then(function(response) {
            let blob = new Blob([response.data], { type: 'application/pdf' })
            let link = document.createElement('a')
            link.href = window.URL.createObjectURL(blob)
            link.download = 'Presupuesto.pdf'
            link.click()
          })
    },
    descargarPago(id){
        let credenciales = JSON.parse(window.localStorage.getItem('credenciales'));       
        axios({
            method: 'get',
            url: process.env.VUE_APP_API_URL + API_URL + API_USER + "estudios/" + id + "/comprobante_de_pago/",
            responseType: 'arraybuffer',
            auth: {
                'username': credenciales.usuario,
                'password': credenciales.clave
            }
           
          }).then(function(response) {
            let blob = new Blob([response.data], { type: 'application/pdf' })
            let link = document.createElement('a')
            link.href = window.URL.createObjectURL(blob)
            link.download = 'Pago.pdf'
            link.click()
          })
    },
    descargarConsentimiento(id){
        let credenciales = JSON.parse(window.localStorage.getItem('credenciales'));       
        axios({
            method: 'get',
            url: process.env.VUE_APP_API_URL + API_URL + API_USER + "estudios/" + id + "/consentimiento_informado/",
            responseType: 'arraybuffer',
            auth: {
                'username': credenciales.usuario,
                'password': credenciales.clave
            }
           
          }).then(function(response) {
            let blob = new Blob([response.data], { type: 'application/pdf' })
            let link = document.createElement('a')
            link.href = window.URL.createObjectURL(blob)
            link.download = 'ConsentimientoFirmado.pdf'
            link.click()
          })
    },
    descargarInformeDeResultado(id){
        let credenciales = JSON.parse(window.localStorage.getItem('credenciales'));       
        axios({
            method: 'get',
            url: process.env.VUE_APP_API_URL + API_URL + API_USER + "estudios/" + id + "/informe_de_resultado/",
            responseType: 'arraybuffer',
            auth: {
                'username': credenciales.usuario,
                'password': credenciales.clave
            }
           
          }).then(function(response) {
            let blob = new Blob([response.data], { type: 'application/pdf' })
            let link = document.createElement('a')
            link.href = window.URL.createObjectURL(blob)
            link.download = 'informe-final.pdf'
            link.click()
          })
    }
}