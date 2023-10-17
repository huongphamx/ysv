<script lang="ts" setup>
const isShowedHeaderLine = useIsShowedHeaderLine()
isShowedHeaderLine.value = true

const config = useRuntimeConfig()
const cloudfrontDistributionDomain = config.public.cloudfrontDistributionDomain

useHead({
  title: 'Cooperation - YSV'
})
</script>


<template>
  <div class="cooperation-body mycontainer mx-auto">
    <GoBackArrow />
    <div class="relative">
      <img :src="`${cloudfrontDistributionDomain}/img/cooperation-hero.webp`" alt="" class="hero-image cooperation-hero"
        v-motion="slideVisibleOnceMotion">
      <div class="absolute w-full top-1/2 right-1/2 translate-x-1/2 -translate-y-1/2 text-center text-white">
        <div class="text-medium">LET'S WORK TOGETHER</div>
        <div class="text-2 text-small">FOR COOPERATION DROP A MESSAGE ON</div>
        <div class="text-small email">ysv.shukshina@gmail.com</div>
        <div class="text-small email">+971 54 560 2477</div>
      </div>
    </div>
  </div>
</template>


<style scoped>
.cooperation-body {
  margin-bottom: 50px;

  @media screen and (min-width: 480px) {
    margin-bottom: 80px;
  }

  @media screen and (min-width: 768px) {
    margin-bottom: 100px;
  }

  @media screen and (min-width: 1280px) {
    margin-bottom: 150px;
  }
}

.text-2 {
  margin-top: 15px;

  @media screen and (min-width: 480px) {
    margin-top: 20px;
  }

  @media screen and (min-width: 1280px) {
    margin-top: 30px;
  }
}

.email {
  text-transform: lowercase !important;
}
</style>