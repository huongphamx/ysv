<script setup lang="ts">
import { Product } from '@/types'

const { params } = useRoute()
const productId = params.productId as string
const productData = ref<Product>()

const { data, error } = await useCustomFetch<Product>(`/v1/products/${productId}`)
if (error.value) {
  // todo: toast
  // todo: if product not found, raise 404 page
} else if (data.value) {
  productData.value = data.value
}
const showedBigPicture = ref(productData.value?.pictures[0].url)

const startPictureIndex = ref(0)
const nextPicture = () => {
  if (startPictureIndex.value + 4 >= productData.value?.pictures.length!) return
  startPictureIndex.value += 1
}
const prePicture = () => {
  if (startPictureIndex.value <= 0) return
  startPictureIndex.value -= 1
}
const showedSmallPictures = computed(() => {
  return productData.value?.pictures.slice(startPictureIndex.value, startPictureIndex.value + 4)
})

definePageMeta({
  layout: 'default-line-header',
})
</script>


<template>
  <div class="mycontainer mx-auto pb-10">
    <NuxtLink to="/collections/">
      <div class="my-5 flex items-center gap-2">
        <UIcon name="i-ph-arrow-up-left" class="text-xl" /><span>LOOK ANOTHER COLLECTIONS</span>
      </div>
    </NuxtLink>

    <div class="flex gap-4">
      <div id="product-pictures" class="flex flex-col md:flex-row lg:flex-col gap-3">
        <div class="text-center">
          <UButton icon="i-ph-arrow-up" variant="ghost" color="gray" @click="prePicture" />
        </div>
        <div v-for="image in showedSmallPictures" :key="image.id" @click="showedBigPicture = image.url"
          :class="{ 'border border-gray-500': showedBigPicture === image.url }">
          <img :src="image.url" alt="Product pic" class="w-[88px]">
        </div>
        <div class="text-center">
          <UButton icon="i-ph-arrow-down" variant="ghost" color="gray" @click="nextPicture" />
        </div>
      </div>

      <div id="product-preview-picture">
        <img :src="showedBigPicture" alt="Product proview picture" class="w-[411px]">
        <ProductAddToCart />
      </div>

      <div class="max-w-[412px]">
        <div class="text-4xl font-['Italiana']">
          {{ productData?.collection.name.toUpperCase() }}
        </div>
        <div class="my-5 text-gray-500">AVAILABLE COLORS: {{ productData?.name.toUpperCase() }}</div>
        <div class="my-8 text-4xl">${{ productData?.price }}</div>
        <div class="px-5">
          <li v-for="d, i in productData?.descriptions.split(/\r?\n/)" :key="i">{{ d.toUpperCase() }}</li>
        </div>

        <ProductSizeTable :variants="productData?.size_variants!" />
      </div>

      <div>
        <div>ANOTHER FROM THE COLLECTION</div>
        <div>
          <div>Product 1</div>
          <div>Product 1</div>
        </div>
      </div>
    </div>
  </div>
</template>

