<template>
  <div id="app">
      <Markings scale="0"/>
    <Bar scale="0" v-bind:centerPositions="centerPositions" v-bind:centerFrequencyRanges="centerFrequencyRanges" v-on:updatePositions="updatePos($event, 0)"/>
    <Bar scale="1" v-bind:centerPositions="centerPositions" v-bind:centerFrequencyRanges="centerFrequencyRanges" v-on:updatePositions="updatePos($event, 1)"/>
    <Bar scale="2" v-bind:centerPositions="centerPositions" v-bind:centerFrequencyRanges="centerFrequencyRanges" v-on:updatePositions="updatePos($event, 2)"/>
    <Bar scale="3" v-bind:centerPositions="centerPositions" v-bind:centerFrequencyRanges="centerFrequencyRanges" v-on:updatePositions="updatePos($event, 3)"/>
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
          centerFrequencyRanges: [[3e-1, 3e1], [1, 1], [1, 1], [1, 1]],
      }
  },
  methods: {
      updatePos: function(event, scale) {
          this.centerPositions[scale] = event / (0.9 * window.innerWidth);
          if (scale == 0) {
              this.centerFrequencyRanges[0] = [pos_to_freq(3e0, 3e20, this.centerPositions[0]-.05), pos_to_freq(3e0, 3e20, this.centerPositions[0]+.05)];
          } else {
              this.centerFrequencyRanges[scale] = 
                  [
                      pos_to_freq(this.centerFrequencyRanges[scale-1][0], this.centerFrequencyRanges[scale-1][1], this.centerPositions[scale]-0.05), 
                      pos_to_freq(this.centerFrequencyRanges[scale-1][0], this.centerFrequencyRanges[scale-1][1], this.centerPositions[scale]+0.05)
                  ]
          }
      }
  }
}

function pos_to_freq(startFreq, endFreq, pos) {
    return startFreq**(1-pos) * endFreq ** pos;
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
