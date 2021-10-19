
import Api from "@/services/Api"


export default {
    obtenerPacientes() {
        console.log("/personas")
        return Api().get( "/personas")
    }
}