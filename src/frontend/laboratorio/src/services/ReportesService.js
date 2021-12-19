import Api from "@/services/Api"

const API_URL = '/reportes_api/'
const API_USER = ''
export default {
    obtenerEstudiosPorMesAño(){        
        return Api().get(API_URL + API_USER + "estudios_por_mes" )
    },
    obtenerEstudiosPorTipo(){       
        return Api().get(API_URL + API_USER + "estudios_por_tipo" )
    },
    demoraEstudiosProcesamiento(){       
        return Api().get(API_URL + API_USER + "demora_promedio_procesamiento" )
    },
    
    
  
    
}