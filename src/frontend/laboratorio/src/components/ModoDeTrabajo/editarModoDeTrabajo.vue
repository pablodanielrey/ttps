<template>
  <b-container>
    <div>
      <b-card header="Modo de Trabajo">
        <div>
          <div>

          </div>
        </div>
      </b-card>
    </div>
  </b-container>
</template>


<script>
import ModoDeTrabajoService from "@/services/ModoDeTrabajo.js";

export default {
  mounted() {},

  components: {},
  props: {
  },
  created() {},
  data() {},

  methods: {
    async verModo() {
      try {
        let response = await ModoDeTrabajoService.obtenerModo();
        this.modo = response.modo_operacion
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
  },
  computed: {},
};
</script>

<style>
</style>