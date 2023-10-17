<script lang="ts" setup>
const config = useRuntimeConfig()
const cloudfrontDistributionDomain = config.public.cloudfrontDistributionDomain
</script>


<template>
  <div class="xl:hidden">
    <div class="grid grid-cols-2 gap-2.5 items-end">
      <img :src="`${cloudfrontDistributionDomain}/img/about-3.webp`" alt="about 3" class="rect-image image-3"
        v-motion="slideVisibleOnceLeftMotion">
      <img :src="`${cloudfrontDistributionDomain}/img/about-5.webp`" alt="about 5" class="rect-image image-5"
        v-motion="slideVisibleOnceRightMotion">
    </div>
    <div class="block-3-mobile text-small">
      <p v-motion="slideVisibleOnceBottomMotion">
        THE FOUNDER OF THE BRAND YULIA SHUKSHINA DREW HER INSPIRATION FROM PROFESSIONAL DANCING BY CREATING A BRAND THAT
        IS EVERYTHING YOU WERE LOOKING FOR AND MORE. SHE WANTED TO BRING THE GLAM AND CHIC THAT YOU SEE ON STAGE TO THE
        WARDROBE OF ANY WOMAN WHO WANTS TO BE NOTICED.
      </p><br>
      <p v-motion="slideVisibleOnceBottomMotion">
        YSV IS MADE FOR WOMEN WITH HIGH STANDARDS, WHO APPRECIATE DISTINCTIVE APPEAL OF EVERY DETAIL AND THE TOUCH OF
        THE
        FINEST FABRICS THAT SURROUND YOUR BODY IN PURE LUXURY. THE ONE YOU DON’T WANT TO TAKE OFF.
      </p><br>
      <p v-motion="slideVisibleOnceBottomMotion">
        CREATED AT FIRST AS A SMALL COLLECTION OF JUST THREE DRESSES, THE BRAND NOW OFFERS A CHOICE OF STUNNING
        ONE-OF-A-KIND PIECES THAT ARE MADE
        TO PERFECTION FOR YOU TO INDULGE YOURSELF, TO STEAL THE SHOW AND FEEL EXTRAORDINARY, WHENEVER YOU GO.
      </p>
    </div>
    <div class="block-4-mobile text-small">
      <div class="block-4-mobile_text">
        <p v-motion="slideVisibleOnceBottomMotion">WITH NO EXCEPTION, WE TAKE GREAT CARE OF THE DETAILS FROM FABRICS TO
          INDIVIDUAL MEASUREMENTS
          AND
          BEYOND TO
          PRODUCE YOUR PERFECT DRESS, BAR TO NONE.
        </p><br>
        <p v-motion="slideVisibleOnceBottomMotion">WE DON’T STOP UNTIL YOU GET THAT WOW-EFFECT. FROM THE EXPERIENCE WHEN
          YOU OPEN YOUR BOX, TILL THE MOMENT
          YOU
          STEP INSIDE THE ROOM AND AND TAKE EVERYONE'S BREATH AWAY. YOU ARE OUR INSPIRATION.</p>
      </div>
      <div class="block-4-mobile_image"><img :src="`${cloudfrontDistributionDomain}/img/about-4.webp`" alt="about 4"
          class="rect-image image-4"></div>
    </div>
    <div class="block-5-mobile text-small">
      <p v-motion="slideVisibleOnceBottomMotion">YSV BRAND IS INSPIRED BY STRONG AND BEAUTIFUL WOMAN WHO WANT TO FEEL
        UNAPOLOGETICALLY HERSELF, SHE WANTS TO
        EXPERIENCE LIFE AND FEEL DESIRED. SHE IS SOPHISTICATED AND REFINED.
      </p><br>
      <p v-motion="slideVisibleOnceBottomMotion">WITH THAT IN MIND, WE CREATED THE FINEST COLLECTIONS THAT ARE EQUALLY
        SENSUAL BUT ALSO ELEGANT AND CLASSY.
        IT’S
        AN ABSOLUTE LUXURY, BUT THE ONE YOU CAN AFFORD.</p><br>
      <p>WE SET THE BAR HIGH, SO YOU NOLONGER HAVE TO COMPROMISE. YOU CAN HAVE THE BEST OF ALL WORLDS.</p>
    </div>
  </div>
</template>
