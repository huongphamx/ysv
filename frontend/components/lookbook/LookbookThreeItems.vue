<script lang="ts" setup>
import { Collection } from '@/types'

const props = defineProps<{
  collection: Collection,
}>()

</script>


<template>
  <div>
    <div class="block-main">
      <img :src="collection.preview_pic" alt="" class="image-left" v-motion="slideVisibleOnceLeftMotion">
      <div class="flex flex-col">
        <div class="flex-1 max-w-[628px]">
          <div class="collection-name text-medium" v-motion="slideVisibleOnceRightMotion">{{ collection.name }} collection
          </div>
          <div class="collection-description text-small" v-motion="slideVisibleOnceRightMotion">{{ collection.descriptions
          }}</div>
        </div>
        <div>
          <div class="flex gap-[20px]">
            <img v-if="collection.products && collection.products.length > 0" :src="collection.products[0].preview_pic"
              alt="" class="image-right" v-motion="slideVisibleOnceRightMotion">
            <img v-if="collection.products && collection.products.length > 1" :src="collection.products[1].preview_pic"
              alt="" class="image-right" v-motion="slideVisibleOnceRightMotion">
          </div>
          <NuxtLink :to="`/catalog/${collection.id}`">
            <div class="view-all-btn mt-5">VIEW ALL
              <UIcon name="i-iconamoon-arrow-bottom-right-1" class="text-2xl" />
            </div>
          </NuxtLink>
        </div>
      </div>
    </div>
    <div class="block-mobile">
      <LookbookMobile :collection="collection" />
    </div>
  </div>
</template>


<style scoped>
.block-main {
  display: flex;
  column-gap: 20px;

  @media screen and (max-width: 1279px) {
    display: none;
  }
}

.block-mobile {
  display: block;

  @media screen and (min-width: 1280px) {
    display: none;
  }
}

.collection-description {
  margin: 30px 0;
}

.image-left {
  width: 520px;
  height: 780px;
  object-fit: cover;
}

.image-right {
  width: 304px;
  height: 457px;
  object-fit: cover;
}

.view-all-btn {
  width: 628px;
  height: 143px;
  font-size: 20px;
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
