<template>
  <b-container>
    <div>
      <b-button
        title="Bajar factura"
        variant="outline-success"
        @click="bajarFactura()"
      >
        <b-icon icon="download" aria-hidden="true"></b-icon
      ></b-button>
      <br>
      <div>
        <div class="counter">Quedan {{ counter }} dias, para realizar el pago del estudio</div>
      </div>
    </div>
  </b-container>
</template>


<script>
export default {
  components: {},

  props: {},
  created() {
       let result = this.$crontab.addJob({
      name: 'counter',
      interval: {
        day: '/31',
      },
      job: this.countUp
    })
    console.log(result)
  },
  data() {
    return {
      file1: [],
      counter: 31
    };
  },

  methods: {
    bajarFactura() {},
     countUp () {
      this.counter -= 1
    }
  },
  computed: {},

  mounted() {},
};
</script>

