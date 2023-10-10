<script setup lang="ts">
import { Product } from '@/types'

const { params } = useRoute()
const productId = params.productId as string
const productData = ref<Product>()

getSizeList()

const { data, error } = await useCustomFetch<Product>(`/v1/products/${productId}`)
if (error.value) {
  // todo: toast
  // todo: if product not found, raise 404 page
} else if (data.value) {
  productData.value = data.value
  getProductList({ collection_id: productData.value.collection_id })
}

// const startPictureIndex = ref(0)
// const nextPicture = () => {
//   if (startPictureIndex.value + 4 >= productData.value?.pictures.length!) return
//   startPictureIndex.value += 1
// }
// const prePicture = () => {
//   if (startPictureIndex.value <= 0) return
//   startPictureIndex.value -= 1
// }
// const showedSmallPictures = computed(() => {
//   return productData.value?.pictures.slice(startPictureIndex.value, startPictureIndex.value + 4)
// })

definePageMeta({
  layout: 'default-line-header',
})

useHead({
  title: productData.value ? productData.value.name.toUpperCase() + ' ' + productData.value.collection.name + '- YSV' : 'Product - YSV'
})
</script>


<template>
  <div class="mycontainer mx-auto pb-10">
    <NuxtLink to="/lookbook">
      <div class="my-5 flex items-center gap-2 text-gray-500">
        <UIcon name="i-iconamoon-arrow-top-left-1-light" class="text-2xl" /><span>LOOK ANOTHER COLLECTIONS</span>
      </div>
    </NuxtLink>

    <div class="xl:flex">
      <div v-if="productData" class="xl:flex-1">
        <div class="md:flex">
          <ProductPictures :pictures="productData.pictures" :product-data="productData" />
        </div>
        <div class="max-w-[412px] xl:hidden">
          <ProductSizeTable :variants="productData?.size_variants!" />
          <ProductAddToCart />
        </div>
      </div>
      <ProductOtherProducts class="xl:max-w-[200px]" />
    </div>
  </div>
</template>

