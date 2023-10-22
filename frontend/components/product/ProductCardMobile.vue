<script lang="ts" setup>
import { Product } from '@/types'

const props = defineProps<{
  product: Product,
}>()

const showedBigPicture = ref(props.product.pictures[0].url)

</script>


<template>
  <div class="mobile-container">
    <div class="pic-container">
      <img :src="showedBigPicture" alt="big pic" class="big-pic">
      <div class="small-pic-container">
        <img v-for="image, i in product.pictures" :key="i" :src="image.url" alt="" class="small-pic"
          @click="showedBigPicture = image.url">
      </div>
    </div>

    <div class="description">
      <div class="text-medium">{{ product.collection.name }} collection</div>
      <div class="product-color">Available colors: {{ product.name }}</div>
      <div class="product-price">${{ product.price }}</div>
      <div class="product-description">
        <ul class="list-disc">
          <li v-for="d, i in product.descriptions.split(/\r?\n/)" :key="i">{{ d.toUpperCase() }}</li>
        </ul>
      </div>
      <ProductSizeTable :variants="product.size_variants" />
    </div>
    <ProductAddToCart class="my-[30px]" />
    <ProductOtherProducts />
  </div>
</template>


<style scoped>
.mobile-container {
  @media screen and (min-width: 768px) {
    display: none;
  }
}

.pic-container {
  display: flex;
  margin-bottom: 15px;
}

.big-pic {
  margin-right: 20px;
  width: 220px;
  height: 330px;
  object-fit: contain;
  background-color: white;

  @media screen and (min-width: 480px) {
    width: 310px;
    height: 460px;
  }
}

.small-pic-container {
  max-height: 330px;
  overflow: auto;

  @media screen and (min-width: 480px) {
    max-height: 400px;
  }
}

.small-pic {
  margin-bottom: 5px;
  width: 60px;
  height: 75px;
  object-fit: cover;

  @media screen and (min-width: 480px) {
    width: 70px;
    height: 88px;
  }
}

.description {
  width: 220px;
  display: flex;
  flex-direction: column;
  gap: 15px;

  @media screen and (min-width: 480px) {
    width: 310px;
  }
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
