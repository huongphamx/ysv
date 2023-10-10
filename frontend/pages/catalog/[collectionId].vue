<script setup lang="ts">
import { Collection } from '@/types'

const { params } = useRoute()
const collectionId = params.collectionId as string

const collectionData = ref<Collection>()
const { data: collectionDetail, error: getCollectionError } = await useCustomFetch<Collection>(`/v1/collections/${collectionId}`)
if (getCollectionError.value) {
  // todo: toast
} else if (collectionDetail.value) {
  collectionData.value = collectionDetail.value
}

const productList = useProductList()
await getProductList({ collection_id: collectionId })

definePageMeta({
  layout: 'default-line-header'
})
</script>


<template>
  <div class="mycontainer mx-auto mb-12 xl:mb-24">
    <NuxtLink to="/lookbook">
      <div class="my-10 items-center gap-2 hidden xl:flex text-gray-500">
        <UIcon name="i-iconamoon-arrow-top-left-1" class="text-2xl" /><span>LOOK ANOTHER COLLECTIONS</span>
      </div>
    </NuxtLink>

    <div class="mt-5 mb-5 md:mb-14 flex flex-col gap-5 md:gap-10 xl:gap-20 xl:items-center">
      <div v-for="p in productList" :key="p.id" class="flex gap-4 hover:cursor-pointer group"
        @click="$router.push(`/p/${p.id}`)">
        <div><img :src="p.preview_pic" alt="Product picture" class="rect-image collection-catalog">
        </div>
        <div class="flex flex-col justify-center group-hover:underline">
          <div class="text-medium">{{ p.collection.name }} COLLECTION</div>
          <div class="my-4 product-color">AVAILABLE COLOR: {{ p.name }}</div>
          <div class="product-price">${{ p.price }}</div>
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped>
.product-color {
  color: #888888;
  font-size: 12px;
  text-transform: uppercase;

  @media screen and (min-width: 480px) {
    font-size: 14px;
  }

  @media screen and (min-width: 768px) {
    font-size: 16px;
  }
}

.product-price {
  font-size: 20px;
  text-transform: uppercase;

  @media screen and (min-width: 480px) {
    font-size: 26px;
  }

  @media screen and (min-width: 768px) {
    font-size: 32px;
  }

  @media screen and (min-width: 1280px) {
    font-size: 36px;
  }
}
</style>