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
    <div
      class="my-5 h-[892px] bg-[url('/img/cooperation.webp')] bg-no-repeat bg-center flex flex-col justify-center items-center">
      <div class="text-4xl">LET'S WORK TOGETHER</div>
      <div class="mt-10 text-xl">FOR COOPERATION DROP A MESSAGE ON</div>
      <div class="text-xl">ysv.shukshina@gmail.com</div>
    </div>
  </div>
</template>

