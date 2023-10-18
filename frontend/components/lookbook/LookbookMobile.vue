<script lang="ts" setup>
import { Collection } from '@/types'

const props = defineProps<{
  collection: Collection,
}>()
</script>


<template>
  <div class="block-main-mobile">
    <div class="text-medium" v-motion="slideVisibleOnceBottomMotion">{{ collection.name }} collection</div>
    <div class="description text-small" v-motion="slideVisibleOnceBottomMotion">{{ collection.descriptions }}</div>
    <div class="grid grid-cols-2 gap-5">
      <img :src="collection.preview_pic" alt="" class="rect-image" v-motion="slideVisibleOnceBottomMotion">
      <img v-if="collection.products && collection.products.length > 0" :src="collection.products[0].preview_pic" alt=""
        class="rect-image" v-motion="slideVisibleOnceBottomMotion">
    </div>
    <NuxtLink :to="`/catalog/${collection.id}`">
      <div class="view-all-btn">VIEW ALL
        <UIcon name="i-iconamoon-arrow-bottom-right-1" class="text-2xl" />
      </div>
    </NuxtLink>
  </div>
</template>


<style scoped>
.block-main {
  margin: 30px auto;

  @media screen and (min-width: 480px) {
    margin: 50px auto;
  }

  @media screen and (min-width: 768px) {
    margin: 100px auto;
  }

  @media screen and (min-width: 1280px) {
    display: none;
  }
}

.description {
  margin-top: 15px;
  margin-bottom: 15px;
}

.view-all-btn {
  width: 100%;
  height: 40px;
  margin-top: 20px;
  border: 1px solid;
  display: flex;
  justify-content: center;
  align-items: center;

  &:hover {
    background-color: var(--black);
    color: white;
  }

  @media screen and (min-width: 480px) {
    height: 70px;
  }

  @media screen and (min-width: 768px) {
    height: 100px;
    border: 2px solid;
    font-size: 18px;
  }
}
</style>
