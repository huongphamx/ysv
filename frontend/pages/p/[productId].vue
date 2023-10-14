<script setup lang="ts">
import { useWindowSize } from '@vueuse/core'
import { Product } from '@/types'

const { params } = useRoute()
const productId = params.productId as string
const productData = ref<Product>()

const { width } = useWindowSize()

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
const isShowedHeaderLine = useIsShowedHeaderLine()
isShowedHeaderLine.value = true

useHead({
  title: productData.value ? productData.value.name.toUpperCase() + ' ' + productData.value.collection.name + '- YSV' : 'Product - YSV'
})
</script>


<template>
  <div class="product-body mycontainer mx-auto">
    <NuxtLink to="/lookbook">
      <div class="btn-look-another">
        <UIcon name="i-iconamoon-arrow-top-left-1-light" class="text-2xl" /><span class="text-sm md:text-base">LOOK
          ANOTHER COLLECTIONS</span>
      </div>
    </NuxtLink>

    <ProductCardMobile v-if="width < 768" :product="productData!" />
    <ProductCardTablet v-if="768 <= width && width < 1280" :product="productData!" />
    <ProductCardDesktop v-if="width >= 1280" :product="productData!" />
  </div>
</template>


<style scoped>
.product-body {
  margin-bottom: 50px;

  @media screen and (min-width: 768px) {
    margin-bottom: 80px;
  }

  @media screen and (min-width: 1280px) {
    margin-bottom: 150px;
  }
}

.btn-look-another {
  display: flex;
  align-items: center;
  gap: 10px;
  color: #888;
  width: 300px;
  margin: 20px 0;

  @media screen and (min-width: 768px) {
    margin: 30px 0;
  }

  @media screen and (min-width: 1280px) {
    margin: 50px 0;
  }
}
</style>
