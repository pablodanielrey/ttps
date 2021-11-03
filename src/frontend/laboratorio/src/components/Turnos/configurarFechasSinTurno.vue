<template>
  <b-container>
    <b-card header="Fechas en las que no se daran turnos">
      <b-row>
        <b-col>
          <vue-cal
            class="vuecal--date-picker"
            xsmall
            hide-view-selector
            :time="false"
            :transitions="false"
            active-view="month"
            :disable-views="['week']"
       locale="es"
          >
          </vue-cal>
        </b-col>
      </b-row>
      <b-row class="pb-2">
        <b-col class="text-center pt-3">
          <b-button variant="success">Agregar </b-button>
        </b-col>
      </b-row>

      <div>
        <b-table striped hover :items="items">
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
import VueCal from "vue-cal";
import "vue-cal/dist/vuecal.css";

export default {
  components: { VueCal },
  data() {
    return {
        fields: [
         { key: "Fecha", label: "Fecha", class: "text-center p2" },
       { key: "acciones", label: "Acciones", class: "text-center p2" },
      ],
      items: [
        { Fecha: "02/12/2021", acciones: "X" },
        { Fecha: "03/11/2021", acciones: "X" },
      ],
    };
  },
};
</script>

<style>
</style>