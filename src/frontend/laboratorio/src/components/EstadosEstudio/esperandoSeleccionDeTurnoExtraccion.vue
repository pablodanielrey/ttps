<template>
  <b-container>
    <div>
      <div v-if="loading">
        <b-spinner> </b-spinner>
      </div>
      <div v-else>
        <vue-cal
          :disable-views="['years']"
          :time-from="9 * 60"
          :time-to="15 * 60"
          :time-step="15"
          :disable-days="this.turnos"
          :snap-to-time="this.tiempoTurnos"
          active-view="year"
          locale="es"
          :events="getPacientes"
          :on-event-click="onEventClick"
          style="height: 600px"
          class="vuecal--full-height-delete"
        />
      </div>
      <b-modal ref="my-modal" :title="selectedEvent.title">
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
        <b-col lg="9" md="9" sm="10">
          <b-form-group
            id="paciente-label"
            label="Paciente:"
            label-for="Paciente"
          >
            <v-select
              @input="cambiarPaciente()"
              placeholder="Seleccione un paciente  "
              v-model="paciente"
              :options="getOptionsPacientes"
              :value="pacienteSelected"
              :sercheable="true"
              responsive="sm"
              size="sm"
              lenguage="en-US"
            ></v-select>
            <p style="color: red; font-size: 10px" v-if="paciente == ''">
              Se debe seleccionar un paciente
            </p>
          </b-form-group>
        </b-col>
      </b-modal>
    </div>
  </b-container>
</template>


<script>
import TurnosService from "@/services/TurnosService.js";
import axios from "axios";
import VueCal from "vue-cal";
import "vue-cal/dist/vuecal.css";
import "vue-cal/dist/i18n/es.js";
import PacientesService from "@/services/PacientesService.js";

export default {
  components: { VueCal },

  props: {},
  created() {},
  data() {
    return {
      tiempoTurnos: 15,
      loading: true,
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
    async obtenerTurnos() {
      try {
        let response = await TurnosService.obtenerTurnos();
        this.turnos = response.data;
        console.log(this.turnos);
      } catch (err) {
        console.log(err);
      }
    },
    onEventClick(event, e) {
      this.selectedEvent = event;
      this.showDialog = true;
      this.$refs["my-modal"].show();
      // Prevent navigating to narrower view (default vue-cal behavior).
      e.stopPropagation();
    },
    cambiarPaciente() {
      console.log(this.paciente);
    },
    async obtenerPacientes() {
      try {
        let response = await PacientesService.obtenerPacientes();
        this.pacientes = response.data;
      } catch (err) {
        console.log(err);
      }
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
    axios
      .all([this.obtenerTurnos(), this.obtenerPacientes()])
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