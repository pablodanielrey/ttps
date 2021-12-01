<template>
  <b-container>
    <div>
      <b-card header="Estudio esperando ingreso del comprobante pago">
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
      counter: 30,
      comprobantePago: null,
    };
  },
  created() {
    console.log(this.estudio)
    let fecha = new Date(this.estudio.fecha_alta);
    this.counter = new Date();
    this.counter = this.difference(fecha, this.counter);
    this.counter = this.counter == 0 ? 30 : this.counter
  },

  methods: {
    difference(date1, date2) {
      let date1utc = Date.UTC(
        date1.getFullYear(),
        date1.getMonth(),
        date1.getDate()
      );
      let date2utc = Date.UTC(
        date2.getFullYear(),
        date2.getMonth(),
        date2.getDate()
      );
      let day = 1000 * 60 * 60 * 24;
      return (date2utc - date1utc) / day;
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
          console.log(datosComprobante);
           await EstudiosService.actualizarUltimoEstado(
            datosComprobante
          );
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

