<script setup lang="ts">
import { Collection } from '~/types';

const props = defineProps<{
  collection: Collection
}>()

const lookbookPics = computed(() => {
  if (props.collection.products) {
    if (props.collection.products.length === 1) {
      return props.collection.products.map(p => p.preview_pic).concat(props.collection.preview_pic)
    } else {
      return props.collection.products.map(p => p.preview_pic)
    }
  }
  return []
})
</script>

<template>
  <div v-if="collection.products?.length" class="my-8">
    <div class="xl:hidden">
      <div class="mb-2 text-xl sm:text-2xl md:text-3xl font-['Italiana']">{{ collection.name.toUpperCase() }}</div>
      <div class="mb-1 text-sm sm:text-base md:text-lg">{{ collection.descriptions.toUpperCase() }}</div>
    </div>
    <div class="xl:grid xl:grid-cols-2 gap-3">
      <div class="my-2 grid grid-cols-2 gap-3">
        <img v-if="lookbookPics[0]" :src="lookbookPics[0]" alt="" class="rect-img">
        <img v-if="lookbookPics[1]" :src="lookbookPics[1]" alt="" class="rect-img">
      </div>
      <div class="flex flex-col">
        <div class="hidden xl:block">
          <div class="text-3xl font-['Italiana']">{{ collection.name.toUpperCase() }}</div>
          <div class="text-lg">{{ collection.descriptions.toUpperCase() }}</div>
        </div>
        <UButton :to="`/catalog/${collection.id}`" label="VIEW ALL" variant="outline" color="black"
          trailing-icon="i-ph-arrow-down-right"
          :ui="{ rounded: '', base: 'w-full h-[40px] sm:h-[60px] md:h-[80px] flex justify-center' }" />
      </div>
    </div>
  </div>
</template>
