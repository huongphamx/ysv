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
  <div class="collection-body">
    <div class="grid grid-cols-2 gap-5">
      <img :src="collectionPics![1]" class="rect-image" v-motion="{
        initial: { opacity: 0, x: -50 },
        enter: { opacity: 1, x: 0, transition: { duration: 800 } },
        delay: 500
      }">
      <div>
        <div class="text-medium">{{ mainCollection.name }} collection</div>
        <div class="my-[15px]">NEW OF 2023</div>
        <div class="view-all-btn">VIEW ALL
          <UIcon name="i-iconamoon-arrow-bottom-right-1-light" class="text-2xl ml-[10px]" />
        </div>
      </div>
    </div>
    <div class="grid grid-cols-2 gap-5">
      <div class="description-1 text-small">{{ mainCollection.main_collection_description }}</div>
      <img :src="collectionPics![2]" alt="" v-motion="slideVisibleOnceRightMotion">
    </div>
    <div class="text-small description-2">{{ mainCollection.main_collection_description_2 }}</div>
  </div>
</template>



<style scoped>
.collection-body {
  margin: 50px 0;

  @media screen and (min-width: 480px) {
    margin: 80px 0;
  }
}

.description-1 {
  margin-top: 15px;
  width: 140px;

  @media screen and (min-width: 480px) {
    margin-top: 20px;
    width: 207px;
  }
}

.description-2 {
  width: 216px;
  margin-top: 15px;
  margin-left: 80px;

  @media screen and (min-width: 480px) {
    width: 249px;
    margin-top: 20px;
    margin-left: 110px;
  }
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
}
</style>
