<template>
  <b-container>
    <div>
      <br />
      <b-card header="Estudio esperando ingreso del comprobante pago">
        <div>
          <b-row>
            <b-col>
              <ValidationObserver ref="detailsComprobante">
                <b-form-group id="pdf-label" label-for="pdf">
                  <ValidationProvider
                    :rules="'required'"
                    :name="'Comprobante '"
                    v-slot="{ errors }"
                  >
                    <b-form-file
                      v-model="file1"
                      :state="Boolean(file1)"
                      @change="obtenerPDF($event, file1)"
                      accept="application/pdf"
                      placeholder="Seleccione el comprobante de pago..."
                      browse-text="Buscar"
                      id="file-default"
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
        </div>
        <div class="counter">
          Quedan {{ counter }} dias para subir el comprobante de pago
        </div>
        <div>
          <b-row class="pb-2">
            <b-col class="text-center pt-3">
              <b-button variant="success" @click="guardarComprobante()"
                >Guardar
              </b-button>
            </b-col>
          </b-row>
        </div>
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
      file1: null,
      counter: 0,
      comprobantePago: null,
    };
  },
  created() {
    console.log(this.estudio);
    let fecha = new Date(this.estudio.ultimo_estado.fecha);
    this.counter = new Date();
    this.counter= this.difference(fecha.getDate(),this.counter.getDate())
 
  },

  methods: {
    difference(fechaAlta, diaHoy) {
      let xtotal=30
    return xtotal - (diaHoy - fechaAlta)     
    },
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
    async guardarComprobante() {
      let result = await this.$refs.detailsComprobante.validate();
      
      if (result) {
        try {
          let datosComprobante = {
            estudio_id: this.estudio.id,
            comprobante: this.comprobantePago,
          };         
          await EstudiosService.actualizarUltimoEstado(datosComprobante,this.estudio.ultimo_estado.id);
          this.$root.$bvToast.toast("Se agrego el comprobante de pago", {
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
            "ocurrio un error mientras agregaba el comprobante de pago",
            {
              title: "Atencion!",
              toaster: "b-toaster-top-center",
              solid: true,
              variant: "danger",
            }
          );
        }
      }
    },
  },
  computed: {},

  mounted() {},
};
</script>

