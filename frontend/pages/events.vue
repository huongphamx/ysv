<script lang="ts" setup>

</script>


<template>
  <div class="mycontainer mx-auto mb-10">
    <div class="relative">
      <img src="/img/event-hero.webp" alt="event hero" class="img-hero object-cover" />
      <div class="absolute bottom-0 text-white font-['Italiana'] text-hero">EVENTS</div>
    </div>

    <div class="my-12 grid grid-cols-2 gap-1">
      <div>
        <div class="event-text-1">FOR THE FIRST TIME FASHION FACTOR TOOK PLACE IN DUBAI AND THEREFORE, THE LOCATION WAS
          CHOSEN
          TO SHOWCASE THE WONDERS OF THE CAPITAL OF FASHION OF THE MIDDLE EAST.</div>
        <img src="/img/event-1.webp" alt="Event 1" class="img-mobile">
      </div>
      <div><img src="/img/event-2.webp" alt="Event 2" class="img-mobile"></div>
    </div>

    <div class="my-12 event-text-2 font-['Italiana'] text-center">
      YSV BRAND IS SHINING LIKE A DIAMOND IN NEW EDITION OF FASHION FACTOR WITH TOP DESIGNERS
    </div>

    <div class="xl:hidden grid grid-cols-2 gap-3">
      <div class="flex flex-col gap-3">
        <img src="/img/event-3.webp" alt="Event 3" class="img-mobile">
        <img src="/img/event-8.webp" alt="Event 8" class="img-mobile">
        <img src="/img/event-4.webp" alt="Event 4" class="img-mobile">
      </div>
      <div class="mt-16 flex flex-col gap-3">
        <img src="/img/event-7.webp" alt="Event 7" class="img-mobile">
        <img src="/img/event-10.webp" alt="Event 10" class="img-mobile">
        <img src="/img/event-9.webp" alt="Event 9" class="img-mobile">
      </div>
    </div>
    <div class="hidden xl:grid xl:grid-cols-2 xl:gap-3">
      <div class="flex flex-col gap-3">
        <img src="/img/event-3.webp" alt="" class="img-desktop">
        <img src="/img/event-4.webp" alt="" class="img-desktop">
        <div class="grid grid-cols-2 gap-3">
          <img src="/img/event-5.webp" alt="" class="img-desktop-small">
          <img src="/img/event-6.webp" alt="" class="img-desktop-small">
        </div>
      </div>
      <div class="flex flex-col gap-3">
        <div class="grid grid-cols-2 gap-3">
          <img src="/img/event-7.webp" alt="" class="img-desktop-small">
          <img src="/img/event-8.webp" alt="" class="img-desktop-small">
        </div>
        <img src="/img/event-9.webp" alt="" class="img-desktop">
        <img src="/img/event-10.webp" alt="" class="img-desktop">
      </div>
    </div>

    <div class="my-3"><img src="/img/event-11.webp" alt="Event 11"></div>

    <div class="grid grid-cols-2 gap-3">
      <img src="/img/event-12.webp" alt="Event 12" class="img-mobile">
      <video autoplay loop class="img-mobile">
        <source src="https://ysv-dev-static-img.s3.ap-northeast-1.amazonaws.com/event-13.mp4" type="video/mp4">
      </video>

    </div>
  </div>
</template>


<style scoped>
.img-hero {
  width: 300px;
  height: 400px;
}

.img-mobile {
  width: 140px;
  height: 210px;
  object-fit: cover;
}

.text-hero {
  font-size: 60px;
  line-height: 100%;
}

.event-text-1 {
  font-size: 14px;
}

.event-text-2 {
  font-size: 20px;
}

.img-desktop {
  width: 628px;
  height: 943px;
  object-fit: cover;
}

.img-desktop-small {
  width: 304px;
  height: 457px;
  object-fit: cover;
}

@media screen and (min-width: 480px) {
  .img-hero {
    width: 420px;
    height: 500px;
  }

  .img-mobile {
    width: 200px;
    height: 300px;
    object-fit: cover;
  }

  .text-hero {
    font-size: 100px;
  }

  .event-text-1 {
    font-size: 16px;
  }

  .event-text-2 {
    font-size: 26px;
  }
}

@media screen and (min-width: 768px) {
  .img-hero {
    width: 620px;
    height: 540px;
  }

  .img-mobile {
    width: 300px;
    height: 450px;
    object-fit: cover;
  }

  .text-hero {
    font-size: 100px;
  }

  .event-text-1 {
    font-size: 18px;
  }

  .event-text-2 {
    font-size: 32px;
  }
}

@media screen and (min-width: 1280px) {
  .img-hero {
    width: 1276px;
    height: 836px;
  }

  .img-mobile {
    width: 628px;
    height: 943px;
    object-fit: cover;
  }

  .text-hero {
    font-size: 200px;
  }

  .event-text-1 {
    font-size: 20px;
  }

  .event-text-2 {
    font-size: 36px;
  }
}
</style>