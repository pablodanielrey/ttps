import axios from 'axios'

import Api from "@/services/Api"


const API_URL = '/login_api/'
export default {
    login(usuario, clave) {
        console.log('almacenando ' + usuario + ' y su clave')
        window.localStorage.setItem('credenciales', JSON.stringify({
            'usuario': usuario,
            'clave': clave
        }));
                return Api().get(API_URL  + "login/", {params: { username:usuario, password: clave }});

    },
    getApiToken() {
        let credenciales = JSON.parse(window.localStorage.getItem('credenciales'));       
        return credenciales
    },
   async  login_api(username, password) {
        console.log(window.localStorage.getItem('credenciales') == undefined)
        if (window.localStorage.getItem('credenciales') == undefined) {
            let instance = axios.create({
                baseURL: process.env.VUE_APP_API_URL,
                auth: {
                    'username': username,
                    'password': password
                }
            })
            let response = await instance.get(API_URL  + "login/");
            console.log(response);
            // response.token
            // response.roles
            window.localStorage.setItem('credenciales', JSON.stringify({
                'usuario': username,
                'clave': password
            }));
        } 
    }

}


//'Administradores' a configurador a empleado
//'Empleados' buscador de pacientes  - cancelar turno - listar turno ocupados   
//'Configuradores' configura turno y rango horario  1  -   os abm - abm de entidades basicas y de medicos informantes
//'Pacientes'  
//'Médicos_Informantes' completa ultimo estado
//'Médicos_Derivantes'