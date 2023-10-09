<script lang="ts" setup>
definePageMeta({
  layout: 'default-line-header',
})

useHead({
  title: 'Payment & Delivery - YSV'
})
</script>


<template>
  <div class="mt-5 mb-24 mycontainer mx-auto">
    <GoBackArrow />

    <div class="my-5 flex flex-col-reverse md:flex-row gap-5 justify-center">
      <div class="md:w-1/2 2xl:w-1/3">
        <div class="hidden 2xl:block">
          <img src="/img/delivery-1.webp" />
        </div>

        <div>
          <div class="text-xl sm:text-2xl md:text-3xl 2xl:text-4xl my-6 font-['Italiana']">DELIVERY/SHIPPING</div>
          <div class="text-sm sm:text-base md:text-lg 2xl:text-xl my-6">AFTER “PLACING AN ORDER” WE WILL CONTACT YOU
            WITHIN 24 HOURS.</div>
          <div class="text-sm sm:text-base md:text-lg 2xl:text-xl my-6">DELIVERY SHIPPING IN UAE WITHIN 1-3 DAYS STARTS
            FROM 4 $ -15 $</div>
          <div class="text-sm sm:text-base md:text-lg 2xl:text-xl my-6">WORLDWIDE SHIPPING STARTS FROM 54 $ DEPENDING ON
            YOUR COUNTRY AND
            DELIVERY
            COMPANY.
            DELIVERY TIME UP TO 10-15 DAYS.</div>
          <div class="text-sm sm:text-base md:text-lg 2xl:text-xl my-6">IT IS POSSIBLE TO PAY BY CRYPTOCURRENCY.</div>
        </div>
      </div>

      <div class="md:w-1/2 2xl:w-2/3">
        <img src="/img/delivery-2.webp" />
      </div>
    </div>
  </div>
</template>

