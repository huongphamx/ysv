<script lang="ts" setup>
import { useWindowSize } from '@vueuse/core'

const { width, height } = useWindowSize()

useHead({
  title: 'About - YSV'
})
</script>


<template>
  <div class="mb-10 mycontainer mx-auto">
    <div class="relative">
      <img src="/img/about-hero.webp" alt="event hero" class="hero-image" />
      <div class="hero-text in-image">ABOUT
      </div>
    </div>
    <div class="hero-text out-image">THE BRAND</div>

    <div class="my-10 grid grid-cols-2 gap-3">
      <div class="xl:w-[300px] mx-auto">
        <div class="text-small mb-5">
          SENSUALITY WITH STYLE. LUXURY FOR THE WOMAN WHO DESERVES IT. FOR YOUR INNER GODDESS. YOUR
          KIND OF LUXURY. SENSUAL. ELEGANT. CLASSY. EXTRAORDINARY. JUST LIKE YOU.
        </div>
        <img src="/img/about-1.webp" alt="about 1" class="rect-image image-1">
      </div>
      <img src="/img/about-2.webp" alt="about 2" class="rect-image image-2">
    </div>

    <div class="text-medium text-center">
      “YOUR LIFE IS A STAGE. YOU DESERVE TO SHINE ON IT. YSV IS NOT YOUR ORDINARY
      DRESS. IT’S EXQUISITE, IT’S SENSUAL, IT’S YOU.”
    </div>
    <div class="mt-2 flex justify-center"><img src="/img/about-sign.svg" alt="about sign" class="w-[200px] md:w-[300px]">
    </div>

    <template v-if="width < 1280">
      <div class="my-5 grid grid-cols-2 gap-3 items-end">
        <img src="/img/about-3.webp" alt="about 3" class="rect-image image-3">
        <img src="/img/about-5.webp" alt="about 5" class="rect-image image-5">
      </div>
      <div class="flex flex-col gap-5 text-small md:max-w-[520px] ml-auto ">
        <div>
          THE FOUNDER OF THE BRAND YULIA SHUKSHINA DREW HER INSPIRATION FROM PROFESSIONAL DANCING BY CREATING A BRAND THAT
          IS EVERYTHING YOU WERE LOOKING FOR AND MORE. SHE WANTED TO BRING THE GLAM AND CHIC THAT YOU SEE ON STAGE TO THE
          WARDROBE OF ANY WOMAN WHO WANTS TO BE NOTICED.
        </div>
        <div>
          YSV IS MADE FOR WOMEN WITH HIGH STANDARDS, WHO APPRECIATE DISTINCTIVE APPEAL OF EVERY DETAIL AND THE TOUCH OF
          THE
          FINEST FABRICS THAT SURROUND YOUR BODY IN PURE LUXURY. THE ONE YOU DON’T WANT TO TAKE OFF.
        </div>
        <div>
          CREATED AT FIRST AS A SMALL COLLECTION OF JUST THREE DRESSES, THE BRAND NOW OFFERS A CHOICE OF STUNNING
          ONE-OF-A-KIND PIECES THAT ARE MADE
          TO PERFECTION FOR YOU TO INDULGE YOURSELF, TO STEAL THE SHOW AND FEEL EXTRAORDINARY, WHENEVER YOU GO.
        </div>
      </div>
      <div class="my-5 flex gap-3 text-small">
        <div class="md:max-w-[207px]">
          <div class="my-3">WITH NO EXCEPTION, WE TAKE GREAT CARE OF THE DETAILS FROM FABRICS TO INDIVIDUAL MEASUREMENTS
            AND
            BEYOND TO
            PRODUCE YOUR PERFECT DRESS, BAR TO NONE.
          </div>
          <div>WE DON’T STOP UNTIL YOU GET THAT WOW-EFFECT. FROM THE EXPERIENCE WHEN YOU OPEN YOUR BOX, TILL THE MOMENT
            YOU
            STEP INSIDE THE ROOM AND AND TAKE EVERYONE'S BREATH AWAY. YOU ARE OUR INSPIRATION.</div>
        </div>
        <div class="about-image-4"><img src="/img/about-4.webp" alt="about 4" class="rect-image image-4"></div>
      </div>
      <div class="flex flex-col gap-2 text-small mt-8">
        <div>YSV BRAND IS INSPIRED BY STRONG AND BEAUTIFUL WOMAN WHO WANT TO FEEL UNAPOLOGETICALLY HERSELF, SHE WANTS TO
          EXPERIENCE LIFE AND FEEL DESIRED. SHE IS SOPHISTICATED AND REFINED.
        </div>
        <div>WITH THAT IN MIND, WE CREATED THE FINEST COLLECTIONS THAT ARE EQUALLY SENSUAL BUT ALSO ELEGANT AND CLASSY.
          IT’S
          AN ABSOLUTE LUXURY, BUT THE ONE YOU CAN AFFORD.</div>
        <div>WE SET THE BAR HIGH, SO YOU NOLONGER HAVE TO COMPROMISE. YOU CAN HAVE THE BEST OF ALL WORLDS.</div>
      </div>
    </template>
    <template v-else>
      <div class="my-16 grid grid-cols-2">
        <div>
          <img src="/img/about-3.webp" alt="">
          <div class="max-w-[480px] mx-auto">
            <div class="text-small my-10">With no exception, we take great care of the details from fabrics to individual
              measurements and beyond to produce your perfect dress, bar to none.
              We don’t stop until you get that WOW-effect. From the experience when you open your box, till the moment you
              step inside the room and and take everyone's breath away. You are our inspiration.</div>
            <img src="/img/about-5.webp" alt="">
          </div>
        </div>
        <div>
          <div class="text-small">
            <p>
              The founder of the brand Yulia Shukshina drew hяer inspiration from professional dancing
              by creating a brand that is everything you were looking for and more. She wanted to bring the glam and chic
              that you see on stage to the wardrobe of any woman who wants to be
              noticed.
            </p>

            <p class="my-10">
              YSV is made for women with high standards, who appreciate distinctive appeal of every detail and the touch
              of
              the finest fabrics that surround your body in pure luxury. The one you don’t want to take off.
            </p>

            <p>
              Created at first as a small collection of just three dresses, the brand now offers a choice of stunning
              one-of-a-kind pieces that are made to perfection for you to indulge yourself, to steal the show and feel
              extraordinary, whenever you go.
            </p>
          </div>
          <img src="/img/about-4.webp" alt="" class="my-10">
          <div class="text-small">
            <p>
              YSV brand is inspired by strong and beautiful woman who want to feel
              unapologetically
              herself, she wants to experience life and feel desired. She is sophisticated and refined.
            </p>

            <p class="my-10">
              With that in mind, we created the finest collections that are equally sensual but also elegant and classy.
              It’s an absolute luxury, but the one you can afford.
            </p>

            <p>We set the bar high, so you nolonger have to compromise. You can have the best of all worlds.</p>
          </div>
        </div>
      </div>
    </template>

    <div class="xl:relative mt-10 mb-16 xl:mb-28">
      <img src="/img/about-6.webp" alt="about 6" class="my-3 about-end">
      <div class="text-medium text-center quoto-2">
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

.about-image-4 {
  display: flex;
  align-items: center;

  @media screen and (min-width: 480px) {
    align-items: start;
    margin-top: 15px;
  }
}

.quoto-2 {
  @media screen and (min-width: 1280px) {
    width: 604px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: white;
  }
}
</style>