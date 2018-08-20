<template>
    <div class="preview"
         v-bind:style="{left: leftPos + 'px'}"
        >
    </div>
</template>

<script>
export default {
    name: 'Preview',
    props: ['leftPos'],
}
</script>

<style>
.preview {
    height: 20px;
    background-color: red;
    width: 10%;
    position: absolute;
    margin-top: -10px;
    pointer-events: none;
}
</style>
