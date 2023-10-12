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

const isShowedHeaderLine = useIsShowedHeaderLine()
isShowedHeaderLine.value = true
</script>


<template>
  <div class="mycontainer mx-auto mb-12 xl:mb-24">
    <div class="w-fit">
      <NuxtLink to="/lookbook">
        <div class="my-10 items-center gap-2 hidden xl:flex text-gray-500 hover:border-b hover:border-[#272727]">
          <UIcon name="i-iconamoon-arrow-top-left-1" class="text-2xl" /><span>LOOK ANOTHER COLLECTIONS</span>
        </div>
      </NuxtLink>
    </div>

    <div class="product-card xl:items-center">
      <div v-for="p in productList" :key="p.id" class="flex hover:cursor-pointer group"
        @click="$router.push(`/p/${p.id}`)">
        <img :src="p.preview_pic" alt="Product picture" class="rect-image collection-catalog">
        <div class="product-description group-hover:underline">
          <div class="text-medium">{{ p.collection.name }} COLLECTION</div>
          <div class="product-color">AVAILABLE COLOR: {{ p.name }}</div>
          <div class="product-price">${{ p.price }}</div>
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped>
.product-card {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 50px;

  @media screen and (min-width: 480px) {
    gap: 30px;
    margin-bottom: 80px;
  }

  @media screen and (min-width: 1280px) {
    gap: 80px;
    margin-bottom: 150px;
  }
}

.product-description {
  display: flex;
  flex-direction: column;
  gap: 15px;
  justify-content: center;
  margin-left: 20px;

  @media screen and (min-width: 480px) {
    gap: 20px;
  }

  @media screen and (min-width: 768px) {
    gap: 30px;
    max-width: 334px;
  }

  @media screen and (min-width: 1280px) {
    max-width: 412px;
  }
}

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