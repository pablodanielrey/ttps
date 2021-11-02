<template>
    <b-container>
        A Partir de:
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

        <b-container>
            Hora Inicio
            <input name='hora_inicio'/>
            Hora Fin
            <input name='hora_fin'/>
            Frecuencia
            <input name='frecuencia'/>
            <button>agregar</button>
        </b-container>


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
          { hora_inicio: "09:00", hora_fin: '13:00', frecuencia: '15 min' },
          { hora_inicio: "14:00", hora_fin: '17:00', frecuencia: '20 min' },
        ]
      }
    }
}
</script>

<style>

</style>