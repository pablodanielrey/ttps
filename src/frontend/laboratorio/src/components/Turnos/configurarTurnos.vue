<template>
  <b-container>
    <b-card header="Horarios de atencion-Rango de horario">
      <b-form action class="form" @submit.prevent="onSubmit">
        <b-row>
          <b-col>
            <b-calendar v-model="fechaSeleccionada" locale="en-US" required></b-calendar>
          </b-col>
        </b-row>

        <b-row>
          <b-col lg="3" md="5" sm="10">
            <b-form-group
              id="hsInicio-label"
              label="Hora de inicio:"
              label-for="hsInicio"
            >
              <b-form-input
                name="hora_inicio"
                placeholder="09:00"
                v-model="hsInicio"
                type="time"
                required
              ></b-form-input>
            </b-form-group>
          </b-col>
          <b-col lg="3" md="5" sm="10">
            <b-form-group
              id="hsFin-label"
              label="Hora de Fin:"
              label-for="hsFin"
            >
              <b-form-input
                name="hora_fin"
                placeholder="13:00"
                :min="hsInicio"
                v-model="hsFin"
                type="time"
                required
              ></b-form-input>
            </b-form-group>
          </b-col>
          <b-col lg="3" md="5" sm="10">
            <b-form-group
              id="frecuencia-label"
              label="Frecuencia en minutos:"
              label-for="frecuencia"
            >
              <b-form-input
                type="number"
                min="5"
                max="60"
                required
                name="frecuencia"
                placeholder="15:00"
                v-model="frecuencia"
              ></b-form-input>
            </b-form-group>
          </b-col>
        </b-row>
        <b-row class="pb-2">
          <b-col class="text-center pt-3">
            <b-button variant="success" type="submit">Agregar </b-button>
          </b-col>
        </b-row>
      </b-form>
    </b-card>
    <div>
      <b-table striped hover :fields="fields" :items="items"></b-table>
    </div>
    <b-row class="pb-2">
      <b-col class="text-center pt-3">
        <b-button variant="success" @click="confirmarRangos()">Confirmar </b-button>
      </b-col>
    </b-row>

   
  </b-container>
</template>

<script>
import TurnosService from "@/services/TurnosService.js";

export default {
  components: {},
  data() {
    return {
      hsFin: null,
      hsInicio: null,
      frecuencia: null,
      fechaSeleccionada: new Date(),
      alerts: [],
      fields: [
        { key: "hora_inicio", label: "inicio", class: "text-center p2" },
        { key: "hora_fin", label: "Fin", class: "text-center p2" },
        { key: "frecuencia", label: "Frecuencia", class: "text-center p2" },
      ],
      items: [],
    };
  },
  methods: {
    onSubmit() {
      this.items.push({
        hora_inicio: this.hsInicio,
        hora_fin: this.hsFin,
        frecuencia: this.frecuencia,
      });
      console.log(this.hsInicio, this.hsFin, this.frecuencia);
      console.log( this.items)
    },
    async confirmarRangos(){
      try {
       /*  { "fecha_valido": "2011-12-13T00:00:00-03:00",
         "rangos": [ { "hora_inicio": 7, "hora_fin": 12, "frecuencia": 15 }, { "hora_inicio": 14, "hora_fin": 19, "frecuencia": 15 } ] } */
       this.armarHoraEnteros()
       let datos={
            "fecha_valido":new Date(this.fechaSeleccionada),
            "rangos": this.armarHoraEnteros()        
        }    
         await TurnosService.agregarRangoTurnos(datos)
          this.$root.$bvToast.toast(
          "Se configuraron los rangos de turnos para la fecha seleccionada " ,           
          {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "info",
          }
        );
     
        

      } catch (error) {
        console.log(error)
      }
    },
    armarHoraEnteros(){
      this.items.forEach(elem => {
        elem.hora_inicio =elem.hora_inicio.substr(0,2)
        elem.hora_fin =elem.hora_fin.substr(0,2)
      });
      return this.items
    }
  },
};
</script>

<style>
</style>