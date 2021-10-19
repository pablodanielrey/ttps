<template>
  <div>
    <button v-on:click='getPacientes'>buscar</button>
  </div>
</template>

<script>
import PacienteService from "@/services/PacientesService";
import axios from "axios";

export default {
  pops: {},
  data() {
    return {};
  },
  methods: {
    buscar: function () {
      console.log("buscando");
    },
    async getPacientes() {
      try {
        const response = await PacienteService.obtenerPacientes();      
        console.log(response)

      } catch (err) {
        console.log(err);
      }
    },

  },
  mounted() {
    axios
      .all([ this.getPacientes()])
     
  },
};
</script>

<style>
</style>