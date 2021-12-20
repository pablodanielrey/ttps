<template>
  <b-container fluid>
    <div v-if="loading">
      <b-spinner> </b-spinner>
      <h4> Estudios liquidados</h4>
    </div>
    <div v-else>
      <h4>Estudios liquidados</h4>
      <br />
   <br />
      <b-table
        show-empty
        empty-text="El sistema no posee estudios a liquidar"
        :items="items"
        :fields="fields"
        :filter="filter"
        :current-page="currentPage"
        :per-page="perPage"
        responsive="sm"
      >
        <template v-slot:cell(estados)="row">
          {{ obtenerUltimoEstado(row.item) }}
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
import LiquidacionesService from "@/services/LiquidacionesService.js";
import axios from "axios";
export default {
  data() {
    return {
      perPage: 10,
      pageOptions: [10, 25, 40],
      filter: null,
      currentPage: 1,
      loading: true,
      totalRows: 1,
      fields: [
        {
          key: "paciente.nombre",
          label: "Nombre",
          class: "text-center p2",
        },
        {
          key: "paciente.apellido",
          label: "Apellido",
          class: "text-center p2",
        },

        {
          key: "diagnostico.nombre",
          label: "Diagnostico",
          class: "text-center p2",
        },
        {
          key: "tipo.nombre",
          label: "Tipo Estudio",
          class: "text-center p2",
        },
        {
          key: "estados",
          label: "Estado",
          class: "text-center p2",
        },
     
      ],
      items: [],
    };
  },
  methods: {
   


    obtenerUltimoEstado(estudio) {
      let nameEstado = estudio.ultimo_estado.resourcetype;
      nameEstado = nameEstado.replace(/([a-z])([A-Z])/g, "$1 $2");
      nameEstado = nameEstado.replace(/([A-Z])([A-Z][a-z])/g, "$1 $2");
      return nameEstado;
    },
    async obtenerEstudiosLiquidados() {
      try {
        let response = await LiquidacionesService.obtenerEstudiosLiquidados();
        this.items = response.data;
      
      } catch (err) {
        console.log(err);
      }
    },
  },
  mounted() {
    axios
      .all([this.obtenerEstudiosLiquidados()])
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