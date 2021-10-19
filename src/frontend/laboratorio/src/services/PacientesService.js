import Api from "@/services/Api"

const API_USER = ''
const API_URL = '/api/'

export default {
    obtenerPacientes(credentials) {
        return Api().get(API_URL + API_USER + "personas/", credentials)
    },
    obtenerPaciente(id) {
        return Api().get(API_URL + API_USER + "personas/" + id)
    },
    crearPaciente(paciente) {
        return Api().post(API_URL + API_USER + "personas/", paciente);
    }
}