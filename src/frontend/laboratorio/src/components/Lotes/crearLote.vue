<template>
  <b-container>
    <br />
    <h4>Listado de Estudios</h4>

    <b-table striped hover :items="items"></b-table>

    <b-button>Crear Lote</b-button>
  </b-container>
</template>


<script>
import LotesService from "@/services/LotesService.js";
import axios from "axios";
export default {
  name: "CrearLote",

  components: {},
  props: {},

  data() {
    return {
        items: [],
    };
  },

  created() {
    console.log(this.paciente);
  },

  methods: {
    formatear_lista(e) {
        return {
            'fecha': e.fecha_alta,
            'paciente': e.paciente.nombre,
            'tipo': e.tipo.nombre,
            'médico': e.medico_derivante.nombre
        }
    },
    async obtenerListaEstudios() {
      try {
        let response = await LotesService.obtenerListaEstudios();
        this.items = response.data.map(this.formatear_lista).slice(0,10);
        console.log(this.items);
      } catch (err) {
        console.log(err);
      }
    }
  },

  computed: {
      
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