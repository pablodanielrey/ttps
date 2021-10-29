<template>
  <b-container>
    <div v-if="loading">
      <b-spinner> </b-spinner>
    </div>
    <div v-else>
      <vue-cal
        :disable-views="['years']"
        :editable-events="{
          title: true,
          drag: false,
          resize: true,
          delete: true,
          create: true,
        }"
        :time-from="9 * 60"
        :time-to="15 * 60"
        :time-step="15"
        :drag-to-create-threshold="0"
        :disable-days="this.turnos"
        active-view="year"
        locale="es"
       :events="getPacientes"
       @event-create="logEvents('event-create', $event)"
        @event-duration-change="logEvents('event-duration-change', $event)"
      />
    </div>
  </b-container>
</template>


<script>
import TurnosService from "@/services/TurnosService.js";
import axios from "axios";
import VueCal from "vue-cal";
import "vue-cal/dist/vuecal.css";
import "vue-cal/dist/i18n/es.js";

export default {
  components: { VueCal },

  props: {},
  created() {},
  data() {
    return {
      loading: true,
      value: "",
      context: null,
      turnos: [],
    };
  },

  methods: {
    async obtenerTurnos() {
      try {
        let response = await TurnosService.obtenerTurnos();
        this.turnos = response.data;
        console.log(this.turnos);
      } catch (err) {
        console.log(err);
      }
    },
    onContext(ctx) {
      this.context = ctx;
    },
    logEvents(e, c){
console.log(e,c)
    }
  },
  computed: {
        getPacientes(){
        let pacientes= this.turnos.map((e) => ({
          start:new Date( e.inicio),
          end: new Date(e.fin),
          title:"test"
        }))
      
        return pacientes
    }
  },

  mounted() {
    axios
      .all([this.obtenerTurnos()])
      .then(() => {
        this.loading = false;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

