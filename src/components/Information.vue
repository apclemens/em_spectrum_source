<template>
    <div class="information" v-bind:style="{transform: 'translateX('+(100*translate)+'%)'}"
    >
        <div class="visible"
             v-bind:style="{
                left: 70.77313409838453*(10**scale) + '%',
                width: (71.98825191232318*(10**scale) - 70.77313409838453*(10**scale)) + '%',
             }"
            >
        </div>
        <div class="band" v-for="(band, index) in information" v-bind:class="{tick: band.start == band.end}" v-bind:key="index"
            v-bind:style="{
                 left: frequency_to_position_information(band.start, scale)*100 + '%',
                 width: (frequency_to_position_information(band.end, scale)*100 - frequency_to_position_information(band.start, scale)*100) + '%'
            }"
        >
            <div class="info"
                 v-bind:style="{left: getLeftPos(band.start) + 'vw'}"
            >
                {{band.title}}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Information',
    props: ['information', 'scale'],
    data() {
        return {
            translate: 0,
        }
    },
    methods: {
        getLeftPos(startFreq) {
            var startPos = this.frequency_to_position_information(startFreq, this.scale);
            if (startPos + this.translate > 0) return 0;
            return -90*(startPos + this.translate);
        },
        frequency_to_position_information: function(frequency, scale) {
            return Math.log10(frequency/3)/20 * 10**scale;
        },
        move: function(A) {
            this.translate = Math.log10(A/3)/20 * 10**this.scale * (-1);
        }
    },
}

</script>

<style>
.information {
    position: absolute;
    width: 100%;
    height: 100%;
    left: 0;
}
.visible {
    position: absolute;
    background-size: 100%;
    height: calc(100% - 29px);
    background-image: url('./../assets/visible.png');
    background-repeat: repeat-y;
}
.small-visible {
    background-image: url('./../assets/visible-small.png');
}
.band {
    position: absolute;
    display: inline-block;
    background-color: rgba(255,0,0,.5);
    top: 0;
    border: 2px solid black;
    box-sizing: border-box;
    overflow: hidden;
    z-index: 0;
    height: 30px;
}
.band:hover {
    overflow: visible;
    z-index: 2;
}
.band:hover .info {
    margin: auto;
    position: relative;
    min-width: 200px !important;
    background-color: red;
    z-index: 1;
}
.info {
    pointer-events: none;
    position: relative;
    display: inline-block;
}
.tick {
    width: auto !important;
    border: none;
    border-left: 2px solid black;
}
</style>
