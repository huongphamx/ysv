<script setup lang="ts">
const productList = useProductList()
const randomProduct = computed(() => {
  const randomCount = 2 // get only 2 random collections
  const result = [];
  const arrayCopy = productList.value.slice(); // Create a copy of the original array to avoid modifying it

  for (let i = 0; i < randomCount; i++) {
    const randomIndex = Math.floor(Math.random() * arrayCopy.length);
    const randomItem = arrayCopy.splice(randomIndex, 1)[0]; // Remove and retrieve the item
    result.push(randomItem);
  }

  return result;
})

const collectionList = useCollectionList()
const randomCollection = computed(() => {
  const randomCount = 2 // get only 2 random collections
  const result = [];
  const arrayCopy = collectionList.value.slice(); // Create a copy of the original array to avoid modifying it

  for (let i = 0; i < randomCount; i++) {
    const randomIndex = Math.floor(Math.random() * arrayCopy.length);
    const randomItem = arrayCopy.splice(randomIndex, 1)[0]; // Remove and retrieve the item
    result.push(randomItem);
  }

  return result;
})
</script>


<template>
  <div>
    <template v-if="productList.length > 1">
      <div class="text-sm sm:text-base">ANOTHER FROM THE COLLECTION</div>
      <div class="flex gap-2 2xl:block">
        <div v-for="product in randomProduct" :key="product.id" class="my-2 relative hover:cursor-pointer"
          @click="$router.push(`/p/${product.id}`)">
          <img :src="product.preview_pic" alt="" class="preview-pic">
          <div class="absolute w-full bottom-0 left-2 font-['Italiana'] 2xl:text-xl text-white">{{
            product.name.toUpperCase() }}
          </div>
        </div>
      </div>
    </template>
    <template v-else>
      <div class="text-sm sm:text-base">ANOTHER COLLECTIONS</div>
      <div>
        <div v-for="collection in randomCollection" :key="collection.id" class="my-2 relative hover:cursor-pointer"
          @click="$router.push(`/catalog/${collection.id}`)">
          <img :src="collection.preview_pic" alt="" class="preview-pic">
          <div class="absolute w-full bottom-0 left-2 font-['Italiana'] 2xl:text-xl text-white">{{
            collection.name.toUpperCase() }}
          </div>
        </div>
      </div>
    </template>
  </div>
</template>


<style scoped>
.preview-pic {
  width: 140px;
  height: 175px;
  object-fit: cover;
}
</style>