import axios from 'axios'
import store from '@/store'
import router from '../router'


export default () => {


    //console.log(process.env);

    let instance = axios.create({
        baseURL: process.env.VUE_APP_API_URL,
        headers: {
        }
    })

    instance.interceptors.response.use(
        (response) => {
            return response
        },
        function (error) {
            let originalRequest = error.config
            if (error.response.status === 401 || error.response.status === 403 && !originalRequest._retry) {
                originalRequest._retry = true

                store.dispatch("storeUser/LOGOUT_REQUEST").then(() => {
                    store.commit('storeUser/addToast',{
                        'message': error.response.data.message || 'error',
                        'variant': 'danger'  
                    })
                    router.push("/");
                })
            }
            // Do something with response error
            return Promise.reject(error)
        })


    return instance


}