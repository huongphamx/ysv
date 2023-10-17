<script lang="ts" setup>
const isShowedHeaderLine = useIsShowedHeaderLine()
isShowedHeaderLine.value = false

const config = useRuntimeConfig()
const cloudfrontDistributionDomain = config.public.cloudfrontDistributionDomain

useHead({
  title: 'About - YSV'
})
</script>


<template>
  <div class="mb-10 mycontainer mx-auto">
    <div class="relative">
      <img :src="`${cloudfrontDistributionDomain}/img/about-hero.webp`" alt="event hero" class="hero-image"
        v-motion="slideVisibleOnceMotion" />
      <div class="hero-text in-image" v-motion="slideVisibleOnceBottomMotion">
        ABOUT
      </div>
    </div>
    <div class="hero-text out-image" v-motion="slideVisibleOnceBottomMotion">
      THE BRAND</div>

    <div class="block-1 flex">
      <div class="mr-3 block-1_left" v-motion="slideVisibleOnceLeftMotion">
        <div class="block-1_left_text text-small">
          SENSUALITY WITH STYLE. LUXURY FOR THE WOMAN WHO DESERVES IT. FOR YOUR INNER GODDESS. YOUR
          KIND OF LUXURY. SENSUAL. ELEGANT. CLASSY. EXTRAORDINARY. JUST LIKE YOU.
        </div>
        <img :src="`${cloudfrontDistributionDomain}/img/about-1.webp`" alt="about 1" class="rect-image image-1">
      </div>
      <img :src="`${cloudfrontDistributionDomain}/img/about-2.webp`" alt="about 2" class="rect-image image-2"
        v-motion="slideVisibleOnceRightMotion">
    </div>

    <div class="block-2">
      <div class="text-medium text-center quoto" v-motion="slideVisibleOnceBottomMotion">
        “YOUR LIFE IS A STAGE. YOU DESERVE TO SHINE ON IT. YSV IS NOT YOUR ORDINARY
        DRESS. IT’S EXQUISITE, IT’S SENSUAL, IT’S YOU.”
      </div>
      <img :src="`${cloudfrontDistributionDomain}/img/about-sign.svg`" alt="about sign" class="sign"
        v-motion="slideVisibleOnceBottomMotion">
    </div>

    <AboutBodyMobile />
    <AboutBodyDesktop />

    <div class="xl:relative mb-16 xl:mb-28 quoto-2" v-motion="slideVisibleOnceBottomMotion">
      <img :src="`${cloudfrontDistributionDomain}/img/about-6.webp`" alt="about 6" class="about-end">
      <div class="text-medium text-center quoto-2_text">
        INDULGE IN LUXURY LIKE NEVER BEFORE WITH YSV BRAND.
        IT’S YOUR TIME TO SHINE, DARLING.
      </div>
    </div>
  </div>
</template>


<style scoped>
.rect-image {
  width: 140px;
  height: 210px;
  object-fit: cover;

  &.image-1 {
    margin-top: 15px;

    @media screen and (min-width: 480px) {
      margin-top: 20px;
    }

    @media screen and (min-width: 1280px) {
      margin-top: 30px;
    }
  }

  @media screen and (min-width: 480px) {
    width: 200px;
    height: 300px;
  }

  @media screen and (min-width: 768px) {
    width: 300px;
    height: 450px;

    &.image-1 {
      height: 380px;
    }

    &.image-2 {
      height: 500px;
    }

    &.image-3 {
      width: 300px;
      height: 390px;
    }

    &.image-4 {
      width: 380px;
      height: 480px;
    }

    &.image-5 {
      width: 220px;
      height: 270px;
    }
  }

  @media screen and (min-width: 1280px) {
    &.image-1 {
      width: 304px;
      height: 380px;
    }

    &.image-2 {
      width: 520px;
      height: 650px;
    }

    &.image-3 {
      width: 628px;
      height: 785px;
    }

    &.image-4 {
      width: 628px;
      height: 685px;
    }

    &.image-5 {
      width: 412px;
      height: 515px;
    }
  }
}

