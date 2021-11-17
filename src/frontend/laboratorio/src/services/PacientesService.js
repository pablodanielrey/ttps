import Api from "@/services/Api"

const API_USER = ''
const API_URL = '/personas_api/'

export default {
    obtenerPacientes() {
        return Api().get(API_URL + API_USER + "pacientes/")
    },
    obtenerPaciente(id) {
        return Api().get(API_URL + API_USER + "pacientes/" + id)
    },
    crearPaciente(paciente) {
        return Api().post(API_URL + API_USER + "pacientes/", paciente);
    },
    obtenerMedicosInformantes(){
        return Api().get(API_URL + API_USER + "medicos_informantes/")
    },
    obtenerMedicosDerivantes(){
        return Api().get(API_URL + API_USER + "medicos_derivantes/")
    }
    
}