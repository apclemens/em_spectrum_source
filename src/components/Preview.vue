<template>
    <div class="preview"
         v-on:mousedown="mouseDown"
         v-bind:style="{left: leftPos + 'px'}"
         v-bind:class="{moving: moving != 0}"
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
        }
    },
}
</script>

<style>
.preview {
    height: 25px;
    background-color: rgba(0,0,255,.35);
    width: 10%;
    position: absolute;
    margin-top: -27px;
    border-left: 2px solid black;
    border-right: 2px solid black;
    cursor: grab;
}
.preview.moving {
    cursor: grabbing;
}
</style>
