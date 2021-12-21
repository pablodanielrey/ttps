<template>
  <div>
    <div v-if="loading">
      <b-spinner> </b-spinner>
    </div>
    <div v-else>
      <b-navbar toggleable="lg" type="dark" variant="dark">
        <b-navbar-brand>Home</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
        <b-navbar-nav>
          <b-collapse class="ml-auto" id="nav-collapse" is-nav>
            <b-nav-item-dropdown
              text="Pacientes"
              right
              v-if="hasPermisos('add_paciente')"
            >
              <b-dropdown-item
                :to="{ name: 'listaPacientes' }"
                v-if="hasPermisos('view_paciente')"
                >Listar</b-dropdown-item
              >
              <b-dropdown-item
                :to="{ name: 'paciente' }"
                v-if="hasPermisos('add_paciente')"
                >nuevo</b-dropdown-item
              >
            </b-nav-item-dropdown>
            <b-nav-item-dropdown
              text="Empleados"
              right
              v-if="hasPermisos('view_empleado')"
            >
              <b-dropdown-item
                :to="{ name: 'listaEmpleado' }"
                v-if="hasPermisos('view_empleado')"
                >Listar</b-dropdown-item
              >
              <b-dropdown-item
                :to="{ name: 'empleado' }"
                v-if="hasPermisos('add_empleado')"
                >nuevo</b-dropdown-item
              >
            </b-nav-item-dropdown>
            <b-nav-item-dropdown
              text="Obra  Social"
              right
              v-if="hasPermisos('add_obrasocial')"
            >
              <b-dropdown-item
                :to="{ name: 'listaObrasSociales' }"
                v-if="hasPermisos('view_obrasocial')"
                >Listar</b-dropdown-item
              >
              <b-dropdown-item
                :to="{ name: 'obraSocial' }"
                v-if="hasPermisos('add_obrasocial')"
                >nuevo</b-dropdown-item
              >
            </b-nav-item-dropdown>
            <b-nav-item
              :to="{ name: 'editarTemplateConsentimiento' }"
              right
              v-if="hasPermisos('change_templateconsentimiento')"
              >Template Consentimiento</b-nav-item
            >
            <b-nav-item
              :to="{ name: 'editarModoDeTrabajo' }"
              right
              v-if="hasPermisos('view_configuracion')"
              >Modo de Trabajo</b-nav-item
            >
            <b-nav-item-dropdown
              text="Configurador"
              right
              v-if="hasPermisos('add_configurador')"
            >
              <b-dropdown-item
                :to="{ name: 'listaConfiguradores' }"
                v-if="hasPermisos('view_configurador')"
                >Listar</b-dropdown-item
              >
              <b-dropdown-item
                :to="{ name: 'configuradores' }"
                v-if="hasPermisos('add_configurador')"
                >nuevo</b-dropdown-item
              >
            </b-nav-item-dropdown>
            <b-nav-item-dropdown
              text="Medicos informantes"
              right
              v-if="hasPermisos('add_medicoinformante')"
            >
              <b-dropdown-item
                :to="{ name: 'listaMedicoInformante' }"
                v-if="hasPermisos('view_medicoinformante')"
                >Listar</b-dropdown-item
              >
              <b-dropdown-item
                :to="{ name: 'medicoInformante' }"
                v-if="hasPermisos('add_medicoinformante')"
                >nuevo</b-dropdown-item
              >
            </b-nav-item-dropdown>
            <b-nav-item-dropdown
              text="Medicos derivantes"
              right
              v-if="hasPermisos('view_medicoderivante')"
            >
              <b-dropdown-item
                :to="{ name: 'listaDerivante' }"
                v-if="hasPermisos('view_medicoderivante')"
                >Listar</b-dropdown-item
              >
              <b-dropdown-item
                :to="{ name: 'medicoDerivante' }"
                v-if="hasPermisos('add_medicoderivante')"
                >nuevo</b-dropdown-item
              >
            </b-nav-item-dropdown>
            <b-nav-item-dropdown text="Resultados Informe" right     v-if="hasPermisos('view_esperandointerpretacionderesultados')">
              <b-dropdown-item :to="{ name: 'listaEstudiosEsperandoInforme' }"
               v-if="hasPermisos('view_esperandointerpretacionderesultados')"
                >Listar</b-dropdown-item
              >
            </b-nav-item-dropdown>

            <b-nav-item-dropdown
              v-if="hasPermisos('view_estudio') && hasRol('Empleados')"
              text="Estudios"
              right
            >
              <b-dropdown-item
                :to="{ name: 'listaEstudios' }"
                v-if="hasPermisos('view_estudio')"
                >Listar</b-dropdown-item
              >
              <b-dropdown-item
                :to="{ name: 'nuevoEstudio' }"
                v-if="hasPermisos('add_estudio')  && hasRol('Pacientes')"
                >Nuevo</b-dropdown-item
              >
            </b-nav-item-dropdown>
             <b-nav-item-dropdown
              v-if="hasPermisos('view_estudio') "
              text="Mis estudios"
              right
            >
       
              <b-dropdown-item
                :to="{ name: 'listaEstudios' }"
                v-if="hasPermisos('view_estudio') "
                >Listar</b-dropdown-item
              >
           
            </b-nav-item-dropdown>

            <b-nav-item-dropdown
              text="Lotes"
              right
              v-if="hasPermisos('view_lote')"
            >
              <b-dropdown-item
                :to="{ name: 'cargarResultadoLote' }"
                v-if="hasPermisos('view_lote')"
                >Listar</b-dropdown-item
              >
              <b-dropdown-item
                :to="{ name: 'crearLote' }"
                v-if="hasPermisos('add_lote')"
                >Nuevo</b-dropdown-item
              >
            </b-nav-item-dropdown>
            <b-nav-item-dropdown text="Turnos ocupados" right  v-if="hasPermisos('view_turnoconfirmado')" >
              <b-dropdown-item :to="{ name: 'turnosOcupados' }"
              v-if="hasPermisos('view_turnoconfirmado')"
                >Listar</b-dropdown-item
              >
            </b-nav-item-dropdown>
            <b-nav-item :to="{ name: 'estadisticas' }" v-if="hasRol('Empleados')">Estadisticas</b-nav-item>

            <b-nav-item-dropdown
              text="Liquidaciones"
              v-if="hasPermisos('add_liquidacion')"
              right
            >
              <b-dropdown-item
                :to="{ name: 'liquidacionesEstudios' }"
                v-if="hasPermisos('add_liquidacion')"
                >Nueva</b-dropdown-item
              >
              <b-dropdown-item :to="{ name: 'liquidadoesEstudios' }"
                >Liquidados</b-dropdown-item
              >
            </b-nav-item-dropdown>

            <b-nav-item-dropdown
              text="Turnos "
              v-if="hasPermisos('change_parametrodeturnos')"
            >
              <b-dropdown-item
                :to="{ name: 'configurarFechasSinTurnos' }"
                v-if="hasPermisos('change_parametrodeturnos')"
                >Configurar turnos</b-dropdown-item
              >
                  <b-dropdown-item
                :to="{ name: 'configurarTurnos' }"
                v-if="hasPermisos('change_configuracion')"
                >Configurar rango fechas</b-dropdown-item
              >
            </b-nav-item-dropdown>
            -

            <b-nav-item @click="cerarrSesion()" right>Cerrar sesion</b-nav-item>
          </b-collapse>
        </b-navbar-nav>
      </b-navbar>
      <br />
    </div>
  </div>
</template>

<script>
import { mapGetters,mapActions} from "vuex";
export default {
  components: {},
  props: {},
  data() {
    return {
      loading: false,
    
    };
  },
  computed: {
    ...mapGetters(["hasPermisos","hasRol"]),

  },
  methods: {
           ...mapActions( ["LOGOUT_REQUEST"]),
    cerarrSesion() {
       this.LOGOUT_REQUEST().then(() => {
        this.$router.push({name: "Login"}).catch({});
      });
      location.reload();
      
    },

  },

  mounted() {

  },
};
</script>

<style>
</style>