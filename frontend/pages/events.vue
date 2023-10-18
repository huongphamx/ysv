<script lang="ts" setup>
const config = useRuntimeConfig()
const cloudfrontDistributionDomain = config.public.cloudfrontDistributionDomain

const isShowedHeaderLine = useIsShowedHeaderLine()
isShowedHeaderLine.value = false

useHead({
  title: 'Events - YSV'
})
</script>


<template>
  <div class="events-body mycontainer mx-auto">
    <div class="relative">
      <img :src="`${cloudfrontDistributionDomain}/img/event-hero.webp`" alt="event hero" class="hero-image"
        v-motion="slideVisibleOnceMotion" />
      <div class="hero-text in-image" v-motion="slideVisibleOnceBottomMotion">EVENTS</div>
    </div>

    <div class="mt-32 mb-12 flex justify-center">
      <div v-motion="slideVisibleOnceLeftMotion">
        <div class="text-small event-text">FOR THE FIRST TIME FASHION FACTOR TOOK PLACE IN DUBAI AND THEREFORE,
          THE LOCATION WAS
          CHOSEN
          TO SHOWCASE THE WONDERS OF THE CAPITAL OF FASHION OF THE MIDDLE EAST.</div>
        <img :src="`${cloudfrontDistributionDomain}/img/event-1.webp`" alt="Event 1" class="rect-image image-1">
      </div>
      <img :src="`${cloudfrontDistributionDomain}/img/event-2.webp`" alt="Event 2" class="rect-image image-2"
        v-motion="slideVisibleOnceRightMotion">
    </div>

    <div class="my-12 mx-auto text-medium text-center max-w-[756px]" v-motion="slideVisibleOnceBottomMotion">
      YSV BRAND IS SHINING LIKE A DIAMOND IN NEW EDITION OF FASHION FACTOR WITH TOP DESIGNERS
    </div>

    <div class="xl:hidden grid grid-cols-2 gap-5">
      <div class="flex flex-col gap-5">
        <img :src="`${cloudfrontDistributionDomain}/img/event-3.webp`" alt="Event 3"
          class="rect-image event-image-small md:ml-auto" v-motion="slideVisibleOnceBottomMotion">
        <img :src="`${cloudfrontDistributionDomain}/img/event-8.webp`" alt="Event 8" class="rect-image"
          v-motion="slideVisibleOnceBottomMotion">
        <img :src="`${cloudfrontDistributionDomain}/img/event-4.webp`" alt="Event 4" class="rect-image"
          v-motion="slideVisibleOnceBottomMotion">
      </div>
      <div class="mt-16 md:mt-0 flex flex-col gap-5">
        <img :src="`${cloudfrontDistributionDomain}/img/event-7.webp`" alt="Event 7" class="rect-image"
          v-motion="slideVisibleOnceBottomMotion">
        <img :src="`${cloudfrontDistributionDomain}/img/event-10.webp`" alt="Event 10" class="rect-image"
          v-motion="slideVisibleOnceBottomMotion">
        <img :src="`${cloudfrontDistributionDomain}/img/event-9.webp`" alt="Event 9" class="rect-image event-image-small"
          v-motion="slideVisibleOnceBottomMotion">
      </div>
    </div>
    <div class="hidden xl:grid xl:grid-cols-2 xl:gap-5">
      <div class="flex flex-col gap-5">
        <img :src="`${cloudfrontDistributionDomain}/img/event-3.webp`" alt="" class="image-3"
          v-motion="slideVisibleOnceBottomMotion">
        <img :src="`${cloudfrontDistributionDomain}/img/event-4.webp`" alt="" class="image-4"
          v-motion="slideVisibleOnceBottomMotion">
        <div class="grid grid-cols-2 gap-5">
          <img :src="`${cloudfrontDistributionDomain}/img/event-5.webp`" alt="" class="image-5"
            v-motion="slideVisibleOnceBottomMotion">
          <img :src="`${cloudfrontDistributionDomain}/img/event-6.webp`" alt="" class="image-6"
            v-motion="slideVisibleOnceBottomMotion">
        </div>
      </div>
      <div class="flex flex-col gap-5">
        <div class="grid grid-cols-2 gap-5">
          <img :src="`${cloudfrontDistributionDomain}/img/event-7.webp`" alt="" class="image-7"
            v-motion="slideVisibleOnceBottomMotion">
          <img :src="`${cloudfrontDistributionDomain}/img/event-8.webp`" alt="" class="image-8"
            v-motion="slideVisibleOnceBottomMotion">
        </div>
        <img :src="`${cloudfrontDistributionDomain}/img/event-9.webp`" alt="" class="image-9"
          v-motion="slideVisibleOnceBottomMotion">
        <img :src="`${cloudfrontDistributionDomain}/img/event-10.webp`" alt="" class="image-10"
          v-motion="slideVisibleOnceBottomMotion">
      </div>
    </div>

    <div class="my-5"><img :src="`${cloudfrontDistributionDomain}/img/event-11.webp`" alt="Event 11" class="image-11"
        v-motion="slideVisibleOnceBottomMotion"></div>

    <div class="grid grid-cols-2 gap-5">
      <img :src="`${cloudfrontDistributionDomain}/img/event-12.webp`" alt="Event 12"
        class="rect-image event-image-small ml-auto image-12" v-motion="slideVisibleOnceBottomMotion">
      <video autoplay preload="auto" playsinline muted loop class="rect-image video-13"
        v-motion="slideVisibleOnceBottomMotion">
        <source :src="`${cloudfrontDistributionDomain}/event-13.mp4`" type="video/mp4">
      </video>
    </div>
  </div>
</template>


<style scoped>
.events-body {
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

@media screen and (min-width: 1280px) {
  .image-1 {
    width: 304px;
    height: 433px;
  }

  .image-2 {
    width: 412px;
    height: 619px;
  }

  .image-3 {
    width: 628px;
    height: 846px;
  }

  .image-4 {
    width: 628px;
    height: 962px;
  }

  .image-5,
  .image-6 {
    width: 304px;
    height: 536px;
  }

  .image-7,
  .image-8 {
    width: 304px;
    height: 457px;
  }

  .image-9,
  .image-10,
  .image-12,
  .video-13 {
    width: 628px;
    height: 943px;
  }
}

.event-text {
  max-width: 155px;
  margin-right: 5px;
  margin-bottom: 15px;

  @media screen and (min-width: 480px) {
    max-width: 200px;
    margin-right: 12px;
    margin-bottom: 20px;
  }

  @media screen and (min-width: 768px) {
    max-width: 293px;
    margin-right: 20px;
  }

  @media screen and (min-width: 1280px) {
    max-width: 324px;
    margin-right: 15px;
    margin-bottom: 30px;
  }
}

.image-11 {
  width: 300px;
  height: 220px;

  @media screen and (min-width: 480px) {
    width: 420px;
    height: 300px;
  }

  @media screen and (min-width: 768px) {
    width: 620px;
    height: 430px;
  }

  @media screen and (min-width: 1280px) {
    width: 1276px;
    height: 892px;
  }
}
</style>