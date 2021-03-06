<template>
    <div class="bar-container" v-bind:class="{moving: moving != 0}">
        <div class="bar"
             v-on:mousedown="mouseDown"
            >
        </div>
        <Preview v-bind:moving="moving" v-on:mouseDown="mouseDown" v-if="scale != '3'" v-bind:leftPos="leftPos" />
        <div class="between">
            <Guider
                 v-if="scale != '3'"
                 v-bind:leftPos="leftPos"
            />
            <ClassList
                 v-if="scale == '0'"
             />
            <Information
                 ref="info"
                 v-else
                 v-bind:information="information"
                 v-bind:scale="scale"
                 v-on:showOverlay="showOverlay($event)"
             />
        </div>
        <Markings 
             v-if="scale != '3'"
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
import Information from './Information.vue'

export default {
    name: 'Bar',
    props: ['scale', 'centerPositions', 'centerFrequencyRanges', 'information'],
    components: {
        Preview,
        Guider,
        Markings,
        ClassList,
        Information,
    },
    data() {
        return {
            moving: 0,
            leftPos: window.innerWidth * 0.045,
            markings: [0,0,0,0,0,0,0,0,0,0,0],
            placements: [0,0,0,0,0,0,0,0,0,0,0],
        }
    },
    mounted() {
        this.movePreview(false);
    },
    methods: {
        showOverlay: function(e) {
            this.$emit('showOverlay', e);
        },
        mouseUp: function() {
            this.moving = 0;
        },
        mouseDown: function(event) {
            event.preventDefault();
            this.$emit('mouseDown');
            switch (event.target.className) {
                case 'bar': 
                case 'preview onLeft': 
                case 'preview onRight': 
                    this.moving = window.innerWidth*.045 + 2;
                    this.movePreview(event);
                    break;
                case 'preview':
                    this.moving = event.layerX + .005*window.innerWidth - 2;
                    break;
            }
        },
        movePreview: function(event) {
            if(event && !this.moving) return;
            if(event) this.leftPos = event.x - this.moving;
            this.$emit('updatePositions', this.leftPos);

            var A = this.centerFrequencyRanges[this.scale][0];
            var B = this.centerFrequencyRanges[this.scale][1];

            var quotient = 10**(Math.floor(Math.log10(A)/3)*3);
            for (var i=0; i<11; i++) {
                var newValue = this.pos_to_freq(A, B, 0.1*i);
                this.markings.splice(i, 1, newValue)
                this.placements.splice(i, 1, this.freq_to_pos(A, B,
                    (newValue / quotient).toFixed(2) * quotient
                ));
            }
        },
        pos_to_freq: function(startFreq, endFreq, pos) {
            return startFreq**(1-pos) * endFreq ** pos;
        },
        freq_to_pos: function(startFreq, endFreq, freq) {
            return Math.log10(freq/startFreq) / Math.log10(endFreq/startFreq);
        },
        movePreviewWithoutUpdating: function(A, B, freq) {
            this.leftPos = this.freq_to_pos(A, B, freq) * .9*window.innerWidth + .045*window.innerWidth;
            this.$refs['info'].move(A);
        },
    },
}
</script>

<style>
.bar-container {
    height: 25%;
}
.bar-container.moving {
    cursor: grabbing;
}
.bar {
    position: relative;
    width: 90%;
    height: 25px;
    border-top: 2px solid black;
    border-bottom: 2px solid black;
    margin: auto;
    cursor: grab;
}
.between {
    position: relative;
    height: 100%;
    width: 90%;
    margin: auto;
}
#visible-preview {
    position: absolute;
    width: 001.328795135%;
    left: 68.56075802%;
    height: 25px;
    transform: translateY(-50%);
    pointer-events: none;
}
.visible_background {
    background-image: url('./../assets/visible.png');
    background-repeat: repeat-y;
}
</style>
