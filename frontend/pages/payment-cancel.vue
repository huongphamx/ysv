<script setup lang="ts">
const isShowedHeaderLine = useIsShowedHeaderLine()
isShowedHeaderLine.value = true

useHead({
  title: 'Payment cancel - YSV'
})
</script>


<template>
  <div class="h-full mycontainer mx-auto flex flex-col gap-5 items-center justify-center">
    <div>
      <UIcon name="i-ph-x-circle" class="text-6xl text-red-500" />
    </div>
    <div class="text-lg md:text-3xl 2xl:text-4xl">
      PAYMENT CANCELED
    </div>
    <div class="text-base md:text-lg 2xl:text-xl">SOMETHING WENT WRONG, PLEASE TRY AGAIN</div>
    <div>
      <UButton @click="$router.back()" label="GO BACK" variant="outline" color="black"
        :ui="{ rounded: '', base: 'w-[300px] h-[60px] flex justify-center' }" />
    </div>
  </div>
</template>

