import Api from "@/services/Api"

const API_USER = ''
const API_URL = '/estudio_api/'

export default {
    obtenerTemplateConsentimiento() {
        return Api().get(API_URL + API_USER + "templateConsentimiento/")
    },
    editarTemplateConsentimiento(template) {
        let datos = {
            'consentimiento': template
        }
        return Api().post(API_URL + "templateConsentimiento/", datos)
    },
}