
import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)
export default new Vuex.Store({
  state: {
    permisos: localStorage.getItem('permisos') ||  null,


   },
  mutations: {

    setPermisos(state, payload) {
        state.permisos = payload
        localStorage.setItem("permisos", JSON.stringify(payload))
    },

    clearToken(state) {
        state.token = null
        localStorage.removeItem("credenciales")      
        localStorage.removeItem("permisos")
        
    },
  },
  getters: {
    hasPermisos: (state) => (permiso) => {      
        if(state.permisos == null){
            return false
        }
        return JSON.parse(state.permisos.includes(permiso)) ;
    }, 
   },
    actions: {
        LOGOUT_REQUEST: ({commit}) => {               
            commit('clearToken');
            
        },
    }


})