<template>
<div>
  <b-navbar type="dark" variant="dark">
    <b-navbar-nav>
      <b-nav-item @click="home()">Home</b-nav-item>   

      <b-nav-item-dropdown text="User" right>
        <b-dropdown-item  :to="{ name: 'perfil' }">Mi cuenta</b-dropdown-item>      
      </b-nav-item-dropdown>
      
        <b-navbar-nav class="">          
          <b-nav-item-dropdown right>
            <template #button-content>
              <b-icon icon="person-fill"></b-icon>
            </template>
           
            <b-dropdown-item
              :to="{ name: 'login' }"
              >Iniciar sesion</b-dropdown-item
            >
            <b-dropdown-item
              :to="{ name: 'Registrarse' }"
              >Crear cuenta</b-dropdown-item
            >
        
          </b-nav-item-dropdown>
        </b-navbar-nav>
    </b-navbar-nav>
  </b-navbar>
</div>
</template>
<script>

export default {
  name: "Index",
  props: {
   
  },
  components: {

  },

  data() {
    return {
     
    };
  },
  created() {
  },

  mounted() {},
   methods: {
     verCuenta(){
         this.$router.push({ name: "perfil",              
      });
     },
      home(){
         this.$router.push({ name: "Home",              
      });
     }
   }
  
 
};
</script>

<style>
</style>