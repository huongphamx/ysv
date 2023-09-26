<script lang="ts" setup>
definePageMeta({
  layout: 'default-line-header',
})
</script>


<template>
  <div class="mt-5 mb-24 container mx-auto">
    <div>
      <UButton label="GO BACK" icon="i-ph-arrow-up-left" to="/" variant="ghost" color="gray" />
    </div>
    <div class="my-5 flex gap-5 justify-center">
      <div class="max-w-[412px]">
        <NuxtPicture src="/img/image-27.png" />
        <div class="text-4xl my-6">DELIVERY/SHIPPING</div>
        <div class="text-xl my-6">AFTER “PLACING AN ORDER” WE WILL CONTACT YOU WITHIN 24 HOURS.</div>
        <div class="text-xl my-6">DELIVERY SHIPPING IN UAE WITHIN 1-3 DAYS STARTS FROM 4 $ -15 $</div>
        <div class="text-xl my-6">WORLDWIDE SHIPPING STARTS FROM 54 $ DEPENDING ON YOUR COUNTRY AND DELIVERY COMPANY.
          DELIVERY TIME UP TO 10-15 DAYS.</div>
        <div class="text-xl my-6">IT IS POSSIBLE TO PAY BY CRYPTOCURRENCY.</div>
      </div>
      <div>
        <img src="https://ysv-dev-static-img.s3.ap-northeast-1.amazonaws.com/image+25.png" />
      </div>
    </div>
  </div>
</template>

