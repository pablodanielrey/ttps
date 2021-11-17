<template>
  <div>
    <div v-if="loading">
      <b-spinner> </b-spinner>
    </div>
    <div v-else>
      <b-navbar type="dark" variant="dark">
        <b-navbar-nav>
          <b-collapse class="ml-auto" id="nav-collapse" is-nav>
            <b-nav-item :to="{ name: '' }">Home</b-nav-item>
            <b-nav-item-dropdown text="Pacientes" right v-if="this.permisos == 'Administradores' " >
              <b-dropdown-item :to="{ name: 'listaPacientes' }"
                >Listar</b-dropdown-item
              >
              <b-dropdown-item :to="{ name: 'paciente' }"
                >nuevo</b-dropdown-item
              >
            </b-nav-item-dropdown>
             <b-nav-item-dropdown v-if="this.permisos == 'Configuradores' " text="Obra  Social" right>
              <b-dropdown-item :to="{ name: 'listaObrasSociales' }"
                >Listar</b-dropdown-item
              >
              <b-dropdown-item :to="{ name: 'obraSocial' }"
                >nuevo</b-dropdown-item
              >
            </b-nav-item-dropdown>
             <b-nav-item-dropdown v-if="this.permisos == 'Administradores' " text="Configurador" right>
              <b-dropdown-item :to="{ name: 'listaConfiguradores' }"
                >Listar</b-dropdown-item
              >
              <b-dropdown-item :to="{ name: 'configuradores' }"
                >nuevo</b-dropdown-item
              >
            </b-nav-item-dropdown>
              <b-nav-item-dropdown v-if="this.permisos == 'Empleados' " text="Medicos informantes" right>
              <b-dropdown-item :to="{ name: 'listaMedicoInformante' }"
                >Listar</b-dropdown-item
              >
              <b-dropdown-item :to="{ name: 'medicoInformante' }"
                >nuevo</b-dropdown-item
              >
            </b-nav-item-dropdown>
             <b-nav-item-dropdown text="Resultados Informe" right v-if="this.permisos == 'Médicos_Informantes' ">
              <b-dropdown-item :to="{ name: 'listaEstudiosEsperandoInforme' }"
                >Listar</b-dropdown-item
              >
             
            </b-nav-item-dropdown>

            <b-nav-item-dropdown  v-if="this.permisos == 'Empleados'"   text="Estudios" right>
              <b-dropdown-item :to="{ name: 'listaEstudios' }"
                >Listar</b-dropdown-item
              >
              <b-dropdown-item :to="{ name: 'nuevoEstudio' }"
                >Nuevo</b-dropdown-item
              >
            </b-nav-item-dropdown>

            <b-nav-item-dropdown  v-if="this.permisos == 'Empleados'" text="Lotes" right>
              <b-dropdown-item :to="{ name: 'cargarResultadoLote' }"
                >Listar</b-dropdown-item
              >
              <b-dropdown-item :to="{ name: 'crearLote' }"
                >Nuevo</b-dropdown-item
              >
            </b-nav-item-dropdown>
            <b-nav-item-dropdown   v-if="this.permisos == 'Empleados'" text="Turnos ocupados" right>
              <b-dropdown-item :to="{ name: 'turnosOcupados' }"
                >Listar</b-dropdown-item
              >
            </b-nav-item-dropdown>
          <!--   <b-nav-item-dropdown   v-if="this.permisos == 'Configuradores'" text="Turnos " >
              <b-dropdown-item :to="{ name: 'configurarTurnos' }"
                >Configurar turnos</b-dropdown-item
              >
            </b-nav-item-dropdown> -->

            <b-nav-item @click="cerarrSesion()" right>Cerrar sesion</b-nav-item>
          </b-collapse>
        </b-navbar-nav>
      </b-navbar>
      <br />
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  components: {},
  props: {},
  data() {
    return {
      loading: true,
      permisos: null,
    };
  },
  computed: {},
  methods: {
  
    cerarrSesion() {
      try {
        window.localStorage.removeItem("credenciales");
        this.$router.push({
          name: "Login",
        });
      } catch (error) {
        console.log(error);
      }
    },
    obtenerPermisos() {
      this.permisos = window.localStorage.getItem("permisos");
      console.log(this.permisos);
    },
  },

  mounted() {
    axios
      .all([this.obtenerPermisos()])
      .then(() => {
        this.loading = false;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style>
</style>