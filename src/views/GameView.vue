<template>
  <div class="contianer">
    <div class="board">
      <h2>{{ description }}</h2><br>
    </div>
    <div class="btn-group">
      <button
        :class="{ btn: true, disappear: disappear && index != choiceBtnIndex, 'disappear-slow': index == choiceBtnIndex }"
        v-for="item, index in options" @click="choice(index + 1)" :key="index">
        <h2>{{ item }}</h2>
      </button><br>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, Ref } from 'vue';
const ws = new WebSocket('ws://127.0.0.1:13254')

ws.onopen = () => {
  console.log('open connection')
}

let description: Ref<string> = ref("")
let options: Ref<Array<string>> = ref([]);
let disappear: Ref<boolean> = ref(false);
let choiceBtnIndex: Ref<number> = ref(-1);

ws.onclose = () => {
  console.log("disconnected");
}

ws.onmessage = event => {
  const data = JSON.parse(event.data);
  description.value = data.description;
  options.value = data.options;
  console.log(data);
}

const choice = function (index: number) {
  ws.send(index.toString());
  disappear.value = true;
  choiceBtnIndex.value = index - 1;
  setTimeout(() => {
    options.value = [];
    disappear.value = false;
    choiceBtnIndex.value = -1;
  }, 1500);
}
</script>
<style lang="scss" scoped >
.contianer {
  width: 60%;
  margin: 0rem auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 3rem;

  .board {
    border-image-source: url("../assets/board.png");
    border-image-slice: 15 15 15 15 fill;
    border-image-width: 80px 80px 80px 80px;
    border-image-repeat: repeat;
    image-rendering: pixelated;
    padding-left: 4rem;
    padding-right: 4rem;
    padding-top: 2.5rem;
    padding-bottom: 2.5rem;
    color: white;
    margin-bottom: 2rem;
    filter: drop-shadow(5px 5px 5px #00000086);

    h2 {
      font-weight: normal;
    }

  }

  .btn-group {
    display: flex;
    flex-direction: column;
    width: 90%;
    align-items: center;

    .btn {
      border-image-source: url("../assets/button.png");
      border-image-slice: 5 10 5 10 fill;
      border-image-width: 20px 35px 20px 35px;
      border-image-repeat: repeat;
      image-rendering: pixelated;
      padding-left: 1rem;
      padding-right: 1rem;
      padding-top: 0.5rem;
      padding-bottom: 0.5rem;
      color: rgba(255, 255, 255, 0.808);
      margin: 0.3rem;
      filter: brightness(1) drop-shadow(5px 5px 5px #00000086);
      background-color: transparent;
      cursor: pointer;
      transition: 200ms;
      opacity: 0;
      width: 95%;

      &>* {
        font-family: Cublic, Avenir, Helvetica, Arial, sans-serif;
        font-weight: normal;
      }

      &:nth-child(1) {
        animation: appear 400ms 000ms forwards;
      }

      &:nth-child(2) {
        animation: appear 400ms 300ms forwards;
      }

      &:nth-child(3) {
        animation: appear 400ms 600ms forwards;
      }

      &:nth-child(4) {
        animation: appear 400ms 900ms forwards;
      }

      &:hover {
        filter: brightness(1.15) drop-shadow(5px 5px 5px #00000086);
        color: rgb(255, 255, 255);
        width: 100%;

      }

      &:active {
        filter: brightness(1.5) drop-shadow(5px 5px 5px #00000086);
      }

      &:is(.disappear) {
        animation: disappear 600ms forwards;
        pointer-events: none;
      }

      &:is(.disappear-slow) {
        animation: disappear-slow 1500ms forwards;
        pointer-events: none;
      }
    }
  }
}

@keyframes appear {
  0% {
    opacity: 0;
    height: 0%;
    transform: translateY(3rem);
  }

  100% {
    opacity: 1;
    height: 100%;
    transform: translateY(0rem);
  }
}

@keyframes disappear {
  0% {
    opacity: 1;
    height: 100%;
  }

  100% {
    opacity: 0;
    height: 0%;
  }
}

@keyframes disappear-slow {
  0% {
    opacity: 1;
    transform: scale(1);
  }

  40% {
    opacity: 1;
    transform: scale(1.1);
  }

  60% {
    opacity: 1;
    transform: scale(1.1);
  }

  100% {
    opacity: 0;
    transform: scale(0.9);
  }
}</style>