import axios from 'axios'

import Api from "@/services/Api"


const API_URL = '/login_api/'
export default {
    login(usuario, clave) {
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
        if (window.localStorage.getItem('credenciales') == undefined) {
            let instance = axios.create({
                baseURL: process.env.VUE_APP_API_URL,
                auth: {
                    'username': username,
                    'password': password
                }
            })
            let response = await instance.get(API_URL  + "login/");
            // response.token
            // response.roles
            window.localStorage.setItem('credenciales', JSON.stringify({
                'usuario': username,
                'clave': password
            }));
            window.localStorage.setItem('permisos', response.data.roles )
        } 
    },
    cerrarSesion(){
        window.localStorage.removeItem('credenciales');
    }


}


//'Administradores' a configurador a empleado
//'Empleados' buscador de pacientes  - cancelar turno - listar turno ocupados  ESTA 
//'Configuradores' configura turno y rango horario  1  -   os abm ESTA - abm de entidades basicas y de medicos informantes
//'Pacientes'  
//'Médicos_Informantes' completa ultimo estado ESTA 
//'Médicos_Derivantes'

// lista de pacientes - http://localhost:8000/personas_api/pacientes/
// busqueda de pacientes por un termino - http://localhost:8000/personas_api/pacientes/buscar/?q=pab
// lista de medicos derivantes - http://localhost:8000/personas_api/medicos_derivantes/
// busqueda de medicos derivantes - http://localhost:8000/personas_api/medicos_derivantes/buscar/?q=med
// lista de medicos derivantes - http://localhost:8000/personas_api/medicos_informantes/
// busqueda de medicos derivantes - http://localhost:8000/personas_api/medicos_informantes/buscar/?q=med
// buscar estudios - http://localhost:8000/estudio_api/estudios/buscar/?q=122

