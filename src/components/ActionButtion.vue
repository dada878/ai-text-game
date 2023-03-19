<template>
    <button class="btn" @click="emit('click')">
        <slot></slot>
    </button>
</template>
  
<script lang="ts" setup>
import { defineEmits, defineProps } from 'vue';

const props = defineProps(["hide"]);
const emit = defineEmits(["click"]);

</script>
<style lang="scss" scoped >
.btn {
    border-image-source: url("../assets/button.png");
    border-image-slice: 5 10 5 10 fill;
    border-image-width: 20px 35px 20px 35px;
    border-image-repeat: repeat;
    image-rendering: pixelated;
    padding-left: 3rem;
    padding-right: 1rem;
    padding-top: 3rem;
    padding-bottom: 1rem;
    color: rgba(255, 255, 255, 0.808);
    margin: 0.3rem;
    filter: brightness(1) drop-shadow(5px 5px 5px #00000086);
    background-color: transparent;
    cursor: pointer;
    transition: 200ms;
    opacity: v-bind("hide ? '0' : '1'");

    &>* {
        font-family: Cublic, Avenir, Helvetica, Arial, sans-serif;
        font-weight: normal;
    }

}

</style>