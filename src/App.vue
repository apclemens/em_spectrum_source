<template>
  <div id="app">
      <Markings scale="0"/>
    <Bar ref="0" scale="0" v-on:mouseDown="mouseDown(0)" v-bind:centerPositions="centerPositions" v-bind:centerFrequencyRanges="centerFrequencyRanges" v-bind:information="information[0]" v-on:updatePositions="updatePos($event, 0)"/>
    <Bar ref="1" scale="1" v-on:mouseDown="mouseDown(1)" v-bind:centerPositions="centerPositions" v-bind:centerFrequencyRanges="centerFrequencyRanges" v-bind:information="information[1]" v-on:updatePositions="updatePos($event, 1)"/>
    <Bar ref="2" scale="2" v-on:mouseDown="mouseDown(2)" v-bind:centerPositions="centerPositions" v-bind:centerFrequencyRanges="centerFrequencyRanges" v-bind:information="information[2]" v-on:updatePositions="updatePos($event, 2)"/>
    <Bar ref="3" scale="3" v-on:mouseDown="mouseDown(3)" v-bind:centerPositions="centerPositions" v-bind:centerFrequencyRanges="centerFrequencyRanges" v-bind:information="information[3]" v-on:updatePositions="updatePos($event, 3)"/>
  </div>
</template>

<script>
import Bar from './components/Bar.vue'
import Markings from './components/Markings.vue'
import BandInfo from './components/BandInfo.vue'

export default {
  name: 'app',
  components: {
    Bar,
    Markings,
  },
  mounted() {
      var ths = this;

      document.addEventListener('mouseup', function() {
          this.moving = -1;
          for(var ref=0; ref < 4; ref++) {
              ths.$refs[ref].mouseUp();
          }
      })
      document.addEventListener('mousemove', function(event) {
          if (ths.moving == -1) return;
          ths.$refs[ths.moving].movePreview(event);
      })

      console.log(this.bi);
//      var xhr = new XMLHttpRequest();
//      xhr.open('GET', 'https://rawgit.com/apclemens/em_spectrum_source/master/src/assets/info/uhf-us2.json', true);
//      xhr.responseType = 'json';
//      xhr.onload = function() {
//          var status = xhr.status;
//          if (status === 200) {
//              var data = xhr.response.uhfus;
//              var band;
//              for (var i=0; i<data.length; i++) {
//                  band = data[i];
//                  ths.information[band.bar].push(band);
//              }
//          }
//      };
//      xhr.send();
  },
  data() {
      return {
          moving: -1,
          centerPositions: [0, 0, 0, 0],
          centerFrequencyRanges: [[3e-1, 3e1], [1, 1], [1, 1], [1, 1]],
          information: BandInfo.data().information,
      }
  },
  methods: {
      mouseDown: function(i) {
          this.moving = i;
      },
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
          if (scale != 3) { // update box location below
              this.$refs[scale+1].movePreviewWithoutUpdating(
                this.centerFrequencyRanges[scale][0],
                this.centerFrequencyRanges[scale][1],
                this.centerFrequencyRanges[scale+1][0]
              );
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
    overflow: hidden;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
