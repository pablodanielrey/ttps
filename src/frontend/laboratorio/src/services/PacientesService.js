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
    borrarPaciente(paciente) {
        return Api().delete(API_URL + API_USER + "pacientes/" + paciente.id);
    },
    crearConfigurador(paciente) {
        return Api().post(API_URL + API_USER + "configuradores/", paciente);
    },
    obtenerConfiguradores() {
        return Api().get(API_URL + API_USER + "configuradores/")
    },
    deleteConfigurador(paciente) {
        return Api().delete(API_URL + API_USER + "configuradores/" + paciente.id);
    },
    editarConfigurador(config) {

        return Api().put(API_URL + "configuradores/" + config.id + '/', config)
    },
    editarPaciente(paciente) {
        return Api().put(API_URL + "pacientes/" + paciente.id + '/', paciente)
    },



}