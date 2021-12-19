import Api from "@/services/Api"

const API_USER = ''
const API_URL = '/admin_api/'

export default {
    obtenerModo() {
        return Api().get(API_URL + API_USER + "configuracion/")
        
    },
    habilitarModo1() {
        return Api().post(API_URL + API_USER + "modo/");
    },
}