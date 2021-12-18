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
import EstudiosService from "@/services/EstudiosService.js";
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
      rangoCelda: {
        inicio: null,
        fin: null,
      },
      tiempoTurnos: 15,
      loading: false,
      turnos: [],
      showDialog: false,
      selectedEvent: {},
      paciente: null,
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
      this.rangoCelda.inicio = rango.inicio;
      this.rangoCelda.fin = rango.fin;
      this.buscarTurnos(rango);
    },
    async buscarTurnos(rango) {
      try {
        let response = await TurnosService.obtenerTurnos(rango);
        this.turnos = response.data;
      } catch (err) {
        console.log(err);
      }
    },
    onEventClick(event, e) {
      this.selectedEvent = event;
      if (this.selectedEvent.start < new Date()) {
        this.$root.$bvToast.toast(
          "Esta seleccionando un turno con una fecha o hora que ya paso, por favor seleccione otro turno",
          {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "danger",
          }
        );
      } else {
        this.showDialog = true;
        this.$refs["my-modal"].show();
        e.stopPropagation();
      }
    },
    async confirmarTurno(inicio, fin) {
      try {
        let turnoEstudio = {
          turno: { inicio: inicio.toISOString(), fin: fin.toISOString() },
          estudio_id: this.estudio.id,
          resourcetype: this.estudio.ultimo_estado.resourcetype,
        };
        await EstudiosService.actualizarUltimoEstado(
          turnoEstudio,
          this.estudio.ultimo_estado.id
        );
        this.$root.$bvToast.toast("Se selecciono el turno para el paciente ", {
          title: "Atencion!",
          toaster: "b-toaster-top-center",
          solid: true,
          variant: "success",
        });
        this.$router.push({
          name: "listaEstudios",
        });
      } catch (err) {
        console.log(err);
        this.$root.$bvToast.toast(
          "no se pudo seleccionar el turno para el paciente, por favor vuelva a intentar ",
          {
            title: "Atencion!",
            toaster: "b-toaster-top-center",
            solid: true,
            variant: "danger",
          }
        );
      }
    },
  },
  computed: {
    getPacientes() {
      let pacientes = this.turnos.map((e) => ({
        start: new Date(e.inicio),
        end: new Date(e.fin),
        title: "Disponible",
      }));

      return pacientes;
    },
  },

  mounted() {},
};
</script>

<style scoped>
</style>