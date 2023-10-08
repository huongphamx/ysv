<script setup lang="ts">
definePageMeta({
  layout: 'default-line-header',
})

useHead({
  title: 'Payment success - YSV'
})
</script>


<template>
  <div class="h-full mycontainer mx-auto flex flex-col gap-5 items-center justify-center">
    <div>
      <UIcon name="i-ph-check-circle" class="text-6xl text-green-500" />
    </div>
    <div class="text-lg md:text-3xl 2xl:text-4xl">
      PAYMENT SUCCESSFUL
    </div>
    <div class="text-base md:text-lg 2xl:text-xl">YOUR ORDER HAS BEEN PLACED</div>
    <div>
      <UButton @click="$router.back()" label="GO BACK" variant="outline" color="black"
        :ui="{ rounded: '', base: 'w-[300px] h-[60px] flex justify-center' }" />
    </div>
  </div>
</template>

