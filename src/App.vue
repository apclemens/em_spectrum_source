<template>
  <div id="app">
      <div ref="overlay" id="overlay" v-on:click="clearOverlay()" v-bind:style="{display: overlayInformation ? 'block' : 'none'}"><iframe id="innerOverlay" :src="overlayInformation"></iframe></div>
      <Markings scale="0"/>
    <Bar ref="0" scale="0" v-on:showOverlay="showOverlay($event)" v-on:mouseDown="mouseDown(0)" v-bind:centerPositions="centerPositions" v-bind:centerFrequencyRanges="centerFrequencyRanges" v-bind:information="information[0]" v-on:updatePositions="updatePos($event, 0)"/>
    <Bar ref="1" scale="1" v-on:showOverlay="showOverlay($event)" v-on:mouseDown="mouseDown(1)" v-bind:centerPositions="centerPositions" v-bind:centerFrequencyRanges="centerFrequencyRanges" v-bind:information="information[1]" v-on:updatePositions="updatePos($event, 1)"/>
    <Bar ref="2" scale="2" v-on:showOverlay="showOverlay($event)" v-on:mouseDown="mouseDown(2)" v-bind:centerPositions="centerPositions" v-bind:centerFrequencyRanges="centerFrequencyRanges" v-bind:information="information[2]" v-on:updatePositions="updatePos($event, 2)"/>
    <Bar ref="3" scale="3" v-on:showOverlay="showOverlay($event)" v-on:mouseDown="mouseDown(3)" v-bind:centerPositions="centerPositions" v-bind:centerFrequencyRanges="centerFrequencyRanges" v-bind:information="information[3]" v-on:updatePositions="updatePos($event, 3)"/>
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
      document.addEventListener('keyup', function(event) {
          if (event.keyCode == 27) {
              ths.clearOverlay();
          }
      })
  },
  data() {
      var centerPos = window.innerWidth * 0.045;
      return {
          overlayInformation: '',
          moving: -1,
          centerPositions: [centerPos, centerPos, centerPos, centerPos],
          centerFrequencyRanges: [[3e0, 3e2], [3e0, 3e1], [3e0, 3*(10**(1/2))], [3e0, 3*(10**(1/4))]],
          information: BandInfo.data().information,
      }
  },
  methods: {
      clearOverlay: function() {
          this.overlayInformation = '';
      },
      showOverlay: function(data) {
          this.overlayInformation = data;
      },
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
@import url('https://fonts.googleapis.com/css?family=Roboto+Mono|Special+Elite|Merriweather|Raleway');

h1 {
    margin: 0;
    height: 10%;
    text-align: center;
    font-size: 10vh;
    font-family: 'Special Elite', cursive;
}
html, body {
    height: 100%;
}
body {
    margin: 0;
    overflow: hidden;
}
#app {
    height: 90%;
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    color: #2c3e50;
}
#overlay {
    position: fixed;
    display: none;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 2;
    cursor: pointer;
    margin: auto;
    background-color: rgba(0, 0, 0, .5);
}
#innerOverlay {
    width: 75%;
    height: 75%;
    margin: auto;
    display: block;
    margin-top: 12.5vh;
}
</style>
