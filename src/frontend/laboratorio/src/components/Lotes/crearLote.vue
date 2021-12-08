<template>
  <b-container>
    <div v-if="loading">
      <b-spinner></b-spinner>
    </div>
    <div v-else>
      <b-card
        header=" Listado de Estudios esperando Lote para procesamiento biotecnológico"
      >
        <b-table :items="estudios" :fields="fields">
          <template v-slot:cell(fecha_alta)="row">
            {{ obtenerFecha(row.item) }}
          </template>
        </b-table>

        <b-row class="pb-2">
          <b-col class="text-center pt-3">
            <b-button
              @click="crearLote()"
              variant="success"
              :disabled="estudios.length < 10 ? true : false"
              >Crear Lote
            </b-button>
          </b-col>
        </b-row>
      </b-card>
    </div>
  </b-container>
</template>


<script>
import LotesService from "@/services/LotesService.js";
import EstudiosService from "@/services/EstudiosService.js";

import axios from "axios";
export default {
  name: "ListaPacientes",

  components: {},
  props: {},

  data() {
    return {
      estudios: [],
      loading: true,
      perPage: 10,
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

        {
          key: "fecha_alta",
          label: "Fecha Extraccion",
          class: "text-center p2",
        },
      ],
      items: [],
    };
  },

  created() {},
  methods: {
    async crearLote() {
      try {
        let estudios = [];
        let objeto = {};
        let id;
        this.estudios.forEach((est) => {
          id = est.id;
          estudios.push(id);
        });
        objeto.estudios = estudios;
        let response = await LotesService.crearLote(objeto);
        this.$root.$bvToast.toast("se creo con exito el lote", {
          title: "Atencion!",
          toaster: "b-toaster-top-center",
          solid: true,
          variant: "success",
        });
        console.log(response);
        this.$router.push({
          name: "cargarResultadoLote",
        });
      } catch (err) {
        console.log(err);
        this.$root.$bvToast.toast(
          "ocurrio un error mientras creaba el lote, por favor vuelva a intentar",
          {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "danger",
          }
        );
      }
    },
    obtenerFecha(estudio) {
      //let fecha = estudio.estados[estudio.estados.length - 1].fecha;
      let fecha = estudio.ultimo_estado.fecha;
      fecha = new Date(fecha);
      return fecha.format("DD-MM-YYYY");
    },
    async obtenerListaEstudiosEsperandoProcesamiento() {
      try {
        let response =
          await LotesService.obtenerListaEstudiosEsperandoProcesamiento();
        this.items = response.data;
        this.obtenerEstudios();
      } catch (err) {
        console.log(err);
      }
    },
    async obtenerEstudios() {
      this.loading = true;
      try {
        this.items.forEach(async (id) => {
          this.loading = true;
          let response = await EstudiosService.obtenerEstudio(id);
          this.estudios.push(response.data);
        });
        this.ordenarEstudiosPorFecha();
      } catch (error) {
        console.log(error);
      } finally {
        this.loading = false;
      }
    },
    ordenarEstudiosPorFecha() {
      this.estudios.sort(function (a, b) {
        if (new Date(a.ultimo_estado.fecha) > new Date(b.ultimo_estado.fecha)) {
          return 1;
        }
        if (new Date(a.ultimo_estado.fecha) < new Date(b.ultimo_estado.fecha)) {
          return -1;
        }
      });
    },
  },
  mounted() {
    axios
      .all([this.obtenerListaEstudiosEsperandoProcesamiento()])
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