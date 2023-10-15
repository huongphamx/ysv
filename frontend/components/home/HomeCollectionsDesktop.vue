<script lang="ts" setup>
import { Collection } from '@/types'

const props = defineProps<{
  showCollections: Collection[]
}>()
</script>


<template>
  <div class="hidden xl:block mb-32">
    <div class="grid grid-cols-2 gap-2.5">
      <div>
        <div class="mb-5 grid grid-cols-2 gap-2.5">
          <CollectionCard v-if="showCollections[0]" :collection="showCollections[0]" />
          <CollectionCard v-if="showCollections[1]" :collection="showCollections[1]" />
        </div>
        <img src="/img/home-collection-square-1.webp" alt="" class="square-img" v-motion="slideVisibleOnceBottomMotion">
      </div>
      <div>
        <img src="/img/home-collection-square-2.webp" alt="" class="square-img" v-motion="slideVisibleOnceBottomMotion">
        <div class="my-5 grid grid-cols-2 gap-2.5">
          <CollectionCard v-if="showCollections[2]" :collection="showCollections[2]" />
          <CollectionCard v-if="showCollections[3]" :collection="showCollections[3]" />
        </div>
      </div>
    </div>
    <div class="grid grid-cols-2 gap-2.5">
      <div>
        <div class="mb-5 grid grid-cols-2 gap-2.5">
          <CollectionCard v-if="showCollections[4]" :collection="showCollections[4]" />
          <CollectionCard v-if="showCollections[5]" :collection="showCollections[5]" />
        </div>
        <img src="/img/home-collection-square-3.webp" alt="" class="square-img" v-motion="slideVisibleOnceBottomMotion">
      </div>
      <div>
        <div class="mb-5 grid grid-cols-2 gap-2.5">
          <CollectionCard v-if="showCollections[6]" :collection="showCollections[6]" />
          <CollectionCard v-if="showCollections[7]" :collection="showCollections[7]" />
        </div>
        <div class="mb-5 grid grid-cols-2 gap-2.5">
          <CollectionCard v-if="showCollections[8]" :collection="showCollections[8]" />
          <CollectionCard v-if="showCollections[9]" :collection="showCollections[9]" />
        </div>
        <NuxtLink to="/lookbook">
          <div class="lookbook-btn">LOOKBOOK
            <UIcon name="i-iconamoon-arrow-bottom-right-1-light" class="text-2xl" />
          </div>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>


<style scoped>
.lookbook-btn {
  width: 623px;
  height: 151px;
  border: 2px solid;
  display: flex;
  justify-content: center;
  align-items: center;

  &:hover {
    background-color: var(--black);
    color: white;
  }
}
</style>
