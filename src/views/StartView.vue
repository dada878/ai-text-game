<template>
  <div class="start">
    <h1>文字冒險遊戲</h1>
    <div class="btn-group">
      <button class="btn">
        <RouterLink :to="'game'" class="btn-link">
          <h2>開始探索</h2>
        </RouterLink>
      </button>
      <button class="btn">
        <h2>遊戲設定</h2>
      </button>
    </div>
  </div>
</template>
<script lang="ts" setup>
import { RouterLink } from "vue-router";
</script>
<style scoped lang="scss">
.start {
  font-size: 4rem;
  color: aliceblue;
  filter: drop-shadow(5px 5px 5px #00000086);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.btn-group {
  display: flex;
  flex-direction: column;
  width: 90%;
  align-items: center;
  gap: 1rem;

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
    width: 40%;

    .btn-link {
      color: inherit;
      text-decoration: none;
    }

    & * {
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
      width: 45%;
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
}
</style>
