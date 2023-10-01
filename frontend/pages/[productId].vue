<script setup lang="ts">
import { Product } from '@/types'

const { params } = useRoute()
const productId = params.productId as string

const productDetail = ref<Product>()
const { data, error } = await useCustomFetch<Product>(`/v1/products/${productId}`)
if (error.value) {
  // todo: toast
} else if (data.value) {
  productDetail.value = data.value
}
const showedBigPicture = ref(productDetail.value?.pictures[0].url)

const startPictureIndex = ref(0)
const nextPicture = () => {
  if (startPictureIndex.value + 4 >= productDetail.value?.pictures.length!) return
  startPictureIndex.value += 1
}
const prePicture = () => {
  if (startPictureIndex.value <= 0) return
  startPictureIndex.value -= 1
}
const showedSmallPictures = computed(() => {
  return productDetail.value?.pictures.slice(startPictureIndex.value, startPictureIndex.value + 4)
})

const selectedSize = ref('xs') // todo: replace with actual size

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
        <div class="my-4 flex gap-5">
          <UButton label="ADD TO CART" trailing-icon="i-ph-arrow-down-right" color="gray"
            :ui="{ rounded: '', padding: { 'sm': 'px-16' } }" />
          <UButton icon="i-ph-heart" color="gray" :ui="{ rounded: '' }" />
        </div>
        <div class="underline text-gray-500"><a href="https://whatsapp.com" target="_blank">CONTACT VIA WHATSAPP</a></div>
      </div>

      <div class="max-w-[412px]">
        <div class="text-4xl font-['Italiana']">
          {{ productDetail?.collection.name.toUpperCase() }}
        </div>
        <div class="my-5 text-gray-500">AVAILABLE COLORS: {{ productDetail?.name.toUpperCase() }}</div>
        <div class="my-8 text-4xl">${{ productDetail?.price }}</div>
        <div class="px-5">
          <li v-for="d, i in productDetail?.descriptions.split(/\r?\n/)" :key="i">{{ d.toUpperCase() }}</li>
        </div>

        <!-- <div class="my-5 grid grid-cols-3 w-fit">
          <div class="w-[100px] h-[70px] border flex justify-center items-center">XS</div>
          <div class="w-[100px] h-[70px] border flex justify-center items-center">S</div>
          <div class="w-[100px] h-[70px] border flex justify-center items-center">M</div>
          <div class="w-[100px] h-[70px] border flex justify-center items-center">L</div>
        </div> -->
        <div>
          <table class="border-collapse border">
            <tr>
              <td class="w-[100px] h-[70px] border-2 text-center hover:cursor-pointer hover:bg-gray-500"
                @click="selectedSize = 'xs'" :class="{ 'bg-gray-500': selectedSize === 'xs' }">XS
              </td>
              <td class="w-[100px] h-[70px] border-2 text-center hover:cursor-pointer hover:bg-gray-500">S</td>
              <td class="w-[100px] h-[70px] border-2 text-center hover:cursor-pointer hover:bg-gray-500">M</td>
            </tr>
            <tr>
              <td class="w-[100px] h-[70px] border-2 text-center hover:cursor-pointer hover:bg-gray-500">L</td>
              <td class="w-[100px] h-[70px] border-2 text-center hover:cursor-pointer hover:bg-gray-500">XL</td>
              <td class="w-[100px] h-[70px] border-2 text-center hover:cursor-pointer hover:bg-gray-500">XXL</td>
            </tr>
          </table>
        </div>
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

