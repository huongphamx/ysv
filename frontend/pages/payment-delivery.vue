<script lang="ts" setup>
definePageMeta({
  layout: 'default-line-header',
})
</script>


<template>
  <div class="mt-5 mb-24 mycontainer mx-auto">
    <div>
      <NuxtLink to="/">
        <div class="flex items-center gap-2">
          <UIcon name="i-ph-arrow-up-left" class="text-xl" /><span>GO BACK</span>
        </div>
      </NuxtLink>
    </div>
    <div class="my-5 flex gap-5 justify-center">
      <div class="max-w-[412px]">
        <NuxtPicture src="/img/delivery-01.webp" />
        <div class="text-4xl my-6 font-['Italiana']">DELIVERY/SHIPPING</div>
        <div class="text-xl my-6">AFTER “PLACING AN ORDER” WE WILL CONTACT YOU WITHIN 24 HOURS.</div>
        <div class="text-xl my-6">DELIVERY SHIPPING IN UAE WITHIN 1-3 DAYS STARTS FROM 4 $ -15 $</div>
        <div class="text-xl my-6">WORLDWIDE SHIPPING STARTS FROM 54 $ DEPENDING ON YOUR COUNTRY AND DELIVERY COMPANY.
          DELIVERY TIME UP TO 10-15 DAYS.</div>
        <div class="text-xl my-6">IT IS POSSIBLE TO PAY BY CRYPTOCURRENCY.</div>
      </div>
      <div>
        <img src="/img/delivery-02.webp" />
      </div>
    </div>
  </div>
</template>

