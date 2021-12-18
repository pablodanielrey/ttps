import Api from "@/services/Api"
import axios from 'axios'

const API_USER = ''
const API_URL = '/personas_api/'

export default {
    registrarPaciente(usuario){
        console.log(process.env.VUE_APP_API_URL + API_URL  + "registro/", usuario)
        return axios.post(process.env.VUE_APP_API_URL + API_URL  + "registro/", usuario);
    },
    obtenerMedicosInformantes() {
        console.log(process.env.VUE_APP_API_URL + API_URL  + "medicos_informantes/")
        return Api().get(API_URL + API_USER + "medicos_informantes/")
    },
    deleteMedicosInformantes(dato) {
        return Api().delete(API_URL + API_USER + "medicos_informantes/" + dato.id);
    },
    crearMedicoInformante(dato) {
        return Api().post(API_URL + API_USER + "medicos_informantes/", dato);
    },
    editarMedicoInformante(dato) {
        return Api().put(API_URL + "medicos_informantes/" + dato.id + '/', dato)
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
        return Api().get(API_URL + API_USER + "empleados/")
    },
    crearEmpleado(empleado) {
        return Api().post(API_URL + API_USER + "empleados/", empleado);
    },
    deleteEmpleado(empleado) {
        return Api().delete(API_URL + API_USER + "empleados/" + empleado.id);

    },
    editarEmpleado(empleado) {
        return Api().put(API_URL + "empleados/" + empleado.id + '/', empleado);
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