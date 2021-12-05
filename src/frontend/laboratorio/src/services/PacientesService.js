import Api from "@/services/Api"

const API_USER = ''
const API_URL = '/personas_api/'

export default {
    obtenerMedicosInformantes() {
        return Api().get(API_URL + API_USER + "medicos_informantes/")
    },
    deleteMedicosInformantes(paciente) {
        return Api().delete(API_URL + API_USER + "medicos_informantes/" + paciente.id);
    },
    obtenerMedicosDerivantes() {
        return Api().get(API_URL + API_USER + "medicos_derivantes/")
    },
    deleteMedicosDerivantes(paciente) {
        return Api().delete(API_URL + API_USER + "medicos_derivantes/" + paciente.id);
    },
    editarDerivante(paciente) {
        return Api().put(API_URL + "medicos_derivantes/" + paciente.id + '/', paciente)
    },
    crearMedicoDerivante(paciente) {
        return Api().post(API_URL + API_USER + "medicos_derivantes/", paciente);
    },
    obtenerEmpleados() {
        console.log(API_URL + API_USER + "empleados/")
        return Api().get(API_URL + API_USER + "empleados/")
    },
    crearEmpleado(paciente) {
        return Api().post(API_URL + API_USER + "empleados/", paciente);
    },
    deleteEmpleado(paciente) {
        return Api().delete(API_URL + API_USER + "empleados/" + paciente.id);

    },
    editarEmpleado(paciente) {
        return Api().put(API_URL + "empleados/" + paciente.id + '/', paciente);
    },
    crearMedicoInformante(paciente) {
        return Api().post(API_URL + API_USER + "medicos_informantes/", paciente);
    },

    crearConfigurador(configurador) {
        return Api().post(API_URL + API_USER + "configuradores/", configurador);
    },
    obtenerConfiguradores() {
        return Api().get(API_URL + API_USER + "configuradores/")
    },
    borrarConfigurador(configurador) {
        return Api().delete(API_URL + API_USER + "configuradores/" + configurador.id);
    },
    editarConfigurador(configurador) {
        return Api().put(API_URL + API_USER + "configuradores/" + configurador.id + '/', configurador)
    },
    obtenerConfigurador(id) {
        return Api().get(API_URL + API_USER + "configuradores/" + id)
    },

    crearPaciente(paciente) {
        return Api().post(API_URL + API_USER + "pacientes/", paciente);
    },
    obtenerPacientes() {
        return Api().get(API_URL + API_USER + "pacientes/")
    },
    borrarPaciente(paciente) {
        return Api().delete(API_URL + API_USER + "pacientes/" + paciente.id);
    },
    editarPaciente(paciente) {
        return Api().put(API_URL + API_USER + "pacientes/" + paciente.id + '/', paciente)
    },
    obtenerPaciente(id) {
        return Api().get(API_URL + API_USER + "pacientes/" + id)
    },
    

}