<template>
  <b-container>
    <b-card header="Fechas de excepcion de turnos, no se daran turnos en estos dias">
      <!--   <b-alert show variant="danger">Atención! la fecha que quiere agregar 10-12-21 a excepcion ya tiene turnos asignados, 
          por favor cancele los turnos para esa fecha y vuelva a intentar </b-alert> -->
      <b-row>
        <b-col>
              <b-calendar v-model="fechaSeleccionada"  locale="en-US"></b-calendar>

        </b-col>
      </b-row>
      <b-row class="pb-2">
        <b-col class="text-center pt-3">
          <b-button variant="success" @click="agregarFechaExcepcion()">Agregar </b-button>
        </b-col>
      </b-row>

      <div>
        <b-table   :items="items"
      :fields="fields"
      >
                  <template v-slot:cell(acciones)>
        <b-button title="Borrar" variant="outline-danger">X
         </b-button>
                  </template>
        </b-table>
      </div>
    </b-card>
  </b-container>
</template>

<script>
import TurnosService from "@/services/TurnosService.js";
import axios from "axios";
export default {

  data() {
    return {
      fechaSeleccionada:null,
        fields: [
         { key: "fecha", label: "Fecha", class: "text-center p2" },
       { key: "acciones", label: "Acciones", class: "text-center p2" },
      ],
      items: [],
    };
  },

  methods: {
     

   async agregarFechaExcepcion(){
      console.log(this.fechaSeleccionada)
      try {
       let datos={
         fecha : this.fechaSeleccionada
       }
        let response = await TurnosService.fechaSinTurnos(datos)
        console.log(response)
         this.$root.$bvToast.toast(
          "Se seleciono que la fecha "+response.data.fecha+" no se daran turnos",
          {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "info",
          }
        );
      this.obtenerFechasSinTurnos()
      } catch (error) {
        console.log(error)
      }
    },
   async  obtenerFechasSinTurnos(){
       try {
       
        let response = await TurnosService.obtenerFechasSinTurnos()        
        console.log(response)
        this.items = response.data

      } catch (error) {
        console.log(error)
      }
    }
  
  },
  computed : {

  },
    mounted() {
    axios
      .all([this.obtenerFechasSinTurnos()])
      .then(() => {
       
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