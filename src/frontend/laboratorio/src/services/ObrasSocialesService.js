import Api from "@/services/Api"

const API_USER = ''
const API_URL = '/api/'

export default {
    obtenerObrasSociales() {
        return Api().get(API_URL + API_USER + "obrasSociales/")
    },
    crearObraSocial(obraSocial) {
        return Api().post(API_URL + API_USER + "obrasSociales/", obraSocial);
    }
    
}