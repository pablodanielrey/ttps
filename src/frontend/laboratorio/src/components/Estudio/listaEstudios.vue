<template>
  <b-container>
    <br />
    <h4>Listado de Estudios</h4>

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
        <div v-if="row.item.estados[0] != null">
          <b-button
            title="Descargar Presupuesto"
            variant="outline-success"
            download="presupuesto.pdf"
            :href="row.item.estados[0].presupuesto"
          >
            <b-icon icon="download" aria-hidden="true"></b-icon
          ></b-button>
             <b-button   
             @click="seleccionTurno(row.item.id)"        
          >
          seleccionar turno
          ></b-button>
        </div>
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
  </b-container>
</template>


<script>
import EstudiosService from "@/services/EstudiosService.js";
import axios from "axios";
export default {
  name: "ListaPacientes",

  components: {},
  props: {},

  data() {
    return {
      perPage: 4,
      pageOptions: [4, 10, 15],
      filter: null,
      currentPage: 1,
      totalRows: 1,
      fields: [
        { key: "paciente.nombre", label: "Paciente", class: "text-center p2" },
        {
          key: "medico_derivante.apellido",
          label: "Medico derivante",
          class: "text-center p2",
        },
        {
          key: "diagnostico.nombre",
          label: "Diagnostico",
          class: "text-center p2",
        },
        { key: "tipo.nombre", label: "Tipo Estudio", class: "text-center p2" },
        {
          key: "estados[0].resourcetype",
          label: "Estado",
          class: "text-center p2",
        },
        { key: "acciones", label: "Acciones", class: "text-center p2" },
      ],
      items: [],
    };
  },

  created() {
    console.log(this.paciente);
  },
  methods: {
    async obtenerListaEstudios() {
      try {
        let response = await EstudiosService.obtenerListaEstudios();
        this.items = response.data;
        console.log(this.items);
      } catch (err) {
        console.log(err);
      }
    },
    onFiltered(filteredItems) {
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    seleccionTurno(estudio){
         this.$router.push({ name: 'seleccionTurno', params: { estudio:estudio} })
    }
  },
  mounted() {
    axios
      .all([this.obtenerListaEstudios()])
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