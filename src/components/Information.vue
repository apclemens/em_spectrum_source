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
            v-on:click="clickBand(band)"
            v-bind:style="{
                 left: frequency_to_position_information(band.start, scale)*100 + '%',
                 width: (frequency_to_position_information(band.end, scale)*100 - frequency_to_position_information(band.start, scale)*100) + '%',
                 top: 'calc(' + 4.5*5/6*band.row + 'vh - ' + 6.25*5/6*band.row + 'px)'
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
        clickBand: function(band) {
            /*
            var url = 'https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&origin=*&rvsection=0&titles=' + band.wiki + '&format=json';
            var http = new XMLHttpRequest();
            http.open('GET', url);
            http.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
            var ths = this;
            http.onload = function() {
                if (http.status === 200) {
                    var json = JSON.parse(http.responseText);
                    var data = json.query.pages[Object.keys(json.query.pages)[0]].revisions[0]['*'];
                    ths.$emit('showOverlay', data);
                } else console.log(http);
            }
            http.send();
            */
            this.$emit('showOverlay', "//en.wikipedia.org/w/index.php?title=" + band.wiki + "&printable=yes");
        },
        getLeftPos: function(startFreq) {
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
    height: calc(3.75vh - 5.21px);
    cursor: pointer;
}
.band:hover {
    overflow: visible;
    z-index: 2;
}
.band:hover .info {
    margin: auto;
    position: relative;
    min-width: 0 !important;
    background-color: red;
    z-index: 1;
}
.info {
    pointer-events: none;
    position: relative;
    display: inline-block;
    font-family: 'Merriweather', serif;
}
.tick {
    width: auto !important;
    border: none;
    border-left: 2px solid black;
}
</style>
