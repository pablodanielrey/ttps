import Api from "@/services/Api"

const API_USER = ''
const API_URL = '/estudios_api/'

export default {
    obtenerModo() {
        return Api().get(API_URL + API_USER + "modo/")
    },
    habilitarModo1() {
        return Api().post(API_URL + API_USER + "modo/");
    },
}