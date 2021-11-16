import Api from "@/services/Api"

const API_URL = '/lotes_api/'

export default {
    obtenerListaEstudiosEsperandoProcesamiento() {
        return Api().get(API_URL + "estudios/")
    },
    crearLote(estudios){
        return Api().post(API_URL  + "lotes/", estudios);
    },
    obtenerLotes(){
        return Api().get(API_URL + "lotes/")
    },
    cargarResultadoLote(id,datos){
        console.log(API_URL + "lotes/"+id,datos +'/')
        return Api().put(API_URL + "lotes/"+id +'/',datos )
    }

    
  
    
}