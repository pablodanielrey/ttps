import Api from "@/services/Api"

const API_USER = ''
const API_URL = '/admin_api/'

export default {
    obtenerModo() {
        return Api().get(API_URL + API_USER + "configuracion/");
    },
    guardarModo(modo) {
        if (modo == "PO")
            return Api().post(API_URL + API_USER + "configuracion/", ({"modo_operacion": "PO"}))
        else
            return Api().post(API_URL + API_USER + "configuracion/", ({"modo_operacion": "PNO"}))
    },
}