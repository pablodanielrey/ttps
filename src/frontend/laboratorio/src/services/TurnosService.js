import Api from "@/services/Api"

const API_USER = ''
const API_URL = '/estudio_api/'

export default {
    obtenerTurnos() {
        return Api().get(API_URL + API_USER + "listaTurnos/")
    },
  
    
}