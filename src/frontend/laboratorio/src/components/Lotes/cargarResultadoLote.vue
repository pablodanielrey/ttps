<template>
  <b-container>
    <br />

    <b-card header=" Listado de Lotes">
      <b-table striped hover :items="items" :fields="fields">
        <template v-slot:cell(acciones)="item">
          <b-button
            title="Ver estudios"
            variant="outline-primary"
            @click="verEstudios(item.item)"
          >
            Estudios
          </b-button>
          <b-button
            title="URL"
            variant="outline-success"
            @click="loteActual(item.item)"
            v-b-modal.modal-prevent-closing
          >
            Cargar Resultado
          </b-button>
          <!-- <b-button @click="seleccionTurno(row.item.id)">
            seleccionar turno
          </b-button> -->
        </template>
      </b-table>
      <div>
        <b-row class="pb-2">
          <b-col class="text-center pt-3">
            <b-pagination
              v-model="currentPage"
              :total-rows="totalRows"
              :per-page="perPage"
            ></b-pagination>
          </b-col>
        </b-row>
      </div>
    </b-card>
    <b-modal size="xl" ref="my-modal" title="Estudios del lote 1" ok-only>
      <b-table :items="itemsEst" :fields="fieldsEst"> </b-table>
    </b-modal>

    <b-modal
      id="modal-prevent-closing"
      ref="modal"
      title="Resultado"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <b-form-group
          label="Url del resultado"
          label-for="url-input"
          invalid-feedback="el campo url del resultado es requerido"
          :state="urlResultadostate"
        >
          <b-form-input
            id="url-input"
            v-model="urlResultado"
            :state="urlResultadostate"
            required
          ></b-form-input>
        </b-form-group>
      </form>
    </b-modal>
  </b-container>
</template>

<script>
import LotesService from "@/services/LotesService.js";
import axios from "axios";

export default {
  name: "CargarResultadoLote",

  components: {},
  props: {},

  data() {
    return {
      idLoteActual: null,
      urlResultadostate: null,
      fechastate: null,
      urlResultado: null,
      fecha: null,
      alerts: [],
      perPage: 4,
      itemsEst: [],
      fieldsEst: [
        {
          key: "estudio.paciente.nombre",
          label: "Nombre",
          class: "text-center p2",
        },
        {
          key: "estudio.paciente.apellido",
          label: "Apellido",
          class: "text-center p2",
        },
        {
          key: "estudio.medico_derivante.apellido",
          label: "Medico derivante",
          class: "text-center p2",
        },
        {
          key: "estudio.tipo.nombre",
          label: "Tipo Estudio",
          class: "text-center p2",
        },
        {
          key: "estudio.diagnostico.nombre",
          label: "Diagnostico",
          class: "text-center p2",
        },
      ],
      pageOptions: [4, 10, 15],
      filter: null,
      currentPage: 1,
      totalRows: 1,
      items: [],
      fields: [
        { key: "fecha", label: "Fecha Creacion", class: "text-center p2" },

        { key: "acciones", label: "Acciones", class: "text-center p2" },
      ],
    };
  },

  created() {},

  methods: {
    loteActual(item) {
      console.log(item);
      this.idLoteActual = item.id;
    },
    async guardarDatos(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      this.enviarDatos()();
      console.log(this.fecha, this.urlResultado);
    },
    checkFormValidity() {
      const valid = this.$refs.form.checkValidity();
      this.urlResultadostate = valid;
      return valid;
    },
    resetModal() {
      this.urlResultado = "";
      this.urlResultadostate = null;
    },
    handleOk(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      this.handleSubmit();
    },
    async handleSubmit() {
      try {
        if (!this.checkFormValidity()) {
          return;
        }
        let datos = { fecha: new Date(), resultado: this.urlResultado };
        console.log(datos);
        let response = await LotesService.cargarResultadoLote(
          this.idLoteActual,
          datos
        );
        console.log(response);
        this.$nextTick(() => {
          this.$bvModal.hide("modal-prevent-closing");
        });
      } catch (error) {
        console.log(error);
      }
      if (!this.checkFormValidity()) {
        return;
      }
    },

    verEstudios(item) {
      console.log(item);
      this.itemsEst = item.estudios;
      this.$refs["my-modal"].show();
    },
    cargarResultado() {
      this.$refs["modalResultado"].show();
    },

    async obtenerLotes() {
      try {
        let response = await LotesService.obtenerLotes();
        console.log(response);
        this.items = response.data;
      } catch (err) {
        console.log(err);
      }
    },
  },

  computed: {},

  mounted() {
    axios
      .all([this.obtenerLotes()])
      .then(() => {
        this.totalRows = this.items.length;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style>
</style>
