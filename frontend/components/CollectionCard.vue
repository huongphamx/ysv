<script setup lang="ts">
import { Collection } from '@/types'

const props = defineProps<{
  collection: Collection,
}>()
</script>


<template>
  <div class="relative hover:cursor-pointer group" @click="$router.push(`/catalog/${collection.id}`)">
    <img :src="collection.preview_pic" alt="" class="rect-img">
    <div
      class="group-hover:hidden absolute bottom-0 max-w-[120px] sm:max-w-[180px] md:max-w-[250px] pl-2 text-xl sm:text-2xl md:text-3xl 2xl:text-4xl font-['Italiana'] text-[#FFFFFF]">
      {{ collection.name.toUpperCase() }}
    </div>
    <div
      class="hidden 2xl:group-hover:flex 2xl:group-hover:flex-col items-center justify-center absolute top-0 left-0 w-[300px] h-full bg-black opacity-70 text-center">
      <div class="border-b border-white text-white font-['Italiana'] text-4xl">{{ collection.name.toUpperCase() }}</div>
      <div class="text-white">{{ collection.descriptions.toUpperCase() }}</div>
    </div>
  </div>
</template>
