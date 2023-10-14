<script lang="ts" setup>
import { Product } from '@/types'

const props = defineProps<{
  product: Product,
}>()

const showedBigPicture = ref(props.product.pictures[0].url)

</script>


<template>
  <div class="flex">
    <div class="small-pic-container">
      <img v-for="image, i in product.pictures" :key="i" :src="image.url" alt="" class="small-pic"
        @click="showedBigPicture = image.url">
    </div>

    <div class="mx-5">
      <img :src="showedBigPicture" alt="big pic" class="big-pic">
      <ProductAddToCart class="my-5" />
    </div>

    <div class="description">
      <div class="text-medium">{{ product.collection.name }} collection</div>
      <div class="product-color">Available colors: {{ product.name }}</div>
      <div class="product-price">${{ product.price }}</div>
      <div class="product-description">
        <li v-for="d, i in product.descriptions.split(/\r?\n/)" :key="i">{{ d.toUpperCase() }}</li>
      </div>
      <ProductSizeTable :variants="product.size_variants" />
    </div>

    <ProductOtherProducts />
  </div>
</template>


<style scoped>
.small-pic-container {
  max-height: 600px;
  overflow: auto;
}

.small-pic {
  width: 88px;
  height: 134px;
  margin-bottom: 15px;
}

.big-pic {
  width: 411px;
  height: 618px;
}

.description {
  margin-right: 129px;
  width: 412px;
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.product-color {
  text-transform: uppercase;
  color: #888;
}

.product-price {
  font-size: 36px;
}

.product-description {
  color: #888;
  margin-left: 15px;
}
</style>
