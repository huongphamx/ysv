<script lang="ts" setup>
import { Collection } from '@/types'

const props = defineProps<{
  collection: Collection,
}>()

</script>


<template>
  <div>
    <div class="block-main">
      <div class="flex flex-col">
        <img v-if="collection.products && collection.products.length > 0" :src="collection.products[0].preview_pic" alt=""
          class="image-left" v-motion="slideVisibleOnceBottomMotion">
        <div class="flex-1 flex flex-col gap-[20px] mt-[20px] xl:gap-[30px] xl:mt-[30px] max-w-[304px]">
          <div class="text-medium" v-motion="slideVisibleOnceBottomMotion">{{ collection.name }} collection</div>
          <div class="text-small" v-motion="slideVisibleOnceBottomMotion">{{ collection.descriptions }}</div>
        </div>
        <NuxtLink :to="`/catalog/${collection.id}`">
          <div class="view-all-btn">VIEW ALL
            <UIcon name="i-iconamoon-arrow-bottom-right-1" class="text-2xl" />
          </div>
        </NuxtLink>
      </div>
      <img :src="collection.preview_pic" alt="" class="image-right" v-motion="slideVisibleOnceBottomMotion">
    </div>
    <div class="block-mobile">
      <LookbookMobile :collection="collection" />
    </div>
  </div>
</template>


<style scoped>
.block-main {
  display: flex;
  justify-content: center;
  column-gap: 20px;
  margin-left: auto;

  @media screen and (max-width: 1279px) {
    display: none;
  }
}

.block-mobile {
  @media screen and (min-width: 1280px) {
    display: none;
  }
}

.image-left {
  width: 304px;
  height: 442px;
  object-fit: cover;
}

.image-right {
  width: 520px;
  height: 780px;
  object-fit: cover;
}


.view-all-btn {
  width: 304px;
  height: 92px;
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
