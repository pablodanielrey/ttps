<template>
  <b-container>
      <div>

      <ValidationObserver ref="detailsEstudio">
               <b-col lg="5" md="5">
              <b-form-group id="pdf-label" label="Ingrese la factura del estudio:" label-for="pdf">
                <ValidationProvider :name="'pdf '" v-slot="{ errors }">
                  <b-form-file
                    v-model="file1"
                    :state="Boolean(file1)"
                     @change="obtenerPDF($event,file1)"
                     accept="application/pdf"
                    placeholder="Seleccione la factura..."
                    drop-placeholder="Drop file here..."
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
      </ValidationObserver>
      </div>

  </b-container>
</template>


<script>


export default {
  components: {},

  props: {   
  },
  created() {
  
  },
  data() {
    return {
     file1:[]
    };
  },

  methods: {
        obtenerPDF(event,file){
            console.log(event,file)
        }
  },
  computed: {

  },

  mounted() {
  }
 
};
</script>

