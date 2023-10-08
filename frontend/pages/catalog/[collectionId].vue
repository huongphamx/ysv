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
</script>


<template>
  <div class="mycontainer mx-auto mb-10">
    <NuxtLink to="/collections/">
      <div class="my-5 items-center gap-2 hidden xl:flex">
        <UIcon name="i-ph-arrow-up-left" class="text-xl" /><span>LOOK ANOTHER COLLECTIONS</span>
      </div>
    </NuxtLink>

    <div class="my-5 flex flex-col items-center">
      <div v-for="p in productList" :key="p.id"
        class="grid grid-cols-2 gap-4 w-[300px] sm:w-[420px] md:w-[620px] lg:w-[768px] hover:cursor-pointer group"
        @click="$router.push(`/p/${p.id}`)">
        <div><img :src="p.preview_pic" alt="Product picture" class="w-[140px] sm:w-[200px] md:w-[220px] lg:w-[420px]">
        </div>
        <div class="flex flex-col justify-center group-hover:underline">
          <div class="text-2xl md:text-3xl lg:text-4xl font-['Italiana']">{{ p.collection.name.toUpperCase() }}</div>
          <div class="my-4 text-sm md:text-md lg:">AVAILABLE COLOR: {{ p.name.toUpperCase() }}</div>
          <div class="text-2xl md:text-3xl lg:text-4xl">${{ p.price }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

