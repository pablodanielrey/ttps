import Api from "@/services/Api"

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
    actualizarUltimoEstado(datos){
        return Api().post(API_URL + API_USER + "estados/",datos)
    }
    
  
    
}