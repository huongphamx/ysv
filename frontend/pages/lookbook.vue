<script lang="ts" setup>

const collectionList = useCollectionList()
await getCollectionList()

useHead({
  title: 'Lookbook - YSV'
})
</script>


<template>
  <div class="mycontainer mx-auto mb-10">
    <div class="relative">
      <img src="/img/lookbook-hero.webp" alt="event hero" class="img-hero" />
      <div class="hero-text in-image">LOOK</div>
    </div>
    <div class="hero-text out-image">BOOK</div>
    <div v-for="collection in collectionList" :key="collection.id">
      <LookbookCollection :collection="collection" />
    </div>
  </div>
</template>

