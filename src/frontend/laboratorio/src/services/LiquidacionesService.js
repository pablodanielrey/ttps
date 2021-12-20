import Api from "@/services/Api"

const API_USER = ''
const API_URL = '/liquidaciones_api/'

export default {
    obtenerEstudiosLiquidar() {
        return Api().get(API_URL + API_USER + "liquidaciones/")
    },
    crearLiquidaciones(estudios){
        return Api().post(API_URL  + "liquidaciones/", estudios);    
    },
    obtenerEstudiosLiquidados() {
        return Api().get(API_URL + API_USER + "liquidados/")
    },
 
    
  
    
}