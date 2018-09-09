<template>
    <div class="preview"
         v-on:mousedown="mouseDown"
         v-bind:style="{left: leftPos + 'px'}"
         v-bind:class="{moving: moving != 0, onLeft: leftPosFrac() < -.045, onRight: leftPosFrac() > .95}"
        >
    </div>
</template>

<script>
export default {
    name: 'Preview',
    props: ['leftPos', 'moving'],
    methods: {
        mouseDown: function(event) {
            this.$emit("mouseDown", event);
        },
        leftPosFrac: function() {
            return this.leftPos / window.innerWidth;
        },
    },
}
</script>

<style>
.preview {
    height: 25px;
    background-color: rgba(0,0,255,.35);
    width: 9%;
    position: absolute;
    margin-top: -27px;
    border-left: 2px solid black;
    border-right: 2px solid black;
    cursor: grab;
    transform: translateX(calc(.5vw - 2px));
}
.preview.moving {
    cursor: grabbing;
}
.preview.onLeft {
    left: 0 !important;
    transform: none;
    border: none;
    background-image: linear-gradient(to right, rgba(0,0,255,.35), rgba(0,0,0,0));
    background-color: unset;
}
.preview.onRight {
    right: 0 !important;
    transform: none;
    border: none;
    left: unset !important;
    background-image: linear-gradient(to left, rgba(0,0,255,.35), rgba(0,0,0,0));
    background-color: unset;
}
</style>
