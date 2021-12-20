<template>
  <b-container>
    <div>
      <b-card header="Modo de Trabajo">
        <div>
          <div>
            <select name="modo_trabajo" @change="guardarModo($event)">
              <option value="PO" :selected="this.modo.modo_operacion=='PO'">Paciente obligado a completar</option>
              <option value="PNO" :selected="this.modo.modo_operacion=='PNO'">Paciente o Empleado pueden completar</option>
            </select>
          </div>
        </div>
      </b-card>
    </div>
  </b-container>
</template>


<script>
import ModoDeTrabajoService from "@/services/ModoDeTrabajo.js";
import axios from "axios";


export default {
  name: "ModoDeTrabajo",

  components: {},
  props: {},

  data() { 
    return {
      modos: null,
      modo: null,
    }
  },
  created() {},

  methods: {
    async obtenerHistorialModos() {
      try {
        let response = await ModoDeTrabajoService.obtenerModo();
        this.modos = response.data; 
        console.log(this.modos)
     
      } catch (err) {
        console.log(err);
      }
    },
    async guardarModo(event) {
      try {
        //console.log(event.target.value);
        let response = await ModoDeTrabajoService.guardarModo(event.target.value);
        console.log(response)
      } catch (err) {
        console.log(err);
      }
    },
  },
  mounted() {
    axios
      .all([this.obtenerHistorialModos()])
      .then(() => {
        this.modo = this.modos.at(-1);
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