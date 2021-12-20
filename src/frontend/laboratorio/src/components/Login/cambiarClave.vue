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
              <p>
                ¡Bienvenido!Para mayor proteccion deberas cambiar la contraseña
                por una nueva
              </p>
              <p class="title mt-2" id="textoRegistro">
                <b-alert v-if="this.show" show variant="danger">{{
                  this.message
                }}</b-alert>
              </p>
            </div>
            <div class="text-center">
              <p class="title h3 mt-2 text-center">Cambiar contraseña</p>
            </div>
            <hr />
            <b-form @submit.prevent="cambiarClave">
              <b-form-group id="input-group-1">
                <b-form-input
                  id="claveAnterior"
                  v-model="claveAnterior"
                  type="password"
                  autocomplete="username"
                  required
                  placeholder="Ingrese contraseña anterior"
                  class="line"
                ></b-form-input>
              </b-form-group>

              <b-form-group id="input-group-1">
                <b-form-input
                  id="usuario"
                  v-model="clave"
                  type="password"
                  autocomplete="username"
                  required
                  placeholder="Ingrese contraseña"
                  class="line"
                ></b-form-input>
              </b-form-group>
              <hr />
              <b-form-group class="text-center">
                <b-button type="submit" block variant="primary"
                  >Cambiar contraseña
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
import LoginService from "@/services/LoginService.js";

export default {
  data() {
    return {
      clave: null,
      claveAnterior: null,
      show: false,
      message: null,
    };
  },
  methods: {
    async cambiarClave() {
      try {
        let data = {
          clave_anterior: this.claveAnterior,
          clave_nueva: this.clave,
        };
        await LoginService.cambiarClave(data);
          window.localStorage.removeItem("credenciales");
        this.$router.push({
          name: "Login",
        });
      
      } catch (error) {
        this.show = true;
        this.message = error.response.data[0];
      }
    },
  },
};
</script>

<style>
</style>