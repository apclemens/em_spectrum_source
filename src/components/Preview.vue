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
    height: 25px;
    background-color: rgba(0,0,255,.35);
    width: 10%;
    position: absolute;
    margin-top: -27px;
    border-left: 2px solid black;
    border-right: 2px solid black;
}
</style>
