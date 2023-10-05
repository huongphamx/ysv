<script setup lang="ts">
import { Collection } from '@/types'

const props = defineProps<{
  collection: Collection,
}>()
</script>


<template>
  <div class="relative hover:cursor-pointer" @click="$router.push(`/catalog/${collection.id}`)">
    <img :src="collection.preview_pic" alt="" class="rect-img">
    <div
      class="absolute bottom-0 max-w-[120px] sm:max-w-[180px] md:max-w-[250px] pl-2 text-xl sm:text-2xl md:text-3xl 2xl:text-4xl font-['Italiana'] text-[#FFFFFF]">
      {{
        collection.name.toUpperCase() }}</div>
  </div>
</template>
