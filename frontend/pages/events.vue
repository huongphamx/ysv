<script lang="ts" setup>
const config = useRuntimeConfig()
const isShowedHeaderLine = useIsShowedHeaderLine()
isShowedHeaderLine.value = false

useHead({
  title: 'Events - YSV'
})
</script>


<template>
  <div class="mycontainer mx-auto mb-10">
    <div class="relative">
      <img src="/img/event-hero.webp" alt="event hero" class="hero-image" />
      <div class="hero-text in-image">EVENTS</div>
    </div>

    <div class="mt-32 mb-12 flex justify-center">
      <div>
        <div class="text-small mb-5 event-text">FOR THE FIRST TIME FASHION FACTOR TOOK PLACE IN DUBAI AND THEREFORE,
          THE LOCATION WAS
          CHOSEN
          TO SHOWCASE THE WONDERS OF THE CAPITAL OF FASHION OF THE MIDDLE EAST.</div>
        <img src="/img/event-1.webp" alt="Event 1" class="rect-image image-1">
      </div>
      <img src="/img/event-2.webp" alt="Event 2" class="rect-image image-2">
    </div>

    <div class="my-12 mx-auto text-medium text-center max-w-[756px]">
      YSV BRAND IS SHINING LIKE A DIAMOND IN NEW EDITION OF FASHION FACTOR WITH TOP DESIGNERS
    </div>

    <div class="xl:hidden grid grid-cols-2 gap-5">
      <div class="flex flex-col gap-5">
        <img src="/img/event-3.webp" alt="Event 3" class="rect-image event-image-small md:ml-auto">
        <img src="/img/event-8.webp" alt="Event 8" class="rect-image">
        <img src="/img/event-4.webp" alt="Event 4" class="rect-image">
      </div>
      <div class="mt-16 md:mt-0 flex flex-col gap-5">
        <img src="/img/event-7.webp" alt="Event 7" class="rect-image">
        <img src="/img/event-10.webp" alt="Event 10" class="rect-image">
        <img src="/img/event-9.webp" alt="Event 9" class="rect-image event-image-small">
      </div>
    </div>
    <div class="hidden xl:grid xl:grid-cols-2 xl:gap-5">
      <div class="flex flex-col gap-5">
        <img src="/img/event-3.webp" alt="" class="image-3">
        <img src="/img/event-4.webp" alt="" class="image-4">
        <div class="grid grid-cols-2 gap-5">
          <img src="/img/event-5.webp" alt="" class="image-5">
          <img src="/img/event-6.webp" alt="" class="image-6">
        </div>
      </div>
      <div class="flex flex-col gap-5">
        <div class="grid grid-cols-2 gap-5">
          <img src="/img/event-7.webp" alt="" class="image-7">
          <img src="/img/event-8.webp" alt="" class="image-8">
        </div>
        <img src="/img/event-9.webp" alt="" class="image-9">
        <img src="/img/event-10.webp" alt="" class="image-10">
      </div>
    </div>

    <div class="my-5"><img src="/img/event-11.webp" alt="Event 11" class="image-11"></div>

    <div class="mb-20 grid grid-cols-2 gap-5">
      <img src="/img/event-12.webp" alt="Event 12" class="rect-image event-image-small ml-auto image-12">
      <video autoplay loop class="rect-image video-13">
        <source :src="`${config.public.s3BaseUrl}/event-13.mp4`" type="video/mp4">
      </video>

    </div>
  </div>
</template>


<style scoped>
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

  @media screen and (min-width: 480px) {
    max-width: 200px;
    margin-right: 12px;
  }

  @media screen and (min-width: 768px) {
    max-width: 293px;
    margin-right: 20px;
  }

  @media screen and (min-width: 1280px) {
    max-width: 324px;
    margin-right: 15px;
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