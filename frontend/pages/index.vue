<script lang="ts" setup>

</script>


<template>
  <div class="-mt-16 relative">
    <video controls class="w-full h-auto">
      <source src="https://ysv-dev-static-img.s3.ap-northeast-1.amazonaws.com/hero.mp4" type="video/mp4">
    </video>
    <div class="mycontainer mx-auto">
      <div class="absolute bottom-0 text-6xl md:text-9xl text-white font-['Italiana']">YSV</div>
    </div>
  </div>
  <div class="mycontainer mx-auto">
    <div class="text-6xl md:text-9xl pl-16 md:pl-32 font-['Italiana']">BRAND</div>

    <div class="my-10 grid xl:grid-cols-2 gap-5">
      <div class="h-[962px] bg-[url('/img/main-prod-01.webp')] bg-cover hidden xl:block"></div>

      <div>
        <div class="grid grid-cols-2 gap-5">
          <div class="h-[480px] bg-[url('/img/main-prod-02.webp')] bg-no-repeat bg-cover"></div>
          <div>
            <div class="text-2xl lg:text-4xl font-['Italiana']">EXCLUSIVE SIHOUETTE COLLECTION</div>
            <div class="my-5">NEW OF 2023</div>
            <div>
              <UButton label="VIEW ALL" trailing-icon="i-ph-arrow-down-right" variant="outline" color="gray"
                :ui="{ rounded: '' }" />
            </div>
          </div>
        </div>
        <div class="grid grid-cols-2 gap-5">
          <div class="my-5 lg:text-xl">
            EMBRACE THE BEAUTY OF NATURE AND THE CHARM OF TIMELESS ELEGANCE WITH OUR BRAND-NEW COLLECTION OF DRESSES,
            "ELEGANCE IN BLOOM."
            INSPIRED BY THE DELICATE BLOSSOMS OF SPRING, THIS COLLECTION IS A CELEBRATION OF FEMININITY, GRACE, AND
            SOPHISTICATION.
          </div>
          <div class="h-[480px] bg-[url('/img/main-prod-03.webp')] bg-no-repeat"></div>
        </div>
      </div>
    </div>

    <div>
      <div class="text-5xl sm:text-7xl md:text-8xl xl:text-9xl text-center font-['Italiana']">COLLECTIONS</div>
      <div class="my-5 grid grid-cols-2">
        <div></div>
        <div>
          <UButton block size="xl" label="LOOKBOOK" trailing-icon="i-ph-arrow-down-right" to="/lookbook" variant="outline"
            color="gray" :ui="{ rounded: '' }" />
        </div>
      </div>
    </div>
  </div>
</template>

