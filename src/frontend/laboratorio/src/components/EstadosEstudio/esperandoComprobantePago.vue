<template>
  <b-container>
    <div>
      <b-card header="Estudio esperando que se ingrese el comprobante pago">
        <b-row>
          <b-col lg="5" md="5" class="text-center pt-3">
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
          </b-col>
        </b-row>
       
        <div>
          <div class="counter">
            Quedan {{ counter }} dias para subir el comprobante de pago
          </div>
        </div>
         <b-row class="pb-2">
          <b-col class="text-center pt-3">
            <b-button variant="success">Guardar </b-button>
          </b-col>
        </b-row>
      </b-card>
    </div>
  </b-container>
</template>


<script>
export default {
  components: {},

  props: {},
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
  data() {
    return {
      file1: [],
      counter: 20,
    };
  },

  methods: {
    bajarFactura() {},
    countUp() {
      this.counter -= 1;
    },
  },
  computed: {},

  mounted() {},
};
</script>

