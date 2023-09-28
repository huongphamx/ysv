<script lang="ts" setup>
const props = defineProps({
  isShowBottomLine: {
    type: Boolean,
    default: false,
  }
})
</script>


<template>
  <div class="z-10 py-2" :class="{ 'border-b': isShowBottomLine }">
    <div class="h-12 mycontainer mx-auto flex justify-between items-center text-white">
      <div class="text-2xl">
        <NuxtLink to="/">YSV</NuxtLink>
      </div>
      <div class="w-2/3 flex justify-between">
        <NuxtLink to="/about">ABOUT</NuxtLink>
        <NuxtLink to="/events">EVENTS</NuxtLink>
        <NuxtLink to="/contact">CONTACT</NuxtLink>
        <NuxtLink to="/payment-delivery">PAYMENT & DELIVERY</NuxtLink>
        <NuxtLink to="/cooperation">COOPERATION</NuxtLink>
        <NuxtLink to="/collections">
          <div class="flex items-center">COLLECTIONS
            <UIcon name="i-ph-arrow-down-right" />
          </div>
        </NuxtLink>
      </div>
      <div>
        <UButton icon="i-ph-heart" color="gray" variant="ghost" />
      </div>
    </div>
  </div>
</template>

