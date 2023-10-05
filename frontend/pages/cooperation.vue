<script lang="ts" setup>
definePageMeta({
  layout: 'default-line-header',
})

useHead({
  title: 'Cooperation - YSV'
})
</script>


<template>
  <div class="mt-5 mb-24 mycontainer mx-auto">
    <div class="my-6 hidden xl:block">
      <div class="flex items-center gap-2 hover:cursor-pointer" @click="$router.back()">
        <UIcon name="i-ph-arrow-up-left" class="text-xl" /><span>GO BACK</span>
      </div>
    </div>
    <div class="relative">
      <img src="/img/cooperation-hero.webp" alt="" class="cooperation-hero">
      <div class="absolute w-full top-1/2 right-1/2 translate-x-1/2 -translate-y-1/2 text-center text-white">
        <div class="cooperation-text-1 font-['Italiana']">LET'S WORK TOGETHER</div>
        <div class="mt-2 cooperation-email">FOR COOPERATION DROP A MESSAGE ON</div>
        <div class="cooperation-email">ysv.shukshina@gmail.com</div>
      </div>
    </div>
  </div>
</template>


<style scoped>
.cooperation-hero {
  width: 300px;
  height: 400px;
  object-fit: cover;
}

.cooperation-text-1 {
  font-size: 20px;
}

.cooperation-email {
  font-size: 14px;
}

@media screen and (min-width: 640px) {
  .cooperation-hero {
    width: 420px;
    height: 500px;
    object-fit: cover;
  }

  .cooperation-text-1 {
    font-size: 26px;
  }

  .cooperation-email {
    font-size: 16px;
  }
}

@media screen and (min-width: 768px) {
  .cooperation-hero {
    width: 620px;
    height: 433px;
    object-fit: cover;
  }

  .cooperation-text-1 {
    font-size: 32px;
  }

  .cooperation-email {
    font-size: 18px;
  }
}

@media screen and (min-width: 1280px) {
  .cooperation-hero {
    width: 1276px;
    height: 892px;
    object-fit: cover;
  }

  .cooperation-text-1 {
    font-size: 36px;
  }

  .cooperation-email {
    font-size: 20px;
  }
}
</style>

