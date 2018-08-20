<template>
  <div id="app">
      <Markings scale="0"/>
    <Bar scale="0" v-bind:centerPositions="centerPositions" v-on:updatePositions="updatePos($event, 0)"/>
    <Bar scale="1" v-bind:centerPositions="centerPositions" v-on:updatePositions="updatePos($event, 1)"/>
    <Bar scale="2" v-bind:centerPositions="centerPositions" v-on:updatePositions="updatePos($event, 2)"/>
    <Bar scale="3" v-bind:centerPositions="centerPositions" v-on:updatePositions="updatePos($event, 3)"/>
  </div>
</template>

<script>
import Bar from './components/Bar.vue'
import Markings from './components/Markings.vue'

export default {
  name: 'app',
  components: {
    Bar,
    Markings,
  },
  data() {
      return {
          centerPositions: [0, 0, 0, 0],
      }
  },
  methods: {
      updatePos: function(event, scale) {
          this.centerPositions[scale] = event / (0.9 * window.innerWidth);
      }
  }
}

function pos_to_freq(pos) {
    return 10**(pos*20)*3;
}

function freq_to_pos(freq) {
    return Math.log10(freq/3)/20;
}
</script>

<style>
body {
    margin: 0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
