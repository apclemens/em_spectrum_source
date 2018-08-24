<template>
    <div class="information" v-bind:style="{transform: 'translateX('+translate+'%)'}">
        <div class="band" v-for="(band, index) in information" v-bind:class="{tick: band.start == band.end}" v-bind:key="index"
            v-bind:style="{
                 left: frequency_to_position_information(band.start, scale)*90 + '%',
                 width: (frequency_to_position_information(band.end, scale)*90 - frequency_to_position_information(band.start, scale)*90) + '%'
            }"
        >
            <div class="info">
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
        frequency_to_position_information: function(frequency, scale) {
            return Math.log10(frequency/3)/20 * 10**scale;
        },
        move: function(A) {
            this.translate = Math.log10(A/3)/20 * 10**this.scale * (-90);
        }
    },
}

function frequencyToRGB(frequency){
    var Wavelength = 299792458 / frequency;
    var factor;
    var Red,Green,Blue;
    const Gamma = 0.8;
    const IntensityMax = 255;

    if((Wavelength >= 380) && (Wavelength<440)){
        Red = -(Wavelength - 440) / (440 - 380);
        Green = 0.0;
        Blue = 1.0;
    }else if((Wavelength >= 440) && (Wavelength<490)){
        Red = 0.0;
        Green = (Wavelength - 440) / (490 - 440);
        Blue = 1.0;
    }else if((Wavelength >= 490) && (Wavelength<510)){
        Red = 0.0;
        Green = 1.0;
        Blue = -(Wavelength - 510) / (510 - 490);
    }else if((Wavelength >= 510) && (Wavelength<580)){
        Red = (Wavelength - 510) / (580 - 510);
        Green = 1.0;
        Blue = 0.0;
    }else if((Wavelength >= 580) && (Wavelength<645)){
        Red = 1.0;
        Green = -(Wavelength - 645) / (645 - 580);
        Blue = 0.0;
    }else if((Wavelength >= 645) && (Wavelength<781)){
        Red = 1.0;
        Green = 0.0;
        Blue = 0.0;
    }else{
        Red = 0.0;
        Green = 0.0;
        Blue = 0.0;
    }

    if((Wavelength >= 380) && (Wavelength<420)){
        factor = 0.3 + 0.7*(Wavelength - 380) / (420 - 380);
    }else if((Wavelength >= 420) && (Wavelength<701)){
        factor = 1.0;
    }else if((Wavelength >= 701) && (Wavelength<781)){
        factor = 0.3 + 0.7*(780 - Wavelength) / (780 - 700);
    }else{
        factor = 0.0;
    }


    var rgb = [0,0,0];

    // Don't want 0^x = 1 for x <> 0
    rgb[0] = Red==0.0 ? 0 : Math.round(IntensityMax * Math.pow(Red * factor, Gamma));
    rgb[1] = Green==0.0 ? 0 : Math.round(IntensityMax * Math.pow(Green * factor, Gamma));
    rgb[2] = Blue==0.0 ? 0 : Math.round(IntensityMax * Math.pow(Blue * factor, Gamma));

    return rgb;
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
}
.tick {
    width: auto !important;
    border: none;
    border-left: 2px solid black;
}
</style>
