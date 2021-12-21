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
    },
    cancelarTurno(idTurno){
        return Api().delete(API_URL + API_USER + "turnos_confirmados/" + idTurno);
    },
    fechaSinTurnos(fecha){
        return Api().post(API_URL + API_USER + "fechas_sin_turnos/",fecha)
    },
    obtenerFechasSinTurnos(){
        return Api().get(API_URL + API_USER + "fechas_sin_turnos/")
    },
    eliminarFechaExcepcion(id){
        return Api().delete(API_URL + API_USER + "fechas_sin_turnos/" + id);
    },
    agregarRangoTurnos(turnos){
        return Api().post(API_URL + API_USER + "parametro_turnos/",turnos)        
    },
    obtenerRangos(){
        return Api().get(API_URL + API_USER + "parametro_turnos/")

    },
    eliminarRango(id){
        return Api().delete(API_URL + API_USER + "parametro_turnos/" + id);

    }
  
    
}