
import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)
export default new Vuex.Store({
  state: {
    permisos: localStorage.getItem('permisos') ||  null,
    rol: localStorage.getItem('rol') ||  null,

   },
  mutations: {

    setPermisos(state, payload) {
        state.permisos = payload
        localStorage.setItem("permisos", JSON.stringify(payload))
    },
    setRol(state, payload){
        state.rol = payload
        localStorage.setItem("rol", JSON.stringify(payload))
    },

    clearToken(state) {
        state.token = null
        localStorage.removeItem("credenciales")      
        localStorage.removeItem("permisos")
        localStorage.removeItem("rol") 
    },
  },
  getters: {
    hasPermisos: (state) => (permiso) => {      
        if(state.permisos == null){
            return false
        }
        return JSON.parse(state.permisos.includes(permiso)) ;
    }, 
    hasRol: (state) => (rol) => {      
        if(state.rol == null){
            return false
        }
        return JSON.parse(state.rol.includes(rol)) ;
    }, 
   },
    actions: {
        LOGOUT_REQUEST: ({commit}) => {               
            commit('clearToken');
            
        },
    }


})