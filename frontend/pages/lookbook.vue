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
      <div class="absolute bottom-0 text-6xl md:text-[100px] text-white font-['Italiana']">LOOK</div>
    </div>
    <div class="pl-32 text-6xl md:text-[100px] font-['Italiana']">BOOK</div>
    <div v-for="collection in collectionList" :key="collection.id">
      <LookbookCollection :collection="collection" />
    </div>
  </div>
</template>

