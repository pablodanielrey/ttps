import Api from "@/services/Api"

const API_USER = ''
const API_URL = '/turnos_api/'

export default {
    obtenerTurnos(rango) {
        return Api().get(API_URL + API_USER + "turnos_disponibles/", {params: { inicio: rango.inicio, fin: rango.fin }})
    },
    confirmarTurno(turno){
        return Api().post(API_URL + API_USER + "turnos_confirmados/",turno)
    },
    obtenerTurnosOcupados(){
        return Api().get(API_URL + API_USER + "turnos_confirmados/")

    }
  
    
}