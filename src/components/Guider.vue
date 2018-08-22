<template>
    <div class="guider">
        <div class="box box1"
             v-bind:style="{width: 'calc('+leftPos+'px - 5%)'}"
            ></div>
        <div class="box box2"
             v-bind:style="{width: 'calc(95% - ' + leftPos + 'px)'}"
            ></div>
    </div>
</template>

<script>

export default {
    name: 'Guider',
    props: ['leftPos'],
}
</script>

<style>
.guider {
    position: absolute;
    height: 100%;
    width: 100%;
}
.box {
    height: 100%;
    position: absolute;
    z-index: -1;
}
.box1 {
    background: linear-gradient(to top left, #fff calc(50% - 1px), #aaa, #d4d4d4 calc(50% + 1px) );
}
.box2 {
    right: 0;
    background: linear-gradient(to top right, #fff calc(50% - 1px), #aaa, #d4d4d4 calc(50% + 1px) );
}
</style>
