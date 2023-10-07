<script lang="ts" setup>

</script>


<template>
  <div class="border-t py-2">
    <div class="mycontainer mx-auto grid grid-cols-2 lg:grid-cols-3 justify-items-center">
      <div class="text-sm lg:text-md">
        <div class="my-4 text-xl lg:text-2xl font-['Italiana']">YSV</div>
        <div>
          <NuxtLink to="/lookbook">LOOKBOOK</NuxtLink>
        </div>
        <!-- <div>
          <NuxtLink to="/all-collections">ALL COLLECTIONS</NuxtLink>
        </div>
        <div>
          <NuxtLink to="/limited-collection">LIMITED COLLECTION</NuxtLink>
        </div> -->
        <div>
          <NuxtLink to="/size-guide">SIZE GUIDE</NuxtLink>
        </div>
        <div class="my-4 opacity-50">
          <div>
            <UIcon name="i-ph-at" /> YSV BRAND
          </div>
          <div>ALL RIGHTS RESERVED</div>
        </div>
      </div>
      <div class="text-sm lg:text-md">
        <div class="my-4 text-xl lg:text-2xl font-['Italiana']">FOR CLIENT</div>
        <div>
          <NuxtLink to="/about">ABOUT</NuxtLink>
        </div>
        <div>
          <NuxtLink to="/payment-delivery">DELIVERY</NuxtLink>
        </div>
        <div>
          <NuxtLink to="/cooperation">COOPERATION</NuxtLink>
        </div>
        <div class="my-4 opacity-50">
          <NuxtLink to="/privacy-policy">PRIVACY POLICY</NuxtLink>
        </div>
      </div>
      <div class="text-sm lg:text-md">
        <div class="my-4 text-xl lg:text-2xl font-['Italiana']">JOIN US</div>
        <div><a href="https://instagram.com/ysv.brand?igshid=MzRlODBiNWFlZA==" target="_blank">INSTAGRAM</a></div>
        <div><a href="https://youtube.com" target="_blank">YOUTUBE</a></div>
        <div><a href="https://api.whatsapp.com/send?phone=971545602477" target="_blank">WHATSAPP</a></div>
        <div><a href="https://telegram.com" target="_blank">TELEGRAM</a></div>
        <!-- <div class="my-4 opacity-50">
          WEBSITE DEVELOPMENT
        </div> -->
      </div>
      <!-- <div>
        <div class="my-4 text-xl lg:text-2xl font-['Italiana']">SUBSCRIBE</div>
        <div class="flex">
          <UInput placeholder="YOUR EMAIL" :ui="{ rounded: '' }" />
          <UButton icon="i-ph-arrow-down-right" variant="outline" color="gray" :ui="{ rounded: '' }" />
        </div>
      </div> -->
    </div>
  </div>
</template>

