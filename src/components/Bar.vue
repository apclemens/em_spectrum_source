<template>
    <div class="bar-container" v-on:mousemove="movePreview">
        <div class="bar"></div>
        <img id="visible-preview" v-if="scale == '0'" src="./../assets/visible.png">
        <Preview v-bind:leftPos="leftPos"/>
        <div class="between">
        <Guider
             v-if="scale != '3'"
             v-bind:leftPos="leftPos"
        />
        <ClassList
             v-if="scale == '0'"
         />
        </div>
        <Markings 
             v-if="scale != '3'"
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
    props: ['scale', 'centerPositions'],
    components: {
        Preview,
        Guider,
        Markings,
        ClassList,
    },
    data() {
        return {
            leftPos: 0,
        }
    },
    methods: {
        movePreview: function(event) {
            this.leftPos = event.x - .045*window.innerWidth;
            this.$emit('updatePositions', this.leftPos);
        }
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
