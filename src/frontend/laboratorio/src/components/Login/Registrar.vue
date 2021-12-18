<template>
  <b-container class="bv-example-row">
    <br /><br />
    <div id="container">
      <b-row>
        <b-col cols="2"> </b-col>
        <b-col>
          <b-form action class="form" v-if="show" @submit.prevent="onSubmit">
            <hr />
            <p class="title h3 mt-2 text-center">
              <small>Completa los datos para registrarte</small>
            </p>
            <br />
            <b-row>
              <b-col lg="6">
                <b-form-group
                  id="input-group-1"
                  label="Nombre :"
                  label-for="input-1"
                >
                  <b-form-input
                    id="nombre-1"
                    v-model="usuario.nombre"
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
                    id="apellido-2"
                    v-model="usuario.apellido"
                    placeholder="Ingrese apellido"
                    required
                  ></b-form-input>
                </b-form-group>
              </b-col>
            </b-row>

            <b-row>
              <b-col lg="4">
                <b-form-group
                  id="input-group-n"
                  label="Fecha de Nacimiento:"
                  label-for="input-n"
                >
                  <b-form-input
                    @click="esMayor()"
                    id="nacimiento-n"
                    v-model="usuario.fecha_nacimiento"
                    required
                    type="date"
                  ></b-form-input>
                </b-form-group>
              </b-col>
              <b-col lg="4">
                <b-form-group
                  id="input-group-n"
                  label="Numero de documento:"
                  label-for="input-n"
                >
                  <b-form-input
                    v-model="usuario.dni"
                    type="number"
                    required
                    placeholder="Ingrese el numero de dni"
                  ></b-form-input>
                </b-form-group>
              </b-col>
            </b-row>
            <div v-if="esMayor()">
              <b-row>
                <b-col lg="4">
                  <b-form-group
                    id="input-group-2"
                    label="Numero de Telefono:"
                    label-for="input-2"
                  >
                    <b-form-input
                      type="number"
                      v-model="usuario.telefono"
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
                      v-model="usuario.email"
                      placeholder="Ingrese Email"
                      required
                    ></b-form-input>
                  </b-form-group>
                </b-col>
              </b-row>
              <b-row>
                <b-col>
                  <b-form-group
                    id="input-group-2"
                    label="Calle:"
                    label-for="input-2"
                  >
                    <b-form-input
                      v-model="usuario.calle"
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
                      v-model="usuario.numero"
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
                      v-model="usuario.piso"
                      placeholder="Ingrese Piso"
                      required
                    ></b-form-input>
                  </b-form-group>
                </b-col>
              </b-row>
            </div>
            <div v-else class="rounded">
              <h5>
                <b> Datos del tutor </b>
              </h5>
              <hr />
              <br />
              <b-row
                ><br />
                <b-col lg="6">
                  <b-form-group label="Nombre del tutor :">
                    <b-form-input
                      v-model="usuario.tutor.nombre"
                      type="text"
                      placeholder="Ingrese Nombre del tutor"
                      required
                    ></b-form-input>
                  </b-form-group>
                </b-col>
                <b-col lg="6">
                  <b-form-group
                    id="input-group-2"
                    label="Apellido del tutor :"
                    label-for="input-2"
                  >
                    <b-form-input
                      v-model="usuario.tutor.apellido"
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
                      v-model="usuario.tutor.telefono"
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
                      v-model="usuario.tutor.email"
                      placeholder="Ingrese Email del tutor"
                      required
                    ></b-form-input>
                  </b-form-group>
                </b-col>
              </b-row>

              <b-row>
                <b-col>
                  <b-form-group
                    id="input-group-2"
                    label="Calle:"
                    label-for="input-2"
                  >
                    <b-form-input
                      v-model="usuario.tutor.calle"
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
                      v-model="usuario.tutor.numero"
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
                      v-model="usuario.tutor.piso"
                      placeholder="Ingrese Piso"
                      required
                    ></b-form-input>
                  </b-form-group>
                </b-col>
              </b-row>
            </div>

            <div>
              <b-row class="pb-2">
                <b-col class="text-center pt-3">
                  <b-button
                    style="width: 200px"
                    type="submit"
                    variant="outline-primary"
                    >Crear</b-button
                  >
                </b-col>
              </b-row>
            </div>
          </b-form>
        </b-col>
      </b-row>
    </div>
  </b-container>
</template>

<script>
import PacientesService from "@/services/PacientesService.js";

export default {
  components: {},

  props: {},

  data() {
    return {
      show: true,
      usuario: {
        nombre: null,
        apellido: null,
        dni: null,
        email: null,
        telefono: null,
        calle: 1,
        numero: 2,
        piso: 3,
        direccion: null,
        fecha_nacimiento: new Date().format("dd-mm-yyyy"),
        tutor: {
          nombre: null,
          apellido: null,
          email: null,
          telefono: null,
          direccion: null,
        },
      },
    };
  },

  methods: {
    esMayor() {
      let hoy = new Date();
      let cumpleanos = new Date(this.usuario.fecha_nacimiento);
      let edad = hoy.getFullYear() - cumpleanos.getFullYear();
      let m = hoy.getMonth() - cumpleanos.getMonth();
      if (m < 0 || (m === 0 && hoy.getDate() < cumpleanos.getDate())) {
        edad--;
      }
      return edad > 17 ? true : false;
    },
    async onSubmit() {
      try {
        console.log(this.usuario);
        this.armarDireccion()
        let response = await PacientesService.registrarPaciente(this.usuario)
        console.log(response)
      } catch (error) {
        console.log(error);
      }
    },
    armarDireccion(){
      this.usuario.direccion= this.usuario.calle + this.usuario.numero + this.usuario.piso
    }
  },
  computed: {},

  mounted() {},
};
</script>


<style>
@import url("https://fonts.googleapis.com/css?family=Montserrat&display=swap");
p,
b,
label,
body {
  font-family: "Roboto", sans-serif !important;
}
#container {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
</style>