import Api from "@/services/Api"
import axios from 'axios'
const API_USER = ''
const API_URL = '/estudio_api/'

export default {
    obtenerTemplateConsentimiento() {
        return Api().get(API_URL + API_USER + "templateConsentimiento/valido")
    },
    obtenerTemplateConsentimiento2(){
        let credenciales = JSON.parse(window.localStorage.getItem('credenciales'));       
        axios({
            method: 'get',
            url: API_URL + API_USER + "templateConsentimiento/valido",
            responseType: 'arraybuffer',
            auth: {
                'username': credenciales.usuario,
                'password': credenciales.clave
            }
           
          }).then(function(response) {
            let blob = new Blob([response.data], { type: 'application/pdf' })
            let link = document.createElement('a')
            link.href = window.URL.createObjectURL(blob)
            link.download = 'Report.pdf'
            link.click()
          })
    },
    editarTemplateConsentimiento(template) {
        let datos = {
            'consentimiento': template
        }
        return Api().post(API_URL + "templateConsentimiento/", datos)
    },
}