<script lang="ts" setup>

</script>


<template>
  <div class="-mt-16 h-[600px] bg-[url('/img/hero.png')] relative">
    <div class="pt-16 container mx-auto">
      <div class="absolute bottom-0 text-9xl text-white">YSV</div>
    </div>
  </div>
  <div class="container mx-auto">
    <div class="text-9xl ml-32">BRAND</div>

    <div class="my-10 grid grid-cols-2 gap-5">
      <div class="h-[962px] bg-[url('/img/image-17.png')] bg-cover"></div>
      <div class="grid grid-cols-2 gap-5">
        <div>
          <div class="h-[480px] bg-[url('/img/image-16.png')]"></div>
          <div class="my-5 text-xl">
            EMBRACE THE BEAUTY OF NATURE AND THE CHARM OF TIMELESS ELEGANCE WITH OUR BRAND-NEW COLLECTION OF DRESSES, "ELEGANCE IN BLOOM." 
            INSPIRED BY THE DELICATE BLOSSOMS OF SPRING, THIS COLLECTION IS A CELEBRATION OF FEMININITY, GRACE, AND SOPHISTICATION.
          </div>
        </div>
        <div>
          <div class="text-4xl">EXCLUSIVE SIHOUETTE COLLECTION</div>
          <div class="my-5">NEW OF 2023</div>
          <div><UButton label="VIEW ALL" trailing-icon="i-ph-arrow-down-right" variant="outline" color="gray" :ui="{rounded: ''}"/></div>
        </div>
      </div>
    </div>

    <div>
      <div class="text-9xl text-center">COLLECTIONS</div>
      <div class="my-5 grid grid-cols-2">
        <div></div>
        <div>
          <UButton block size="xl" label="LOOKBOOK" trailing-icon="i-ph-arrow-down-right" to="/lookbook" variant="outline" color="gray" :ui="{rounded: ''}" />
        </div>
      </div>
    </div>
  </div>
</template>

