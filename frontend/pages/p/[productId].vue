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
const isShowedHeaderLine = useIsShowedHeaderLine()
isShowedHeaderLine.value = true

useHead({
  title: productData.value ? productData.value.name.toUpperCase() + ' ' + productData.value.collection.name + '- YSV' : 'Product - YSV'
})
</script>


<template>
  <div class="product-body mycontainer mx-auto">
    <div class="my-10 w-fit group" @click="$router.push('/lookbook')">
      <div class="look-another-body">
        <UIcon name="i-iconamoon-arrow-top-left-1-light" class="text-2xl" /><span>LOOK ANOTHER COLLECTIONS</span>
      </div>
      <div class="-mt-0.5 ml-1 h-[1px] bg-[var(--gray)] hidden group-hover:block"></div>
    </div>

    <ProductCardMobile :product="productData!" />
    <ProductCardTablet :product="productData!" />
    <ProductCardDesktop :product="productData!" />
  </div>
</template>


<style scoped>
.look-another-body {
  color: var(--gray);
  display: none;

  @media screen and (min-width: 1280px) {
    width: fit-content;
    display: flex;
    align-items: center;
    column-gap: 0.5rem;

    &:hover {
      cursor: pointer;
    }
  }
}

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
