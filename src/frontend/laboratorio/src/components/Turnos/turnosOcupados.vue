<template>
  <b-container>
    <div>
      <h3>Turnos Ocupados</h3>

      <div v-if="loading">
        <b-spinner> </b-spinner>
      </div>
      <div v-else>
        <vue-cal
          active-view="years"
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
      <b-modal ref="my-modal" :title="selectedEvent.title" ok-only>
        <div>
          <p v-if="selectedEvent.start != null">
            Turno Ocupado
            {{ selectedEvent.start.format("DD/MM/YYYY") }}
          </p>
        </div>

        <p v-html="selectedEvent.contentFull" />
        <strong>Detalles Paciente:</strong>
        <ul>
          <li v-if="selectedEvent.persona != null">
            Nombre: {{ selectedEvent.persona.apellido }}
            {{ selectedEvent.persona.nombre }}
          </li>
          <li v-if="selectedEvent.persona != null"> 
            Telefono:
            {{ selectedEvent.persona.telefono }}
          </li>
          <li v-if="selectedEvent.persona != null"> 
            Email:
            {{ selectedEvent.persona.email }}
          </li>
        </ul>
        <strong>Detalles Turno:</strong>
        <ul>
          <li v-if="selectedEvent.start != null">
            Inicio {{ selectedEvent.start && selectedEvent.start.formatTime() }}
          </li>
          <li v-if="selectedEvent.end != null">
            Fin: {{ selectedEvent.end && selectedEvent.end.formatTime() }}
          </li>
        </ul>
      <!--   <b-button
          @click="cancelarTurno(selectedEvent.start, selectedEvent.end)"
          variant="outline-danger"
          >Cancelar turno</b-button
        > -->
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
import axios from "axios";
export default {
  components: { VueCal },

  props: {
    estudio: {
      type: Object,
    },
  },
  data() {
    return {
      rangoCelda: {
        inicio: null,
        fin: null,
      },
      tiempoTurnos: 15,
      loading: true,
      value: "",
      context: null,
      turnos: [],
      selectedEvent: {},
      paciente: null,
      pacienteSelected: null,
      pacientes: [],
    };
  },

  methods: {
    async obtenerTurnos() {
      try {
        let response = await TurnosService.obtenerTurnosOcupados();
        this.turnos = response.data;
      } catch (err) {
        console.log(err);
      }
    },
    logEvents(accion, event) {
      console.log(accion, event);
    },
    onEventClick(event, e) {
      console.log(event, e);
      this.selectedEvent = event;
      this.$refs["my-modal"].show();
      e.stopPropagation();
    },
    async cancelarTurno(inicio, fin) {
      try {
        let turnoEstudio = {
          inicio: inicio.toISOString(),
          fin: fin.toISOString(),
        };
        let response = await TurnosService.cancelarTurno(turnoEstudio);
        this.obtenerTurnos();
        console.log(response);
      } catch (err) {
        console.log(err);
      }
    },
  },
  computed: {
    getPacientes() {
      let pacientes = this.turnos.map((e) => ({
        start: new Date(e.inicio),
        end: new Date(e.fin),
        title: e.persona.apellido + " " + e.persona.nombre,
        persona: e.persona,
      }));

      return pacientes;
    },
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

<style scoped>
</style>