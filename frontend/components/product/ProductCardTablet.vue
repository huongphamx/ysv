<script lang="ts" setup>
import { Product } from '@/types'

const props = defineProps<{
  product: Product,
}>()

const showedBigPicture = ref(props.product.pictures[0].url)

</script>


<template>
  <div class="tablet-container">
    <div class="small-pic-container">
      <img v-for="image, i in product.pictures" :key="i" :src="image.url" alt="" class="small-pic"
        @click="showedBigPicture = image.url">
    </div>
    <div class="flex">
      <img :src="showedBigPicture" alt="big pic" class="big-pic">
      <div class="description">
        <div class="text-medium">{{ product.collection.name }} collection</div>
        <div class="product-color">Available colors: {{ product.name }}</div>
        <div class="product-price">${{ product.price }}</div>
        <div class="product-description">
          <ul class="list-disc">
            <li v-for="d, i in product.descriptions.split(/\r?\n/)" :key="i">{{ d.toUpperCase() }}</li>
          </ul>
        </div>
      </div>
    </div>
    <ProductSizeTable :variants="product.size_variants" class="my-[20px]" />
    <ProductAddToCart class="mb-[50px]" />
    <ProductOtherProducts />
  </div>
</template>


<style scoped>
.tablet-container {

  @media screen and (max-width: 767px),
  (min-width: 1280px) {
    display: none;
  }
}

.small-pic-container {
  margin-bottom: 20px;
  max-width: 330px;
  overflow: auto;
}

.small-pic {
  margin-right: 10px;
  width: 60px;
  height: 92px;
  object-fit: cover;
}

.big-pic {
  margin-right: 20px;
  width: 380px;
  height: 570px;
  object-fit: cover;
}

.description {
  width: 220px;
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.product-color {
  color: #888;
  font-size: 12px;
  line-height: normal;
  text-transform: uppercase;

  @media screen and (min-width: 480px) {
    font-size: 14px;
  }
}

.product-price {
  font-size: 20px;
  line-height: normal;

  @media screen and (min-width: 480px) {
    font-size: 26px;
  }
}

.product-description {
  color: #888;
  margin-left: 20px;
}
</style>
