<template>
  <b-container>
    <br>
    <h4>Listado de estudios</h4>
    <b-table striped hover :items="items"></b-table>

    <br />
    <b-row align-v="stretch">
      <b-col v-for="(item, index) in indice" :key="index">
        <b-card
          title="Card Title"
          img-src="https://picsum.photos/600/300/?image=25"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20rem"
          class="mb-2"
        >
          <b-card-text>
            Some quick example text to build on the card title and make up the
            bulk of the card's content.
          </b-card-text>

          <b-button href="#" variant="primary">Go somewhere</b-button>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>


<script>
export default {
  name: "Home",

  components: {},
  props: {},

  data() {
    return {
      indice: 3,
      items: [
        { nombre:"Juan perez", numero_afiliado: 40, diagnostico: "Dickerson", obra_social: "osde", estado: "Esperando comprobante pago" },
        {nombre:"Juan",  numero_afiliado: 21, diagnostico: "Larsen", obra_social: "osde" , estado: "Esperando comprobante pago"},
        {nombre:"Juan" , numero_afiliado: 89, diagnostico: "Geneva", obra_social: "Medife", estado: "Esperando comprobante pago"},
        {nombre:"Juan", numero_afiliado: 38, diagnostico: "Jami", obra_social: "osde", estado: "Esperando comprobante pago" },
      ],
    };
  },
  mounted() {},
  created() {},
  methods: {},
};
</script>


<style>
</style>