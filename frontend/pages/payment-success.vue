<script setup lang="ts">
const isShowedHeaderLine = useIsShowedHeaderLine()
isShowedHeaderLine.value = true

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
    <div class="text-small text-center">YOUR ORDER HAS BEEN PLACED. MANAGER WILL CONTACT YOU SOON VIA WHATSAPP.
    </div>
    <div>
      <UButton @click="$router.back()" label="GO BACK" variant="outline" color="black"
        :ui="{ rounded: '', base: 'w-[300px] h-[60px] flex justify-center' }" />
    </div>
  </div>
</template>

