<template>
    <div class="markings">
        <span class="label">Hz</span>
        <div v-if="scale == 0" class="hertz">
            <div v-for="n in 11" class="mark" v-bind:key=n v-bind:style="{left: ((n-1)*10)+'%'}">
                &nbsp;3e{{2*n-2}}
            </div>
        </div>
        <div v-else class="hertz">
            <div v-for="(n, index) in markings" class="mark" v-bind:key=index v-bind:style="{left: (placements[index]*100)+'%'}">
                &nbsp;{{n.toExponential(2)}}
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
.markings {
    position: absolute;
    height: 25px;
    width: 100%;
}
.label {
    display: inline-block;
    position: absolute;
    right: 10px;
}
.hertz {
    width: 90%;
    margin: auto;
    overflow: hidden;
}
.mark {
    display: inline-block;
    position: relative;
    width: 0;
    background-color: black;
    height: 100%;
}
</style>
