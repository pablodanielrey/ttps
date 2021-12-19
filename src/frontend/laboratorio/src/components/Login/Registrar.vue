<template>
  <div class="bv-example-row">
    <br /><br />
    <div>
      <b-row>
        <br />
        <b-col id="columnaImg" cols="5">
          <div>
            <img
              src="@/assets/lab1.png"
              class="rounded"
              alt="..."
              id="imgLaboratorio"
            /></div
        ></b-col>
        <b-col>
          <b-form action class="form" v-if="show" @submit.prevent="onSubmit">
            <hr />
            <p class="title mt-2" id="textoRegistro">
              <b> Completa los datos para registrarte</b><br />
              <small> Recorda que si sos menor tendras un tutor a cargo</small>
              <b-alert v-if="this.showCreated" show variant="success"
                >Su usuario se creo con exito, recorda que te enviamos un email
                con los datos para poder ingresar en el sistema</b-alert
              >
                <b-alert v-if="this.showError" show variant="danger"
                >{{this.error}}</b-alert
              >
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
                  label="DNI:"
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
                      type="email"
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
              <h6>
                <b> Datos del tutor </b>
              </h6>
              <hr />
              <br />
              <b-row
                ><br />
                <b-col lg="6">
                  <b-form-group label="Nombre del tutor :">
                    <b-form-input
                      v-model="tutor.tutor.nombre"
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
                      v-model="tutor.tutor.apellido"
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
                      v-model="tutor.tutor.telefono"
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
                      v-model="tutor.tutor.email"
                      placeholder="Ingrese Email del tutor"
                      required
                      type="email"
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
                      v-model="tutor.tutor.calle"
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
                      v-model="tutor.tutor.numero"
                      placeholder="Ingrese numero"
                      required
                      type="number"
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
                      v-model="tutor.tutor.piso"
                      placeholder="Ingrese Piso"
                      required
                      type="number"
                    ></b-form-input>
                  </b-form-group>
                </b-col>
              </b-row>
            </div>

            <div>
              <b-row class="pb-2">
                <b-col class="text-center pt-3">
                  <b-button
                    style="width: 250px"
                    type="submit"
                    variant="outline-primary"
                    >Crear</b-button
                  >
                </b-col>
              </b-row>
              <b-col class="text-left">
                <router-link to="/login"
                  ><b-icon icon="arrow-left-circle"></b-icon
                ></router-link>
              </b-col>
            </div>
          </b-form>
        </b-col>
        <b-col cols="2"></b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
 import PacientesService from "@/services/PacientesService.js";
 
export default {
  components: {},

  props: {},

  data() {
    return {
      show: true,
      showCreated: false,
      showError:false,
      error:null,
      usuario: {
        nombre: null,
        apellido: null,
        dni: null,
        email: null,
        telefono: null,
        calle: null,
        numero: null,
        piso: null,
        direccion: null,
        fecha_nacimiento: new Date().format("dd-mm-yyyy"),
      },
      tutor: {
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
        this.armarDireccion();
        let datos = this.armarArray();
        console.log(datos)
        let response = await PacientesService.registrarPaciente(datos);
        console.log(response);
        if (response.status == 201) {
          this.showCreated = true;
          this.limpiarCampos();
        }
      } catch (error) {
        this.showError = true;
        this.error= error.response.data
        console.log(error.response.data);
      }
    },
    armarDireccion() {
      this.usuario.direccion =
        this.usuario.calle +
        " " +
        this.usuario.numero +
        " " +
        this.usuario.piso;
    },
    armarDireccionTutor(calle, numero, piso) {
      return calle + " " + numero + " " + piso;
    },
    armarArray() {
      if (this.esMayor()) {
        return this.usuario;
      } else {
        let datos = {};
        datos = {
          usuario: {
            nombre: this.usuario.nombre,
            apellido: this.usuario.apellido,
            dni: this.usuario.dni,
            fecha_nacimiento: this.usuario.fecha_nacimiento,
            tutor: {
              tutor: {
                nombre: this.tutor.tutor.nombre,
                apellido: this.tutor.tutor.apellido,
                email: this.tutor.tutor.email,
                telefono: this.tutor.tutor.telefono,
                calle: this.tutor.tutor.calle,
                numero: this.tutor.tutor.numero,
                piso: this.tutor.tutor.piso,
                direccion: this.armarDireccionTutor(
                  this.tutor.tutor.calle,
                  this.tutor.tutor.numero,
                  this.tutor.tutor.piso
                ),
              },
            },
          },
        };
        return datos;
      }
    },
    limpiarCampos() {
      (this.usuario.nombre = null),
        (this.usuario.apellido = null),
        (this.usuario.dni = null),
        (this.usuario.email = null),
        (this.usuario.telefono = null),
        (this.usuario.calle = null),
        (this.usuario.numero = null),
        (this.usuario.piso = null),
        (this.usuario.direccion = null),
        (this.usuario.fecha_nacimiento = new Date().format("dd-mm-yyyy")),
        (this.tutor.tutor.nombre = null),
        (this.tutor.tutor.apellido = null),
        (this.tutor.tutor.email = null),
        (this.tutor.tutor.telefono = null),
        (this.tutor.tutor.direccion = null);
    },
  },
  computed: {},

  mounted() {},
};
</script>


<style>
@media (max-width: 600px) {
  #columnaImg {
    visibility: hidden;
  }
}
@import url("https://fonts.googleapis.com/css?family=Montserrat&display=swap");
p,
b,
label,
body,
a {
  font-family: "Roboto", sans-serif !important;
}
#container {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
#textoRegistro {
  text-align: left;
}
#imgLaboratorio {
  width: 100%;
  height: 80%;
}
</style>