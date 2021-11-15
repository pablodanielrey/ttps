<template>
  <b-container>
    <div>
      <h3>Seleccion de turno para un paciente</h3>
      <h5>
        Paciente: {{ estudio.paciente.apellido }} {{ estudio.paciente.nombre }}
      </h5>
      <div v-if="loading">
        <b-spinner> </b-spinner>
      </div>
      <div v-else>
        <vue-cal
          :disable-views="['years', 'day']"
          :time-step="15"
          :disable-days="this.turnos"
          :snap-to-time="this.tiempoTurnos"
          locale="es"
          :events="getPacientes"
          :on-event-click="onEventClick"
          style="height: 600px"
          class="vuecal--full-height-delete"
          @view-change="logEvents('view-change', $event)"
          ref="vuecal"
        />
      </div>
      <b-modal
        ref="my-modal"
        :title="selectedEvent.title"
        @ok="confirmarTurno(selectedEvent.start, selectedEvent.end)"
      >
        <div>
          <p v-if="selectedEvent.start != null">
            Turno seleccionado {{ selectedEvent.start.format("DD/MM/YYYY") }}
          </p>
        </div>
        <p v-html="selectedEvent.contentFull" />
        <strong>Detalles:</strong>
        <ul>
          <li v-if="selectedEvent.start != null">
            Inicio {{ selectedEvent.start && selectedEvent.start.formatTime() }}
          </li>
          <li v-if="selectedEvent.end != null">
            Fin: {{ selectedEvent.end && selectedEvent.end.formatTime() }}
          </li>
        </ul>
      </b-modal>
    </div>
  </b-container>
</template>


<script>
import TurnosService from "@/services/TurnosService.js";
/* import axios from "axios"; */
import VueCal from "vue-cal";
import "vue-cal/dist/vuecal.css";
import "vue-cal/dist/i18n/es.js";

export default {
  components: { VueCal },

  props: {
    estudio: {
      type: Object,
    },
  }, 
  data() {
    return {
      tiempoTurnos: 15,
      loading: false,
      value: "",
      context: null,
      turnos: [],
      showDialog: false,
      selectedEvent: {},
      paciente: null,
      pacienteSelected: null,
      pacientes: [],
    };
  },

  methods: {
    logEvents(accion, event) {
     
      let rango;
      if (event.view == "month") {
        rango = {
          inicio: event.firstCellDate.toISOString(),
          fin: event.lastCellDate.toISOString(),
        };
      } else {
        rango = {
          inicio: event.startDate.toISOString(),
          fin: event.endDate.toISOString(),
        };
      }
      this.buscarTurnos(rango);    
      console.log(accion);
    },
    async buscarTurnos(rango) {
       
         try {
        let response = await TurnosService.obtenerTurnos(rango);
        this.turnos = response.data;
        console.log(response)
      } catch (err) {
        console.log(err);
      }

    },
 /*    async obtenerTurnos() {
      try {
        let response = await TurnosService.obtenerTurnos();
        this.turnos = response.data;
      } catch (err) {
        console.log(err);
      }
    }, */
    onEventClick(event, e) {
      this.selectedEvent = event;
      this.showDialog = true;
      this.$refs["my-modal"].show();
      // Prevent navigating to narrower view (default vue-cal behavior).
      e.stopPropagation();
    },
    confirmarTurno(inicio, fin) {
      let turnoEstudio = {
        inicio: inicio.format("YYYY-MM-DD HH:m"),
        fin: fin.toLocaleString("en-es"),
        idEstudio: this.estudio.id,
      };
      console.log(turnoEstudio);
    },
  },
  computed: {
    getOptionsPacientes() {
      let pacientes = this.pacientes.map((e) => ({
        id: e.id,
        label: e.nombre + " " + e.apellido,
      }));
      return pacientes;
    },
    getPacientes() {
      let pacientes = this.turnos.map((e) => ({
        start: new Date(e.inicio),
        end: new Date(e.fin),
        title: "Turno disponible",
        class: "ejemplo",
      }));

      return pacientes;
    },
  },

  mounted() {
   /*  axios
      .all([this.obtenerTurnos()])
      .then(() => {
        this.loading = false;
      })
      .catch((err) => {
        console.log(err);
      }); */
  },
};
</script>

<style scoped>
.vuecal__event {
  cursor: pointer;
}

.vuecal__event-title {
  font-size: 1.2em;
  font-weight: bold;
  margin: 4px 0 8px;
}

.vuecal__event-time {
  display: inline-block;
  margin-bottom: 12px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(0, 0, 0, 0.2);
}

.vuecal__event-content {
  font-style: italic;
}
</style>