<script lang="ts" setup>

</script>


<template>
  <div class="mycontainer mx-auto mb-10">
    <div class="relative">
      <img src="/img/about-hero.webp" alt="event hero" class="about-hero" />
      <div class="absolute bottom-0 text-5xl sm:text-6xl md:text-8xl xl:text-[200px] text-white font-['Italiana']">ABOUT
      </div>
    </div>
    <div class="pl-16 text-5xl sm:text-6xl md:text-8xl xl:text-[200px] font-['Italiana']">THE BRAND</div>

    <div class="my-10 grid grid-cols-2 gap-3">
      <div>
        <div class="text-sm sm:text-base md:text-lg xl:text-xl">SENSUALITY WITH STYLE. LUXURY FOR THE WOMAN WHO DESERVES
          IT. FOR YOUR
          INNER
          GODDESS. YOUR
          KIND OF LUXURY. SENSUAL. ELEGANT. CLASSY. EXTRAORDINARY. JUST LIKE YOU.</div>
        <img src="/img/about-1.webp" alt="about 1" class="about-img">
      </div>
      <img src="/img/about-2.webp" alt="about 2" class="about-img">
    </div>

    <div class="text-xl sm:text-2xl md:text-3xl xl:text-4xl text-center font-['Italiana']">“YOUR LIFE IS A STAGE. YOU
      DESERVE TO SHINE
      ON IT. YSV
      IS NOT YOUR
      ORDINARY
      DRESS. IT’S EXQUISITE, IT’S SENSUAL, IT’S YOU.”</div>
    <div class="mt-2 flex justify-center"><img src="/img/about-sign.svg" alt="about sign" class="w-[200px] md:w-[300px]">
    </div>

    <div class="my-5 grid grid-cols-2 gap-3">
      <img src="/img/about-3.webp" alt="about 3" class="about-img">
      <img src="/img/about-5.webp" alt="about 5" class="about-img">
    </div>

    <div class="flex flex-col gap-5 text-sm sm:text-base md:text-lg xl:text-xl">
      <div>
        THE FOUNDER OF THE BRAND YULIA SHUKSHINA DREW HER INSPIRATION FROM PROFESSIONAL DANCING BY CREATING A BRAND THAT
        IS EVERYTHING YOU WERE LOOKING FOR AND MORE. SHE WANTED TO BRING THE GLAM AND CHIC THAT YOU SEE ON STAGE TO THE
        WARDROBE OF ANY WOMAN WHO WANTS TO BE NOTICED.
      </div>
      <div>
        YSV IS MADE FOR WOMEN WITH HIGH STANDARDS, WHO APPRECIATE DISTINCTIVE APPEAL OF EVERY DETAIL AND THE TOUCH OF THE
        FINEST FABRICS THAT SURROUND YOUR BODY IN PURE LUXURY. THE ONE YOU DON’T WANT TO TAKE OFF.
      </div>
      <div>
        CREATED AT FIRST AS A SMALL COLLECTION OF JUST THREE DRESSES, THE BRAND NOW OFFERS A CHOICE OF STUNNING
        ONE-OF-A-KIND PIECES THAT ARE MADE
        TO PERFECTION FOR YOU TO INDULGE YOURSELF, TO STEAL THE SHOW AND FEEL EXTRAORDINARY, WHENEVER YOU GO.
      </div>
    </div>

    <div class="my-5 grid grid-cols-2 gap-3 text-sm sm:text-base md:text-lg xl:text-xl">
      <div>
        <div class="my-3">WITH NO EXCEPTION, WE TAKE GREAT CARE OF THE DETAILS FROM FABRICS TO INDIVIDUAL MEASUREMENTS AND
          BEYOND TO
          PRODUCE YOUR PERFECT DRESS, BAR TO NONE.
        </div>
        <div>WE DON’T STOP UNTIL YOU GET THAT WOW-EFFECT. FROM THE EXPERIENCE WHEN YOU OPEN YOUR BOX, TILL THE MOMENT YOU
          STEP INSIDE THE ROOM AND AND TAKE EVERYONE'S BREATH AWAY. YOU ARE OUR INSPIRATION.</div>
      </div>
      <div class="flex items-center"><img src="/img/about-4.webp" alt="about 4" class="about-img"></div>
    </div>

    <div class="text-sm flex flex-col gap-3 sm:text-base md:text-lg xl:text-xl">
      <div>YSV BRAND IS INSPIRED BY STRONG AND BEAUTIFUL WOMAN WHO WANT TO FEEL UNAPOLOGETICALLY HERSELF, SHE WANTS TO
        EXPERIENCE LIFE AND FEEL DESIRED. SHE IS SOPHISTICATED AND REFINED.
      </div>
      <div>WITH THAT IN MIND, WE CREATED THE FINEST COLLECTIONS THAT ARE EQUALLY SENSUAL BUT ALSO ELEGANT AND CLASSY. IT’S
        AN ABSOLUTE LUXURY, BUT THE ONE YOU CAN AFFORD.</div>
      <div>WE SET THE BAR HIGH, SO YOU NOLONGER HAVE TO COMPROMISE. YOU CAN HAVE THE BEST OF ALL WORLDS.</div>
    </div>

    <div class="xl:relative">
      <img src="/img/about-6.webp" alt="about 6" class="my-3 about-end">
      <div
        class="text-xl sm:text-2xl md:text-3xl xl:text-4xl text-center font-['Italiana'] xl:absolute xl:top-1/2 xl:left-1/2 xl:-translate-x-1/2 xl:-translate-y-1/2 xl:text-white xl:w-[600px]">
        INDULGE IN LUXURY LIKE NEVER
        BEFORE WITH
        YSV BRAND.
        IT’S YOUR TIME
        TO SHINE, DARLING.
      </div>
    </div>
  </div>
</template>


<style scoped>
.about-hero {
  width: 300px;
  height: 400px;
  object-fit: cover;
}

.about-img {
  width: 140px;
  height: 210px;
  object-fit: cover;
}

.about-end {
  width: 300px;
  height: 220px;
  object-fit: cover;
}

@media screen and (min-width: 480px) {
  .about-hero {
    width: 420px;
    height: 500px;
    object-fit: cover;
  }

  .about-img {
    width: 200px;
    height: 300px;
    object-fit: cover;
  }

  .about-end {
    width: 422px;
    height: 300px;
    object-fit: cover;
  }
}

@media screen and (min-width: 768px) {
  .about-hero {
    width: 620px;
    height: 540px;
    object-fit: cover;
  }

  .about-img {
    width: 300px;
    height: 500px;
    object-fit: cover;
  }

  .about-end {
    width: 620px;
    height: 300px;
    object-fit: cover;
  }
}

@media screen and (min-width: 1024px) {
  .about-hero {
    width: 700px;
    height: 540px;
    object-fit: cover;
  }

  .about-img {
    width: 340px;
    height: 520px;
    object-fit: cover;
  }

  .about-end {
    width: 680px;
    height: 300px;
    object-fit: cover;
  }
}

@media screen and (min-width: 1280px) {
  .about-hero {
    width: 1276px;
    height: 836px;
    object-fit: cover;
  }

  .about-img {
    width: 628px;
    height: 785px;
    object-fit: cover;
  }

  .about-end {
    width: 1276px;
    height: 592px;
    object-fit: cover;
  }
}
</style>