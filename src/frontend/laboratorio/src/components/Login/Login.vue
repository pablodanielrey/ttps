<template>
  <div class="contenedor1">
    <br />
    <div class="wrapper1">
      <b-row class="h-100 justify-content-center align-items-center">
        <b-col id="columnaImgLogin" cols="7">
          <div>
            <img
              src="@/assets/lablogin.png"
              class="rounded"
              alt="..."
              id="imgLaboratorio"
            /></div
        ></b-col>
        <b-col sm="10" md="8" xl="4" class="base-box m-2">
          <div class="">
            <div class="text-center">
              <p>¡Hola! Ingresá tu usuario y contraseña</p>
            </div>
            <div class="text-center">
              <p class="title h3 mt-2 text-center">Iniciar Sesion</p>
            </div>
            <hr />
            <b-alert v-if="userIncorrecto" show variant="danger"
              >Usuario o contraseña incorrectos,por favor vuelva a ingresar los
              datos</b-alert
            >
            <b-alert show variant="danger" v-if="error">{{ error }}</b-alert>

            <b-form @submit.prevent="login">
              <b-form-group id="input-group-1">
                <b-form-input
                  id="usuario"
                  v-model="credenciales.usuario"
                  type="text"
                  autocomplete="username"
                  required
                  placeholder="Usuario"
                  class="line"
                ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-2">
                <b-form-input
                  id="password"
                  v-model="credenciales.clave"
                  type="password"
                  required
                  autocomplete="current-password"
                  placeholder="Ingresa la contraseña"
                  class="line"
                ></b-form-input>
              </b-form-group>
              <hr />
              <b-form-group class="text-center">
                <b-button type="submit" block variant="primary" v-if="ingresar"
                  >Ingresar
                </b-button>

                <div class="text-center" v-if="!ingresar">
                  <b-spinner
                    variant="primary"
                    label="Text Centered"
                  ></b-spinner>
                </div>
              </b-form-group>
              <b-form-group class="text-center">
                <b-button
                  block
                  @click="$router.push('registrar')"
                  variant="outline-info"
                  >Crear cuenta
                </b-button>
              </b-form-group>
              <div class="text-center"></div>
            </b-form>
          </div>
        </b-col>
      </b-row>
    </div>
  </div>
</template>

<script>
import LoginService from "@/services/LoginService";
import { mapMutations } from "vuex";
export default {
  name: "Login",
  props: {},
  data() {
    return {
      userIncorrecto: false,
      ingresar: true,
      credenciales: {
        usuario: "",
        clave: "",
      },
      error: "",
    };
  },
  created() {},
  methods: {
     ...mapMutations([
    
      "setPermisos",
    
    ]),
    home() {
      this.$router.push("/");
    },

    async login() {
      try {
        let response = await LoginService.login_api(
          this.credenciales.usuario,
          this.credenciales.clave
        );
        if (response.data.cambiar_clave) {
          this.$router.push({
            name: "cambiarClave",
          });
          return
        }
        console.log("rta");
        console.log(response.data.cambiar_clave);

        this.setPermisos(response.data.permisos);
        this.$router.push({
          name: "home",
        });
      } catch (error) {
        this.userIncorrecto = true;
        console.log("catch");
        console.log(error.detail);
      }
    },
  },
};
</script>

<style scoped>
@media (max-width: 600px) {
  #columnaImgLogin {
    visibility: hidden;
  }
}
</style>

