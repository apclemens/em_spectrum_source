<template>
    <div class="bar-container" v-on:mousemove="movePreview">
        <div class="bar"></div>
        <img id="visible-preview" v-if="scale == '0'" src="./../assets/visible.png">
        <Preview v-bind:leftPos="leftPos"/>
        <div class="between">
        <Guider
             v-bind:leftPos="leftPos"
        />
        <ClassList
             v-if="scale == '0'"
         />
        </div>
        <Markings 
             v-bind:centerPos="centerPositions[scale]"
             v-bind:centerFrequencyRange="centerFrequencyRanges[scale]"
             v-bind:markings="markings"
             v-bind:placements="placements"
        />
    </div>
</template>

<script>
import Preview from './Preview.vue'
import Guider from './Guider.vue'
import Markings from './Markings.vue'
import ClassList from './ClassList.vue'

export default {
    name: 'Bar',
    props: ['scale', 'centerPositions', 'centerFrequencyRanges'],
    components: {
        Preview,
        Guider,
        Markings,
        ClassList,
    },
    data() {
        return {
            leftPos: 0,
            markings: [0,0,0,0,0,0,0,0,0,0,0],
            placements: [0,0,0,0,0,0,0,0,0,0,0],
        }
    },
    methods: {
        movePreview: function(event) {
            this.leftPos = event.x - .045*window.innerWidth;
            this.$emit('updatePositions', this.leftPos);

            var A = this.centerFrequencyRanges[this.scale][0];
            var B = this.centerFrequencyRanges[this.scale][1];

            for (var i=0; i<11; i++) {
                var newValue = this.pos_to_freq(A, B, 0.1*i);
                this.markings.splice(i, 1, newValue)
                this.placements.splice(i, 1, this.freq_to_pos(A, B, newValue.toExponential(2)));
            }
        },
        pos_to_freq: function(startFreq, endFreq, pos) {
            return startFreq**(1-pos) * endFreq ** pos;
        },
        freq_to_pos: function(startFreq, endFreq, freq) {
            return Math.log10(freq/startFreq) / Math.log10(endFreq/startFreq);
        },
    },
}
</script>

<style>
.bar {
    position: relative;
    width: 90%;
    height: 5px;
    background-color: black;
    margin: auto;
}
.between {
    position: relative;
    height: 200px;
    width: 90%;
    margin: auto;
}
#visible-preview {
    position: absolute;
    width: 001.328795135%;
    left: 68.56075802%;
    height: 25px;
    transform: translateY(-50%);
}
</style>
