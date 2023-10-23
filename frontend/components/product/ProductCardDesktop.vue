<script lang="ts" setup>
import { Product } from '@/types'

const props = defineProps<{
  product: Product,
}>()

const showedBigPicture = ref(props.product.pictures[0].url)

</script>


<template>
  <div class="desktop-container">
    <div class="small-pic-container">
      <img v-for="image, i in product.pictures" :key="i" :src="image.url" alt="" class="small-pic"
        @click="showedBigPicture = image.url">
    </div>

    <div class="mx-5">
      <img :src="showedBigPicture" alt="big pic" class="big-pic">
      <ProductAddToCart class="my-5" />
    </div>

    <div class="description flex flex-col">
      <div class="flex flex-col gap-5 max-h-[414px] overflow-auto">
        <div>
          <div class="text-medium line-clamp-2">{{ product.collection.name }} collection</div>
        </div>
        <div class="product-color">Available colors: {{ product.name }}</div>
        <div class="product-price">${{ product.price }}</div>
        <div class="product-description">
          <ul class="list-disc">
            <li v-for="d, i in product.descriptions.split(/\r?\n/)" :key="i">{{ d.toUpperCase() }}</li>
          </ul>
        </div>
      </div>
      <ProductSizeTable :variants="product.size_variants" class="mt-auto" />
    </div>

    <ProductOtherProducts class="ml-auto" />
  </div>
</template>


<style scoped>
.desktop-container {
  display: flex;

  @media screen and (max-width: 1279px) {
    display: none;
  }
}

.small-pic-container {
  max-height: 600px;
  overflow: auto;
}

.small-pic {
  object-fit: cover;
  width: 88px;
  height: 134px;
  margin-bottom: 15px;
}

.big-pic {
  object-fit: contain;
  width: 411px;
  height: 618px;
  background-color: white;
}

.description {
  margin-right: 129px;
  height: 618px;
  width: 412px;
  /* display: flex;
  flex-direction: column; */
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
  margin-left: 20px;
}
</style>
