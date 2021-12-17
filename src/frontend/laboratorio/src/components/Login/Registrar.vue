<template>
  <div class="contenedor1">
    <br /><br /><br />
    <div class="wrapper1">
      <b-row class="h-100 justify-content-center align-items-center">
        
        <br>
      </b-row>
      <br>
      <b-container>
        <br />
        <b-form v-if="show">
          <b-card
            bg-variant="light"
            header="Datos personales"
            class="text-center"
          >
            <b-row>
              <b-col lg="6">
                <b-form-group
                  id="input-group-1"
                  label="Nombre :"
                  label-for="input-1"
                >
                  <b-form-input
                    id="input-1"
                    v-model="form.nombre"
                    type="text"
                    placeholder="Ingrese Nombre "
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
              <b-col lg="6">
                <b-form-group
                  id="input-group-2"
                  label="Apellido:"
                  label-for="input-2"
                >
                  <b-form-input
                    id="input-2"
                    v-model="form.apellido"
                    placeholder="Ingrese apellido"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col lg="4" class="my-1">
                <b-form-group
                  id="input-group-n"
                  label="Fecha de Nacimiento:"
                  label-for="input-n"
                >
                  <b-form-datepicker
                    id="input-n"
                    v-model="form.nacimiento"
                    required
                  ></b-form-datepicker>
                </b-form-group>
              </b-col>
              <b-col lg="4" class="my-1">
                <b-form-group
                  id="input-group-n"
                  label="Numero de documento:"
                  label-for="input-n"
                >
                  <b-form-input
                    id="input-n"
                    v-model="form.DNI"
                    type="number"
                    required
                    placeholder="Ingrese el numero de dni"
                  ></b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <div v-if="selected == 1">
              <b-row>
                <b-col lg="4">
                  <b-form-group
                    id="input-group-2"
                    label="Numero de Telefono:"
                    label-for="input-2"
                  >
                    <b-form-input
                      type="number"
                      id="input-2"
                      v-model="form.Telefono"
                      placeholder="Ingrese Telefono"
                      required
                    ></b-form-input>
                  </b-form-group>
                </b-col>
                <b-col lg="4">
                  <b-form-group
                    id="input-group-2"
                    label="Direccion de Email:"
                    label-for="input-2"
                  >
                    <b-form-input
                      id="input-2"
                      v-model="form.Email"
                      placeholder="Ingrese Email"
                      required
                    ></b-form-input>
                  </b-form-group>
                </b-col>
              </b-row>
            </div>

            <div v-if="selected == 1">
              <b-card bg-variant="light" header="Direccion" class="text-center">
                <br />
                <b-row>
                  <b-col>
                    <b-form-group
                      id="input-group-2"
                      label="Calle:"
                      label-for="input-2"
                    >
                      <b-form-input
                        id="input-2"
                        v-model="form.Calle"
                        placeholder="Ingrese Calle"
                        required
                      ></b-form-input>
                    </b-form-group>
                  </b-col>
                  <b-col>
                    <b-form-group
                      id="input-group-2"
                      label="Numero:"
                      label-for="input-2"
                    >
                      <b-form-input
                        id="input-2"
                        v-model="form.numero"
                        placeholder="Ingrese numero"
                        required
                      ></b-form-input>
                    </b-form-group>
                  </b-col>
                  <b-col>
                    <b-form-group
                      id="input-group-2"
                      label="Piso:"
                      label-for="input-2"
                    >
                      <b-form-input
                        id="input-2"
                        v-model="form.Piso"
                        placeholder="Ingrese Piso"
                        required
                      ></b-form-input>
                    </b-form-group>
                  </b-col>
                </b-row>
              </b-card>
            </div>
            <div v-if="selected == 2">
              <b-card
                bg-variant="light"
                header="Datos del tutor"
                class="text-center"
              >
                <b-row>
                  <b-col class="my-1">
                    <b-form-group
                      id="input-group-1"
                      label="Nombre del tutor :"
                      label-for="input-1"
                    >
                      <b-form-input
                        id="input-1"
                        v-model="form.nombre"
                        type="text"
                        placeholder="Ingrese Nombre del tutor"
                        required
                      ></b-form-input>
                    </b-form-group>
                  </b-col>
                  <b-col>
                    <b-form-group
                      id="input-group-2"
                      label="Apellido del tutor :"
                      label-for="input-2"
                    >
                      <b-form-input
                        id="input-2"
                        v-model="form.apellido"
                        placeholder="Ingrese apellido del tutor"
                        required
                      ></b-form-input>
                    </b-form-group>
                  </b-col>
                </b-row>
                <b-row>
                  <b-col lg="4">
                    <b-form-group
                      id="input-group-2"
                      label="Telefono deltutor:"
                      label-for="input-2"
                    >
                      <b-form-input
                        type="number"
                        id="input-2"
                        v-model="form.Telefono"
                        placeholder="Ingrese Telefono del tutor"
                        required
                      ></b-form-input>
                    </b-form-group>
                  </b-col>
                  <b-col lg="4">
                    <b-form-group
                      id="input-group-2"
                      label="Email del tutor:"
                      label-for="input-2"
                    >
                      <b-form-input
                        id="input-2"
                        v-model="form.Email"
                        placeholder="Ingrese Email del tutor"
                        required
                      ></b-form-input>
                    </b-form-group>
                  </b-col>
                </b-row>
                <b-card
                  bg-variant="light"
                  header="Direccion del tutor"
                  class="text-center"
                >
                  <br />
                  <b-row>
                    <b-col>
                      <b-form-group
                        id="input-group-2"
                        label="Calle:"
                        label-for="input-2"
                      >
                        <b-form-input
                          id="input-2"
                          v-model="form.Calle"
                          placeholder="Ingrese Calle"
                          required
                        ></b-form-input>
                      </b-form-group>
                    </b-col>
                    <b-col>
                      <b-form-group
                        id="input-group-2"
                        label="Numero:"
                        label-for="input-2"
                      >
                        <b-form-input
                          id="input-2"
                          v-model="form.numero"
                          placeholder="Ingrese numero"
                          required
                        ></b-form-input>
                      </b-form-group>
                    </b-col>
                    <b-col>
                      <b-form-group
                        id="input-group-2"
                        label="Piso:"
                        label-for="input-2"
                      >
                        <b-form-input
                          id="input-2"
                          v-model="form.Piso"
                          placeholder="Ingrese Piso"
                          required
                        ></b-form-input>
                      </b-form-group>
                    </b-col>
                  </b-row>
                </b-card>
              </b-card>
            </div>
          </b-card>
        </b-form>

        <div>
          <b-row class="pb-2">
            <b-col class="text-center pt-3">
              <b-button style="width: 165px" variant="outline-success"
                >Guardar</b-button
              >
            </b-col>
          </b-row>
        </div>
      </b-container>
    </div>
  </div>
</template>

<script>
export default {
  components: {},

  props: {},

  data() {
    return {
      selected: 2, // Must be an array reference!
      show: true,
      form: {},

      options: [
        { text: "Soy mayor de 18 años", value: 1 },
        { text: "Soy menor de 18 años", value: 2 },
      ],
    };
  },

  methods: {},
  computed: {},

  mounted() {},
};
</script>


<style>
</style>