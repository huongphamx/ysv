<script lang="ts" setup>
import { Collection } from '@/types'

const props = defineProps<{
  mainCollection: Collection
}>()

const collectionPics = computed(() => {
  return props.mainCollection.main_collection_pics?.split('$')
})
</script>


<template>
  <div class="collection-body flex gap-5">
    <img :src="collectionPics![0]" alt="" class="collection-image-1" v-motion="slideVisibleOnceLeftMotion">
    <div>
      <img :src="collectionPics![1]" alt="" class="collection-image-2" v-motion="slideVisibleOnceBottomMotion">
      <div class="text-small w-[279px] mt-[30px]" v-motion="slideVisibleOnceBottomMotion">
        <div>{{ mainCollection.main_collection_description }}</div>
        <div>{{ mainCollection.main_collection_description_2 }}</div>
      </div>
    </div>
    <div class="flex flex-col">
      <div class="text-medium" v-motion="slideVisibleOnceRightMotion">{{ mainCollection.name }} collection</div>
      <div class="my-[30px] text-small" v-motion="slideVisibleOnceRightMotion">NEW OF 2023</div>
      <div class="view-all-btn" v-motion="slideVisibleOnceRightMotion">VIEW ALL
        <UIcon name="i-iconamoon-arrow-bottom-right-1-light" class="text-2xl ml-[10px]" />
      </div>
      <img :src="collectionPics![2]" alt="" class="collection-image-2 mt-auto" v-motion="slideVisibleOnceRightMotion">
    </div>
  </div>
</template>


<style scoped>
.collection-body {
  margin: 150px 0;
}

.collection-image-1 {
  width: 628px;
  height: 962px;
}

.collection-image-2 {
  width: 304px;
  height: 462px;
}

.view-all-btn {
  width: 110px;
  height: 30px;
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
    width: 142px;
    height: 40px;
  }

  @media screen and (min-width: 768px) {
    width: 174px;
    height: 45px;
    border: 2px solid;
  }

  @media screen and (min-width: 1280px) {
    width: 196px;
    height: 50px;
  }
}
</style>
