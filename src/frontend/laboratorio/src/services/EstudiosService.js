import Api from "@/services/Api"

const API_USER = ''
const API_URL = '/estudio_api/'

export default {
    obtenerEstudios() {
        return Api().get(API_URL + API_USER + "tiposEstudio/")
    },
  
    
}