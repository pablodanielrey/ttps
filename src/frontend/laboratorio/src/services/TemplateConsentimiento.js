import Api from "@/services/Api"

const API_USER = ''
const API_URL = '/personas_api/'

export default {
    obtenerTemplateConsentimiento() {
        return Api().get(API_URL + API_USER + "templateConsentimiento/")
    },
    editarTemplateConsentimiento(template) {
        return Api().put(API_URL + "templateConsentimiento/" + template.id + '/', template)
    },
}