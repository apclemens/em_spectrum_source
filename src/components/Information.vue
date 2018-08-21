<template>
    <div class="information" v-bind:style="{transform: 'translateX('+translate+'%)'}">
        <div class="band" v-for="band in information"
            v-bind:style="{
                 left: frequency_to_position_information(band.start, scale)*90 + '%',
                 width: (frequency_to_position_information(band.end, scale)*90 - frequency_to_position_information(band.start, scale)*90) + '%'
            }"
        >
            {{band.title}}
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
        frequency_to_position_information: function(frequency, scale) {
            return Math.log10(frequency/3)/20 * 10**scale;
        },
        move: function(A, B, freq) {
            this.translate = Math.log10(A/3)/20 * 10**this.scale * (-90);
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
.band {
    position: absolute;
    display: inline-block;
    background-color: rgba(255,0,0,.5);
    top: 0;
    border: 2px solid black;
    box-sizing: border-box;
}
</style>
