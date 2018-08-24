<template>
    <div class="markings" v-bind:style="{transform: 'translateY('+(scale==0 ? 0 : -100)+'%)'}">
        <span class="label">Hz</span>
        <div v-if="scale == 0" class="hertz">
            <div v-for="n in 11" class="mark" v-bind:key=n v-bind:style="{left: ((n-1)*10)+'%'}">
                <div>
                3e{{2*n-2}}
                </div>
            </div>
        </div>
        <div v-else class="hertz">
            <div v-for="n in 11" class="mark" v-bind:key=n v-bind:style="{left: (placements[n-1])*100+'%'}">
                <div>
                {{markings[n-1].toExponential(2).replace('e+', 'e')}}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Markings',
    props: ['scale', 'centerPos', 'centerFrequencyRange', 'markings', 'placements'],
    methods: {
        pos_to_freq: function(startFreq, endFreq, pos) {
            return startFreq**(1-pos) * endFreq ** pos;
        }
    },
}


</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Roboto+Mono');
.markings {
    font-family: 'Roboto Mono', monospace;
    position: absolute;
    height: 25px;
    width: 100%;
    transform: translateY(-100%);
}
.label {
    display: inline-block;
    position: absolute;
    right: 0;
    padding: 0 10px;
    background-color: white;
    z-index: 2;
}
.hertz {
    width: 90%;
    margin: auto;
}
.mark {
    display: inline-block;
    position: relative;
    width: 0;
    background-color: black;
    height: 100%;
    border: 1px solid black;
    margin: -1px;
}
.mark div {
    transform: translateX(-50%);
    display: inline-block;
    font-size: 12px;
    background-color: white;
}
</style>
