<template>
  <b-container>

 <b-card header=" Listado de Estudios esperando Lote para procesamiento biotecnológico">
    <b-table
      :items="items"
      :fields="fields"
      :filter="filter"
      :current-page="currentPage"
      :per-page="perPage"
      @filtered="onFiltered"
      selectable
    >
      <template v-slot:cell(acciones)>
        <b-button
          title="Descargar Presupuesto"
          variant="outline-success"
          download="presupuesto.pdf"
        >
          <b-icon icon="eye" aria-hidden="true"></b-icon
        ></b-button>
        <!-- <b-button @click="seleccionTurno(row.item.id)">
            seleccionar turno
          </b-button> -->
      </template>
    </b-table>

 <b-row class="pb-2">
      <b-col class="text-center pt-3">
        <b-button   variant="success"
          >Crear Lote
        </b-button>
  
      </b-col>
    </b-row>
     </b-card>
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
      perPage: 10,
      pageOptions: [4, 10, 15],
      filter: null,
      currentPage: 1,
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

        { key: "fecha_alta", label: "Fecha Extraccion", class: "text-center p2" },
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
        this.items.sort(function (a, b) {
          if (a.fecha_alta < b.fecha_alta){
            return -1
          }
          if (a.fecha_alta > b.fecha_alta){
            return 1
          }
          
          
        });
      } catch (err) {
        console.log(err);
      }
    },
    onFiltered(filteredItems) {
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    seleccionTurno(estudio) {
      this.$router.push({
        name: "seleccionTurno",
        params: { estudio: estudio },
      });
    },
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