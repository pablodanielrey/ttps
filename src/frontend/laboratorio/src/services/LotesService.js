import Api from "@/services/Api"

const API_URL = '/lotes/'

export default {
    obtenerListaEstudiosEsperandoProcesamiento() {
        return Api().get(API_URL + "estudios/")
    },
    crearLote(estudios){
        return Api().post(API_URL  + "lotes/", estudios);
    },
    obtenerLotes(){
        return Api().get(API_URL + "lotes/")
    }

    
  
    
}