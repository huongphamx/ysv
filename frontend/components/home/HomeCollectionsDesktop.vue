<script lang="ts" setup>
import { Collection } from '@/types'

const props = defineProps<{
  showCollections: Collection[]
}>()
</script>


<template>
  <div class="hidden xl:block mb-32">
    <div class="grid grid-cols-2 gap-3">
      <div>
        <div class="mb-6 grid grid-cols-2 gap-3">
          <CollectionCard :collection="showCollections[0]" />
          <CollectionCard :collection="showCollections[1]" />
        </div>
        <img src="/img/home-collection-square-1.webp" alt="" class="square-img">
      </div>
      <div>
        <img src="/img/home-collection-square-2.webp" alt="" class="square-img">
        <div class="my-6 grid grid-cols-2 gap-3">
          <CollectionCard :collection="showCollections[2]" />
          <CollectionCard :collection="showCollections[3]" />
        </div>
      </div>
    </div>
    <div class="grid grid-cols-2 gap-3">
      <div>
        <div class="mb-6 grid grid-cols-2 gap-3">
          <CollectionCard :collection="showCollections[4]" />
          <CollectionCard :collection="showCollections[5]" />
        </div>
        <img src="/img/home-collection-square-3.webp" alt="" class="square-img">
      </div>
      <div>
        <div class="mb-6 grid grid-cols-2 gap-3">
          <CollectionCard :collection="showCollections[6]" />
          <CollectionCard :collection="showCollections[7]" />
        </div>
        <div class="mb-6 grid grid-cols-2 gap-3">
          <CollectionCard :collection="showCollections[8]" />
          <CollectionCard :collection="showCollections[9]" />
        </div>
        <UButton label="LOOKBOOK" trailing-icon="i-iconamoon-arrow-bottom-right-1" to="/lookbook" variant="outline"
          color="black"
          :ui="{ rounded: '', base: 'h-[147px] w-[622px] flex justify-center', size: { sm: 'xl:text-xl' } }" />
      </div>
    </div>
  </div>
</template>


<style scoped></style>
