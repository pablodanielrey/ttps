import Api from "@/services/Api"

const API_USER = ''
const API_URL = '/personas_api/'

export default {
    obtenerObrasSociales() {
        return Api().get(API_URL + API_USER + "obras_sociales/")
    },
    crearObraSocial(obraSocial) {
        return Api().post(API_URL + API_USER + "obras_sociales/", obraSocial);
    }
    
}