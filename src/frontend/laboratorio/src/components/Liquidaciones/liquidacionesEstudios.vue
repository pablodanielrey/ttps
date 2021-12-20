<template>
  <b-container fluid>
    <div v-if="loading">
      <b-spinner> </b-spinner>
      <h4>Liquidaciones de Estudios</h4>
    </div>
    <div v-else>
      <h4>Liquidaciones de Estudios</h4>
      <br />
      <b-button variant="outline-success" @click="liquidarEstudios()"
        >Liquidar estudios</b-button
      ><br />
      <b-table
        show-empty
        empty-text="El sistema no posee estudios a liquidar"
        :items="items"
        :fields="fields"
        :filter="filter"
        :current-page="currentPage"
        :per-page="perPage"
        :select-mode="selectMode"
        responsive="sm"
        ref="selectableTable"
        selectable
        @row-selected="onRowSelected"
      >
        <template v-slot:cell(estados)="row">
          {{ obtenerUltimoEstado(row.item) }}
        </template>
        <template #cell(selected)="{ rowSelected }">
          <template v-if="rowSelected">
            <span aria-hidden="true">&check;</span>
            <span class="sr-only">Selected</span>
          </template>
          <template v-else>
            <span aria-hidden="true">&nbsp;</span>
            <span class="sr-only">Not selected</span>
          </template>
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
      selectMode: "multi",
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
        {
          key: "selected",
          label: "Seleccionado",
          class: "text-center p2",
        },
      ],
      items: [],
      liquidacionesSeleccionadas: [],
    };
  },
  methods: {
    onRowSelected(items) {
      console.log(items);
      this.liquidacionesSeleccionadas = items;
    },
    async liquidarEstudios() {
      try {
          let respuesta = this.armarRespuestaConId()
          console.log(respuesta)
      } catch (error) {
          console.log(error)
      }
    },
    armarRespuestaConId(){
        let respuesta=[]
        console.log(this.liquidacionesSeleccionadas)
         this.liquidacionesSeleccionadas.forEach(estudio => {
             respuesta.push(estudio.id)
        });
        return respuesta
    },

    obtenerUltimoEstado(estudio) {
      let nameEstado = estudio.ultimo_estado.resourcetype;
      nameEstado = nameEstado.replace(/([a-z])([A-Z])/g, "$1 $2");
      nameEstado = nameEstado.replace(/([A-Z])([A-Z][a-z])/g, "$1 $2");
      return nameEstado;
    },
    async obtenerEstudiosLiquidar() {
      try {
        let response = await LiquidacionesService.obtenerEstudiosLiquidar();
        console.log(response);
        this.items = response.data;
      } catch (err) {
        console.log(err);
      }
    },
  },
  mounted() {
    axios
      .all([this.obtenerEstudiosLiquidar()])
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