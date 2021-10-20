import axios from 'axios'

import LoginService from '@/services/LoginService'

export default () => {

    let credenciales = LoginService.getApiToken();
    let instance = axios.create({
        baseURL: process.env.VUE_APP_API_URL,
        headers: {
        },
        auth: {
            'username': credenciales.usuario,
            'password': credenciales.clave
        }
    })


    

    // por ahora no usamos interceptores
    // instance.interceptors.response.use(
    //     (response) => {
    //         return response
    //     },
    //     function (error) {
    //         let originalRequest = error.config
    //         if (error.response.status === 401 || error.response.status === 403 && !originalRequest._retry) {
    //             originalRequest._retry = true

    //             store.dispatch("storeUser/LOGOUT_REQUEST").then(() => {
    //                 store.commit('storeUser/addToast',{
    //                     'message': error.response.data.message || 'error',
    //                     'variant': 'danger'  
    //                 })
    //                 router.push("/");
    //             })
    //         }
    //         // Do something with response error
    //         return Promise.reject(error)
    //     })


    return instance


}