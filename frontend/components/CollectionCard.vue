<script setup lang="ts">
import { Collection } from '@/types'

const props = defineProps<{
  collection: Collection,
}>()
</script>


<template>
  <div class="relative hover:cursor-pointer group" @click="$router.push(`/catalog/${collection.id}`)"
    v-motion="popVisibleOnceMotion">
    <img :src="collection.preview_pic" alt="" class="rect-image">
    <div
      class="group-hover:hidden absolute bottom-0 max-w-[120px] sm:max-w-[180px] md:max-w-[250px] pl-4 pb-2 text-medium text-white">
      {{ collection.name.toUpperCase() }}
    </div>
    <div
      class="hidden xl:group-hover:flex xl:group-hover:flex-col items-center justify-center absolute top-0 left-0 rect-image bg-black opacity-70 text-center">
      <div class="w-[215px]">
        <div class=" text-white font-['Italiana'] text-3xl">{{ collection.name.toUpperCase() }}</div>
        <div class="h-[2px] bg-white"></div>
        <div class="text-white">{{ collection.descriptions.toUpperCase() }}</div>
      </div>
    </div>
  </div>
</template>
