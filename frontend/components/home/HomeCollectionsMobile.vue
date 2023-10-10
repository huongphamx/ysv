<script lang="ts" setup>
import { Collection } from '@/types'

const props = defineProps<{
  showCollections: Collection[]
}>()
</script>


<template>
  <div class="xl:hidden">
    <div class="grid grid-cols-2 gap-4 justify-items-center">
      <CollectionCard :collection="showCollections[0]" />
      <CollectionCard :collection="showCollections[1]" />
      <CollectionCard :collection="showCollections[2]" />
      <CollectionCard :collection="showCollections[3]" />
    </div>
    <div class="my-4 mx-auto"><img src="/img/home-collection-square-1.webp" alt="" class="square-img"></div>
    <div class="grid grid-cols-2 gap-4 justify-items-center mb-4">
      <CollectionCard :collection="showCollections[4]" />
      <CollectionCard :collection="showCollections[5]" />
    </div>
    <div>
      <UButton block to="/lookbook" label="LOOKBOOK" variant="outline" color="black"
        :ui="{ rounded: '', gap: { sm: 'gap-x-0' }, base: 'md:py-10', size: { sm: 'md:text-lg' } }">
        <template #trailing>
          <UIcon name="i-iconamoon-arrow-bottom-right-1-light" class="text-2xl" />
        </template>
      </UButton>
    </div>
  </div>
</template>


<style scoped></style>
