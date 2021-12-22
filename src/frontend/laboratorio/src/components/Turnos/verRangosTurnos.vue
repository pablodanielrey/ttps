<template>
  <b-container>
    <b-card
      header="Fechas de rango de turnos seleccionadas"
    >  
        <b-table :items="items" :fields="fields">
            <template v-slot:cell(fecha_valido)="row">
          {{ armarFecha(row.item) }}
        </template>
          <template v-slot:cell(acciones)="row">
            <b-button
              title="Borrar"
              variant="outline-danger"
              @click="borrarRango(row.item)"
              >X
            </b-button>
              <b-button
              title="Rangos"
              variant="outline-info"
              @click="verRangos(row.item)"
              >Rangos
            </b-button>
          </template>
        </b-table>
  
    </b-card>
     <b-modal ref="modalRangos" ok-only title="Rangos de fechas">
        <b-table :items="rangos" :fields="fieldsRango">
        </b-table>
     
      
      </b-modal>
  </b-container>
</template>

<script>
import TurnosService from "@/services/TurnosService.js";
import axios from "axios";
export default {
  data() {
    return {
      fechaSeleccionada: null,
      fields: [
        { key: "fecha_valido", label: "Fecha", class: "text-center p2" },
        { key: "acciones", label: "Acciones", class: "text-center p2" },
      ],
        fieldsRango: [
               { key: "hora_inicio", label: "inicio", class: "text-center p2" },
        { key: "hora_fin", label: "Fin", class: "text-center p2" },
        { key: "frecuencia", label: "Frecuencia", class: "text-center p2" },
      ],
      items: [],
      rangos:[],
    };
  },

  methods: {
      armarFecha(fecha) {
      return new Date(fecha.fecha_valido).format("DD-MM-YYYY");
    },
    verRangos(rangos){
      this.rangos = rangos.rangos;
         this.$refs["modalRangos"].show();
    
    },
    async obtenerRangos() {
      try {
        let response = await TurnosService.obtenerRangos();
        console.log(response);
        this.items = response.data;
      } catch (error) {
        console.log(error);
      }
    },
    async borrarRango(rango) {
      try {
         await TurnosService.eliminarRango(rango.id);
          this.$root.$bvToast.toast(
          "Se elimino el rango ",
          {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "info",
          }
        );
        this.obtenerRangos();
      } catch (error) {
        console.log(error);
      }
    },
  },
  computed: {},
  mounted() {
    axios
      .all([this.obtenerRangos()])
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