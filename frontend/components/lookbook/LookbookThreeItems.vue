<script lang="ts" setup>
import { Collection } from '@/types'

const props = defineProps<{
  collection: Collection,
}>()

</script>


<template>
  <div class="block-main">
    <img :src="collection.preview_pic" alt="" class="image-left">
    <div class="flex flex-col">
      <div class="flex-1">
        <div class="collection-name text-medium">{{ collection.name }} collection</div>
        <div class="collection-description text-small">{{ collection.descriptions }}</div>
      </div>
      <div>
        <div class="flex gap-[20px]">
          <img v-if="collection.products && collection.products.length > 0" :src="collection.products[0].preview_pic"
            alt="" class="image-right">
          <img v-if="collection.products && collection.products.length > 1" :src="collection.products[1].preview_pic"
            alt="" class="image-right">
        </div>
        <NuxtLink :to="`/catalog/${collection.id}`">
          <div class="view-all-btn mt-5">VIEW ALL
            <UIcon name="i-iconamoon-arrow-bottom-right-1" class="text-2xl" />
          </div>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>


<style scoped>
.block-main {
  display: flex;
  column-gap: 20px;
  margin: 80px auto;
}

.collection-description {
  margin: 30px 0;
}

.image-left {
  width: 520px;
  height: 781px;
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
    background-color: #272727;
    color: white;
  }
}
</style>
