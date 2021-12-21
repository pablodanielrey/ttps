<template>
  <b-container>
    <ValidationObserver ref="detailsEstudio">
      <b-form-group>
        <b-alert
          v-for="alert in alerts"
          dismissible
          v-bind:key="alert.key"
          show
          :variant="alert.variant"
          >{{ alert.message }}</b-alert
        >
      </b-form-group>
      <b-card header="Horarios de atencion-Rango de horario">
        <b-row>
          <b-col lg="3" md="5" sm="10">
            <b-form-group
              id="hsInicio-label"
              label="Hora de inicio:"
              label-for="hsInicio"
            >
              <ValidationProvider
                :name="'hsInicio '"
                :rules="'required'"
                v-slot="{ errors, valid }"
              >
                <b-form-input
                  name="hora_inicio"
                  placeholder="09:00"
                  v-model="hsInicio"
                  :state="errors[0] ? false : valid ? true : null"
                ></b-form-input>
                <b-form-invalid-feedback
                  v-for="error in errors"
                  :key="error.key"
                >
                  {{ error }}
                </b-form-invalid-feedback>
              </ValidationProvider>
            </b-form-group>
          </b-col>
          <b-col lg="3" md="5" sm="10">
            <b-form-group
              id="hsFin-label"
              label="Hora de Fin:"
              label-for="hsFin"
            >
              <ValidationProvider
                :name="'hsFin '"
                :rules="'required'"
                v-slot="{ errors, valid }"
              >
                <b-form-input
                  name="hora_fin"
                  placeholder="13:00"
                  v-model="hsFin"
                  :state="errors[0] ? false : valid ? true : null"
                ></b-form-input>
                <b-form-invalid-feedback
                  v-for="error in errors"
                  :key="error.key"
                >
                  {{ error }}
                </b-form-invalid-feedback>
              </ValidationProvider>
            </b-form-group>
          </b-col>
          <b-col lg="3" md="5" sm="10">
            <b-form-group
              id="frecuencia-label"
              label="Frecuencia en minutos:"
              label-for="frecuencia"
            >
              <ValidationProvider
                :name="'frecuencia '"
                :rules="'required'"
                v-slot="{ errors, valid }"
              >
                <b-form-input
                  name="frecuencia"
                  placeholder="15:00"
                  v-model="frecuencia"
                  :state="errors[0] ? false : valid ? true : null"
                ></b-form-input>
                <b-form-invalid-feedback
                  v-for="error in errors"
                  :key="error.key"
                >
                  {{ error }}
                </b-form-invalid-feedback>
              </ValidationProvider>
            </b-form-group>
          </b-col>
          <b-col>
                 <div>
      A Partir de:<br>
               <b-calendar v-model="fechaSeleccionada" locale="en-US"></b-calendar>

    </div>
          </b-col>
        </b-row>
        <b-row class="pb-2">
          <b-col class="text-center pt-3">
            <b-button variant="success">Agregar </b-button>
          </b-col>
        </b-row>
      </b-card>
    </ValidationObserver>
       <div>
      <b-table striped hover :items="items"></b-table>
    </div>
  <b-row class="pb-2">
          <b-col class="text-center pt-3">
            <b-button variant="success">Confirmar </b-button>
          </b-col>
        </b-row>

  <!--   <b-container>
      Hora Inicio
      <input name="hora_inicio" />
      Hora Fin
      <input name="hora_fin" />
      Frecuencia
      <input name="frecuencia" />
      <button>agregar</button>
    </b-container>

    <div>
      <b-table striped hover :items="items"></b-table>
    </div>

    <button>aceptar</button> -->
  </b-container>
</template>

<script>

export default {
  components: {  },
  data() {
    return {
      hsFin: null,
      hsInicio: null,
      frecuencia: null,
      items: [
        { hora_inicio: "09:00", hora_fin: "13:00", frecuencia: "15 min", a_partir:"02/11/2021" },
        { hora_inicio: "14:00", hora_fin: "17:00", frecuencia: "20 min",a_partir:"02/01/2022"},
      ],
    };
  },
};
</script>

<style>
</style>