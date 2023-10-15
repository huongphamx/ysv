<script lang="ts" setup>
import { Collection } from '@/types'

const props = defineProps<{
  showCollections: Collection[]
}>()
</script>


<template>
  <div class="xl:hidden">
    <div class="grid grid-cols-2 gap-5 justify-items-center">
      <CollectionCard v-if="showCollections[0]" :collection="showCollections[0]" />
      <CollectionCard v-if="showCollections[1]" :collection="showCollections[1]" />
      <CollectionCard v-if="showCollections[2]" :collection="showCollections[2]" />
      <CollectionCard v-if="showCollections[3]" :collection="showCollections[3]" />
    </div>
    <div class="my-5 mx-auto" v-motion="slideVisibleOnceBottomMotion"><img src="/img/home-collection-square-1.webp" alt=""
        class="square-img"></div>
    <div class="grid grid-cols-2 gap-5 justify-items-center mb-5">
      <CollectionCard v-if="showCollections[4]" :collection="showCollections[4]" />
      <CollectionCard v-if="showCollections[5]" :collection="showCollections[5]" />
    </div>
    <div>
      <NuxtLink to="/lookbook">
        <div class="lookbook-btn">LOOKBOOK
          <UIcon name="i-iconamoon-arrow-bottom-right-1-light" class="text-2xl" />
        </div>
      </NuxtLink>
    </div>
  </div>
</template>


<style scoped>
.lookbook-btn {
  width: 100%;
  height: 40px;
  border: 1px solid;
  display: flex;
  justify-content: center;
  align-items: center;

  &:hover {
    cursor: pointer;
    background-color: var(--black);
    color: white;
  }

  @media screen and (min-width: 480px) {
    height: 70px;
  }

  @media screen and (min-width: 768px) {
    height: 100px;
    border: 2px solid;
  }
}
</style>
