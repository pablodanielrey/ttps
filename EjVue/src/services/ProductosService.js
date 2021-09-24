import Api from '@/services/Api'
const API_USER = "";
const API_URL = "/";

export default {

    getProductos(credentials) {    
        return Api().get(API_URL + API_USER + "destacados", credentials)
    },
  
}