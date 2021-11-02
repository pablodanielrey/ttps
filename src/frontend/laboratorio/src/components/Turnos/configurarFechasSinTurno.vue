<template>
    <b-container>
        <div>
        Fecha
        <vue-cal
            class="vuecal--date-picker"
            xsmall
            hide-view-selector
            :time="false"
            :transitions="false"
            active-view="month"
            :disable-views="['week']"
            style="width: 210px;height: 230px">
        </vue-cal>

        <button>agregar</button>
        </div>

        
        <div>
            <b-table striped hover :items="items"></b-table>
        </div>

        <button>aceptar</button>

    </b-container>
</template>

<script>
import VueCal from 'vue-cal'
import 'vue-cal/dist/vuecal.css'

export default {
    components: { VueCal },
data() {
      return {
        items: [
          { Fecha: "02/12/2021", eliminar:'X' },
          { Fecha: "03/11/2021", eliminar:'X' },
        ]
      }
    }
}
</script>

<style>

</style>