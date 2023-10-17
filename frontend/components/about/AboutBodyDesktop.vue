<script lang="ts" setup>
const config = useRuntimeConfig()
const cloudfrontDistributionDomain = config.public.cloudfrontDistributionDomain
</script>


<template>
  <div class="hidden xl:block">
    <div class="mb-20 grid grid-cols-2 gap-5">
      <div>
        <img :src="`${cloudfrontDistributionDomain}/img/about-3.webp`" alt="" class="w-[628px] h-[785px] object-cover"
          v-motion="slideVisibleOnceLeftMotion">
        <div class="max-w-[479px] ml-[108px]" v-motion="slideVisibleOnceLeftMotion">
          <div class="text-small my-[60px]">
            <p>
              With no exception, we take great care of the details from fabrics to individual
              measurements and beyond to produce your perfect dress, bar to none.
            </p><br>
            <p>
              We don’t stop until you get that WOW-effect. From the experience when you open your box, till the moment
              you
              step inside the room and and take everyone's breath away. You are our inspiration.
            </p>
          </div>
          <img :src="`${cloudfrontDistributionDomain}/img/about-5.webp`" alt="" class="w-[412px] h-[515px] object-cover">
        </div>
      </div>
      <div>
        <div class="text-small w-[520px]" v-motion="slideVisibleOnceRightMotion">
          <p>
            The founder of the brand Yulia Shukshina drew hяer inspiration from professional dancing
            by creating a brand that is everything you were looking for and more. She wanted to bring the glam and chic
            that you see on stage to the wardrobe of any woman who wants to be
            noticed.
          </p><br>

          <p>
            YSV is made for women with high standards, who appreciate distinctive appeal of every detail and the touch
            of
            the finest fabrics that surround your body in pure luxury. The one you don’t want to take off.
          </p><br>

          <p>
            Created at first as a small collection of just three dresses, the brand now offers a choice of stunning
            one-of-a-kind pieces that are made to perfection for you to indulge yourself, to steal the show and feel
            extraordinary, whenever you go.
          </p>
        </div>
        <img :src="`${cloudfrontDistributionDomain}/img/about-4.webp`" alt=""
          class="w-[628px] h-[785px] object-cover my-[60px]" v-motion="slideVisibleOnceRightMotion">
        <div class="text-small w-[520px]" v-motion="slideVisibleOnceRightMotion">
          <p>
            YSV brand is inspired by strong and beautiful woman who want to feel
            unapologetically
            herself, she wants to experience life and feel desired. She is sophisticated and refined.
          </p><br>

          <p>
            With that in mind, we created the finest collections that are equally sensual but also elegant and classy.
            It’s an absolute luxury, but the one you can afford.
          </p><br>

          <p>We set the bar high, so you nolonger have to compromise. You can have the best of all worlds.</p>
        </div>
      </div>
    </div>
  </div>
</template>
