<script setup lang="ts">
import { ProductPicture, Product } from '@/types'

const props = defineProps<{
  pictures: ProductPicture[],
  productData: Product,
}>()

const showedBigPicture = ref(props.pictures[0].url)
</script>


<template>
  <div class="mb-2 flex md:flex-col-reverse xl:flex-row-reverse">
    <div class="md:flex">
      <div>
        <img :src="showedBigPicture" alt="Product proview picture" class="img-preview">
        <ProductAddToCart class="hidden 2xl:block" />
      </div>
      <div class="mt-5 px-4 description">
        <div class="text-xl sm:text-2xl xl:text-3xl font-['Italiana']">
          {{ productData?.collection.name.toUpperCase() }} COLLECTION
        </div>
        <div class="my-5 text-sm xl:text-base text-gray-500">AVAILABLE COLORS: {{ productData?.name.toUpperCase() }}</div>
        <div class="my-4 text-xl sm:text-2xl xl:text-3xl">${{ productData?.price }}</div>
        <div class="px-5 text-sm xl:text-base">
          <li v-for="d, i in productData?.descriptions.split(/\r?\n/)" :key="i">{{ d.toUpperCase() }}</li>
        </div>
        <ProductSizeTable :variants="productData?.size_variants!" class="hidden 2xl:block" />
      </div>
    </div>
    <div
      class="ml-2 flex flex-col md:flex-row md:overflow-x-auto md:ml-0 md:mb-2 xl:flex-col xl:mr-2 gap-2 img-list overflow-auto">
      <div v-for="image in pictures!" :key="image.id" @click="showedBigPicture = image.url" class="whitespace-nowrap"
        :class="{ 'border border-gray-500': showedBigPicture === image.url }">
        <img :src="image.url" alt="Product pic" class="img-small">
      </div>
    </div>
  </div>
</template>


<style scoped>
.img-preview {
  width: 220px;
  height: 330px;
  object-fit: cover;
}

.description {
  max-width: 220px;
}

.img-list {
  max-height: 330px;
  overflow: auto;
}

.img-small {
  width: 65px;
  height: 75px;
  object-fit: cover;
}

@media screen and (min-width: 480px) {
  .img-preview {
    width: 310px;
    height: 460px;
  }

  .description {
    max-width: 310px;
  }

  .img-list {
    max-height: 460px;
  }

  .img-small {
    width: 70px;
    height: 88px;
  }

}

@media screen and (min-width: 1536px) {
  .img-preview {
    width: 380px;
    height: 570px;
  }

  .description {
    max-width: 510px;
  }
}

/* @media screen and (min-width: 150px) {
  .img-preview {
    width: 380px;
    height: 570px;
  }

  .description {
    max-width: 510px;
  }
} */
</style>