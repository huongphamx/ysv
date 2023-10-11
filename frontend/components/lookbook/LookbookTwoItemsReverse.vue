<script lang="ts" setup>
import { Collection } from '@/types'

const props = defineProps<{
  collection: Collection,
}>()

</script>


<template>
  <div class="block-main">
    <div class="flex flex-col ml-auto">
      <img v-if="collection.products && collection.products.length > 0" :src="collection.products[0].preview_pic" alt=""
        class="image-left">
      <div class="flex-1 flex flex-col gap-[20px] mt-[20px] xl:gap-[30px] xl:mt-[30px] max-w-[412px]">
        <div class="text-medium">{{ collection.name }} collection</div>
        <div class="text-small">{{ collection.descriptions }}</div>
      </div>
      <NuxtLink :to="`/catalog/${collection.id}`">
        <div class="view-all-btn">VIEW ALL
          <UIcon name="i-iconamoon-arrow-bottom-right-1" class="text-2xl" />
        </div>
      </NuxtLink>
    </div>
    <img :src="collection.preview_pic" alt="" class="image-right">
  </div>
</template>


<style scoped>
.block-main {
  display: flex;
  column-gap: 20px;
  margin: 80px 0 80px auto;
}

.image-left {
  width: 412px;
  height: 600px;
  object-fit: cover;
}

.image-right {
  width: 736px;
  height: 1106px;
  object-fit: cover;
}


.view-all-btn {
  width: 412px;
  height: 92px;
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
