<template>
    <div class="markings">
        <span class="label">Hz</span>
        <div v-if="scale == 0" class="hertz">
            <div v-for="n in 11" class="mark" v-bind:key=n>
                3e{{2*n-2}}
            </div>
        </div>
        <div v-else class="hertz">
            <div v-for="n in 11" class="mark" v-bind:key=n>
                {{n}}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Markings',
    props: ['scale', 'markingList'],
    methods: {
    },
}
</script>

<style>
.markings {
    position: absolute;
    transform: translateY(-100%);
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
    display: flex;
    justify-content: space-between;
}
.mark {
    display: inline-block;
}
</style>
