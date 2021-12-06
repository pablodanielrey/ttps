<template>
  <b-container fluid>
    <div v-if="loading">
      <b-spinner> </b-spinner>

      <h4>Listado de Estudios</h4>
    </div>
    <div v-else>
      <b-col lg="4" class="my-1">
        <b-input-group size="sm">
          <b-form-input
            id="filter-input"
            v-model="filter"
            type="search"
            placeholder="Buscar por nombre de paciente,medico derivante u diagnostico"
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
        <template v-slot:cell(estados)="row">
          {{ obtenerUltimoEstado(row.item) }}
        </template>
        <template v-slot:cell(acciones)="row">
        
          <b-button
            @click="siguienteEstado(row.item)"
            variant="outline-white"
            title="Cargar informe"
          >
            <b-icon icon="arrow-right-square" variant="info"> </b-icon>
          </b-button>
        </template>
      </b-table>

      <b-row>
        <b-col>
          <b-form-select
            style="width: 150px"
            id="per-page-select"
            v-model="perPage"
            :options="pageOptions"
            size="sm"
          ></b-form-select>
        </b-col>
        <b-col>
          <b-pagination
            v-model="currentPage"
            :total-rows="totalRows"
            :per-page="perPage"
          ></b-pagination>
        </b-col>
        <br />
      </b-row>
    </div>
  </b-container>
</template>


<script>
import EstudiosService from "@/services/EstudiosService.js";
import axios from "axios";
export default {
  name: "listaEstudios",

  components: {},
  props: {},

  data() {
    return {
      perPage: 10,
      pageOptions: [4, 10, 15],
      filter: null,
      currentPage: 1,
      loading: true,
      totalRows: 1,
      fields: [
        { key: "paciente.nombre", label: "Nombre", class: "text-center p2" },
        {
          key: "paciente.apellido",
          label: "Apellido",
          class: "text-center p2",
        },
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
        { key: "estados", label: "Estado", class: "text-center p2" },

        { key: "acciones", label: "Acciones", class: "text-center p2" },
      ],
      items: [],
    };
  },

  created() {},
  methods: {
    obtenerUltimoEstado(estudio) {
      let nameEstado = estudio.ultimo_estado.resourcetype;
      nameEstado = nameEstado.replace(/([a-z])([A-Z])/g, "$1 $2");
      nameEstado = nameEstado.replace(/([A-Z])([A-Z][a-z])/g, "$1 $2");
      return nameEstado;
    },
    async obtenerListaEstudios() {
      try {
        let response = await EstudiosService.obtenerListaEstudiosParaInformes();
        this.items = response.data;
        console.log(response)
      console.log("estudios:"+ this.items)
      } catch (err) {
        console.log(err);
      }
    },
    onFiltered(filteredItems) {
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    detalleEstudio(estudio) {
      console.log(estudio);
      this.$router.push({
        name: "detalleDeEstudio",
        params: {
          estudio: estudio,
        },
      });
    },
    siguienteEstado(estudio) {
      
      //let ultimoEstado = estudio.estados[estudio.estados.length - 1];
      this.$router.push({
        name: "EsperandoInterpretacionDeResultadosInformante",
        params: {
          estudio: estudio,
        },
      });
    },
  },
  mounted() {
    axios
      .all([this.obtenerListaEstudios()])
      .then(() => {
        this.totalRows = this.items.length;
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