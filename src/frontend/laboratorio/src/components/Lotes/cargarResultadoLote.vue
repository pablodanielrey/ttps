<template>
  <b-container>
    <br />
       <h4>Listado de Lotes generados</h4>
      <b-table
        striped
        hover
        :items="items"
        :fields="fields"
        show-empty
        empty-text="Todavia no hay lotes para que se cargen los resultados"
      >
        <template v-slot:cell(acciones)="item">
      <!--     <b-button
            title="Ver estudios"
            variant="outline-primary"
            @click="verEstudios(item.item)"
          >
            Estudios
          </b-button>  -->
          <b-button
            title="URL"
            variant="outline-success"
            @click="loteActual(item.item)"
            v-b-modal.modal-prevent-closing
          >
            Cargar Resultado
          </b-button>
      
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
    <b-modal size="xl" ref="my-modal" title="Estudios del lote 1" ok-only>
      <b-table :items="itemsEst" :fields="fieldsEst"> </b-table>
      

    </b-modal>

    <b-modal
      id="modal-prevent-closing"
      ref="modal"
      title="Resultado"
      @show="resetModal"
      @hidden="resetModal"
      size="xl"
      @ok="handleOk"
    >
       <b-table :items="itemsEst" :fields="fieldsEst"> 
   <template v-slot:cell(acciones)="row">
     <b-button
            title="Anular estudio por muestra insuficiente"
            variant="outline-white"            
            @click="anularEstudioMuestraInsuficiente(row.item.estudio)"
            >
             <b-icon icon="x-circle" fill variant="danger"> </b-icon>
           
          </b-button>
   </template>

       </b-table>
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
         {
          key: "acciones",
          label: "Anular",
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
      this.itemsEst = item.estudios;
    },

    eliminarEstudio(item) {
      this.itemEst.pop(item);
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
        let datos = { fecha: new Date(), resultado: this.urlResultado,estudios:this.getIdEstudios() };
        console.log(datos);
        let response = await LotesService.cargarResultadoLote(
          this.idLoteActual,
          datos
        );
        console.log(response);
        this.$nextTick(() => {
          this.$bvModal.hide("modal-prevent-closing");
        });
        this.$root.$bvToast.toast("se guardo la Url del resultado con exito", {
          title: "Atencion!",
          toaster: "b-toaster-top-center",
          solid: true,
          variant: "success",
        });
        this.obtenerLotes(); 
      } catch (error) {
        console.log(error);
      }
      if (!this.checkFormValidity()) {
        return;
      }
    },
    getIdEstudios(){
      let idEstudios=[]
      this.itemsEst.forEach(estudio => {
          idEstudios.push({estudio:{id:estudio.estudio.id}})
      });
        return idEstudios
    },

    verEstudios(item) {    
      this.itemsEst = item.estudios;
      this.$refs["my-modal"].show();
    },
    cargarResultado() {
      this.$refs["modalResultado"].show();
    },

    async obtenerLotes() {
      try {
        let response = await LotesService.obtenerLotes();      
        this.items = response.data;
      } catch (err) {
        console.log(err);
      }
    },
    anularEstudioMuestraInsuficiente(estudio){ 
      this.itemsEst =  this.itemsEst.filter(e => e.estudio.id != estudio.id);   
      
    }
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
