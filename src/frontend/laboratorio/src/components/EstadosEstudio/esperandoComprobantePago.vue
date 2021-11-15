<template>
  <b-container>
    <div>
      <b-card header="Estudio esperando que se ingrese el comprobante pago">
        <b-row>
          <b-col lg="5" md="5" class="text-center pt-3">
            <ValidationObserver ref="detailsComprobante">
              <b-form-group
                id="pdf-label"
                label="Comprobante de pago:"
                label-for="pdf"
              >
                <ValidationProvider :name="'pdf '" v-slot="{ errors }">
                  <b-form-file
                    v-model="file1"
                    :state="Boolean(file1)"
                    @change="obtenerPDF($event, file1)"
                    accept="application/pdf"
                    placeholder="Seleccione el comprobante de pago..."
                    browse-text="Buscar"
                  ></b-form-file>
                  <b-form-invalid-feedback
                    v-for="error in errors"
                    :key="error.key"
                  >
                    {{ error }}
                  </b-form-invalid-feedback>
                </ValidationProvider>
              </b-form-group>
            </ValidationObserver>
          </b-col>
        </b-row>

        <div>
          <div class="counter">
            Quedan {{ counter }} dias para subir el comprobante de pago
          </div>
        </div>
        <b-row class="pb-2">
          <b-col class="text-center pt-3">
            <b-button variant="success" @click="guardarComprobante()"
              >Guardar
            </b-button>
          </b-col>
        </b-row>
      </b-card>
    </div>
  </b-container>
</template>


<script>
 import EstudiosService from "@/services/EstudiosService.js";
 
export default {
  components: {},
  props: {
    estudio: {
      type: Object,
    },
  },
  data() {
    return {
      file1: [],
      counter: 20,
      comprobantePago: null,
    };
  },
  created() {
    let result = this.$crontab.addJob({
      name: "counter",
      interval: {
        day: "/31",
      },
      job: this.countUp,
    });
    console.log(result);
  },

  methods: {
    obtenerPDF(event) {
      const file = event.target.files[0];
      this.createBase64(file);
    },
    createBase64(file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        this.comprobantePago = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    countUp() {
      this.counter -= 1;
    },
    async guardarComprobante() {
      let result = await this.$refs.detailsComprobante.validate();
      if (result) {
        let datosComprobante = {
          estudio_id: this.estudio.id,
          comprobante: this.comprobantePago,
        };
        console.log(datosComprobante)
         try {
          let response = await EstudiosService.actualizarUltimoEstado(
            datosComprobante
          );
          console.log(response);
        } catch (err) {
          console.log(err);
        } 
        console.log(datosComprobante);
      }
    },
  },
  computed: {},

  mounted() {},
};
</script>

