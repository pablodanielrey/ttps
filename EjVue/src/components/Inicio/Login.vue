<template>
  <div class="">
    <div class="text-center">
      <p>¡Hola! Ingresá tu e‑mail y contraseña</p>
    </div>
    <div class="text-center">
      <p class="title h3 mt-2 text-center">Iniciar Sesion</p>
    </div>
    <hr />
    <b-alert show variant="danger" v-if="error">{{ error }}</b-alert>

    <b-form @submit.prevent="login">
      <b-form-group id="input-group-1">
        <b-form-input
          id="email"
          v-model="form.email"
          type="email"
          autocomplete="username"
          required
          placeholder="Direccion de correo electronico"
          class="line"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2">
        <b-form-input
          id="password"
          v-model="form.password"
          type="password"
          required
          autocomplete="current-password"
          placeholder="Ingresa la contraseña"
          class="line"
        ></b-form-input>
      </b-form-group>
      <hr />
      <b-form-group class="text-center">
        <b-button type="submit" block variant="primary" v-if="form.ingresar"
          >Ingresar
        </b-button>

        <div class="text-center" v-if="!form.ingresar">
          <b-spinner variant="primary" label="Text Centered"></b-spinner>
        </div>
      </b-form-group>
      <b-form-group class="text-center">
        <b-button
          block
          @click="$router.push('registrar')"
          variant="outline-light"
          >Crear cuenta
        </b-button>
      </b-form-group>
      <div class="text-center"></div>
      <b-button @click="home()" variant="outline-secondary">
        <b-icon icon="arrow-left-short"></b-icon>Volver
      </b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  name: "Login",
  props: {},
  data() {
    return {
      form: {
        email: "",
        password: "",
        ingresar: true,
      },
      error: "",
    };
  },
  created() {},
  methods: {
    home() {
      this.$router.push("/");
    },

    async login() {
      console.log("entra login");
    },
  },
};
</script>

<style scoped>
</style>