.hero-text {
  font-family: Italiana;
  font-size: 40px;
  font-weight: 400;
  line-height: 28px;

  @media screen and (min-width: 480px) {
    font-size: 60px;
    line-height: 42px;
  }

  @media screen and (min-width: 768px) {
    font-size: 100px;
    line-height: 68px;
  }

  @media screen and (min-width: 1280px) {
    font-size: 200px;
    line-height: 135px;
  }

  &.in-image {
    color: white;
    position: absolute;
    bottom: 0;
  }

  &.out-image {
    margin-top: 10px;
    margin-left: 80px;

    @media screen and (min-width: 480px) {
      margin-left: 110px;
    }

    @media screen and (min-width: 768px) {
      margin-top: 16px;
    }

    @media screen and (min-width: 768px) {
      margin-left: 80px;
    }

    @media screen and (min-width: 1276px) {
      margin-top: 35px;
      margin-left: 108px;
    }
  }
}

.block-1 {
  margin-top: 50px;

  @media screen and (min-width: 480px) {
    margin-top: 80px;
  }

  @media screen and (min-width: 768px) {
    margin-top: 100px;
  }

  @media screen and (min-width: 1276px) {
    margin-top: 200px;
    margin-left: 216px;


    &_left {
      margin-right: 108px;

      &_text {
        width: 324px;
        margin-bottom: 30px;
      }
    }
  }
}

.block-2 {
  margin-top: 30px;
  margin-bottom: 30px;

  @media screen and (min-width: 480px) {
    margin-top: 50px;
    margin-bottom: 50px;
  }

  @media screen and (min-width: 1280px) {
    margin-top: 80px;
    margin-bottom: 80px;
  }

  .quoto {
    margin: 0 auto;
    width: 255px;

    @media screen and (min-width: 480px) {
      width: 329px;
    }

    @media screen and (min-width: 768px) {
      width: 447px;
    }

    @media screen and (min-width: 1280px) {
      width: 756px;
    }
  }

  .sign {
    margin: 0 auto;
    width: 140px;
    margin-top: 20px;

    @media screen and (min-width: 480px) {
      margin-top: 30px;
      width: 178px;
    }

    @media screen and (min-width: 768px) {
      width: 220px;
    }
  }
}

.block-3-mobile {
  margin-top: 15px;
  margin-bottom: 15px;
  max-width: 300px;

  @media screen and (min-width: 480px) {
    margin-top: 20px;
    margin-bottom: 20px;
    max-width: 411px;
  }

  @media screen and (min-width: 768px) {
    margin-bottom: 50px;
    max-width: 520px;
    margin-left: auto;
  }
}

.block-4-mobile {
  display: flex;

  &_text {
    max-width: 155px;
    margin-right: 5px;

    @media screen and (min-width: 480px) {
      max-width: 200px;
      margin-right: 20px;
    }
  }

  &_image {
    display: flex;
    align-items: center;

    @media screen and (min-width: 480px) {
      align-items: start;
      margin-top: 15px;
    }
  }
}

.block-5-mobile {
  margin-top: 15px;
  margin-bottom: 15px;

  @media screen and (min-width: 480px) {
    margin-top: 20px;
    margin-bottom: 20px;
  }

  @media screen and (min-width: 768px) {
    margin-top: 50px;
    margin-bottom: 50px;
  }
}

.quoto-2 {
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

  &_text {
    width: 255px;
    margin: 15px auto 0;

    @media screen and (min-width: 480px) {
      width: 420px;
      margin: 20px auto 0;
    }

    @media screen and (min-width: 768px) {
      width: 604px;
      margin: 30px auto 0;
    }

    @media screen and (min-width: 1280px) {
      width: 604px;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      color: white;
    }
  }
}
</style>