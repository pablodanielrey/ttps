<template>
  <b-container>
    <br />
    <h4>Listado de Pacientes</h4>

    <b-col lg="4" class="my-1">
      <b-input-group size="sm">
        <b-form-input
          id="filter-input"
          v-model="filter"
          type="search"
          placeholder="Buscar en el listado"
        ></b-form-input>
        <b-input-group-append>
          <b-button :disabled="!filter" @click="filter = ''">Buscar</b-button>
        </b-input-group-append>
      </b-input-group>
    </b-col>
    <b-table
      :items="items"
      :fields="fields"
      :filter="filter"
      :current-page="currentPage"
      :per-page="perPage"
      @filtered="onFiltered"
    >
      <template v-slot:cell(acciones)="row">
     <!--    <b-button
          title="Editar paciente"
          variant="outline-primary"
          @click="editarPaciente(row.item)"
        >
          <b-icon icon="arrow-clockwise" aria-hidden="true"></b-icon
        ></b-button> -->
        <b-button
          title="Ver historia clinica"
          variant="outline-primary"
          @click="verHistoria(row.item.historia_clinica)"
        >
          <b-icon icon="eye" aria-hidden="true"></b-icon
        ></b-button>
          <b-button
            @click="borrarPaciente(row.item)"
            variant="outline-danger"
            title="Eliminar"
          >
            <b-icon icon="trash" variant="danger"> </b-icon>
          </b-button>
      </template>
    </b-table>

    <b-row>
      <b-col md="1">
        <b-form-select
          id="per-page-select"
          v-model="perPage"
          :options="pageOptions"
          size="sm"
        ></b-form-select>
      </b-col>
      <b-col class="text-center">
        <b-pagination
          v-model="currentPage"
          :total-rows="totalRows"
          :per-page="perPage"
        ></b-pagination>
      </b-col>
      <br />
    </b-row>
    <div>
      <b-modal ref="modalHistoriaCLinica" ok-only title="Historia clinica">
        <div v-html="this.historiaClinica "> </div>
     
      
      </b-modal>
    </div>
  </b-container>
</template>


<script>
import PacientesService from "@/services/PacientesService.js";
import axios from "axios";
export default {
  name: "ListaPacientes",

  components: {},
  props: {},

  data() {
    return {
      historiaClinica: null,
      perPage: 10,
      pageOptions: [10, 15,20],
      filter: null,
      currentPage: 1,
      totalRows: 1,
      fields: [
        { key: "apellido", label: "Apellido", class: "text-center p2" },
        { key: "nombre", label: "Nombre", class: "text-center p2" },
        { key: "dni", label: "DNI", class: "text-center p2" },
        {
          key: "fecha_nacimiento",
          label: "Fecha Nacimiento",
          class: "text-center p2",
        },
        { key: "telefono", label: "Telefono", class: "text-center p2" },
        { key: "acciones", label: "Acciones", class: "text-center p2" },
      ],
      items: [],
    };
  },

  created() {},
  methods: {
    async borrarPaciente(paciente){ 
         try {
        let response = await PacientesService.borrarPaciente(paciente);
        console.log(response)
       this.$root.$bvToast.toast("Se elimino el paciente", {
              title: "Atencion!",
              toaster: "b-toaster-top-center",
              solid: true,
              variant: "success",
            });
        this.obtenerPacientes()
     
      } catch (err) {
        console.log(err);
           this.$root.$bvToast.toast("No se pudo eliminar el paciente", {
              title: "Atencion!",
              toaster: "b-toaster-top-center",
              solid: true,
              variant: "danger",
            });
      }

    },
    async obtenerPacientes() {
      try {
        let response = await PacientesService.obtenerPacientes();
        this.items = response.data;
      } catch (err) {
        console.log(err);
      }
    },
    onFiltered(filteredItems) {
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    editarPaciente(paciente) {
      this.$router.push({
        name: "paciente",
        params: { paciente: paciente, editar: true },
      });
    },
    verHistoria(historiaClinica) {
      this.historiaClinica = historiaClinica;
         this.$refs["modalHistoriaCLinica"].show();
    },
  },
  mounted() {
    axios
      .all([this.obtenerPacientes()])
      .then(() => {
        this.totalRows = this.items.length;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>


<style>
</style>