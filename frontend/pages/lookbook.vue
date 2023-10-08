<script lang="ts" setup>

const collectionList = useCollectionList()

useHead({
  title: 'Lookbook - YSV'
})
</script>


<template>
  <div class="mycontainer mx-auto mb-10">
    <div class="relative">
      <img src="/img/lookbook-hero.webp" alt="event hero" class="img-hero" />
      <div class="absolute bottom-0 text-6xl text-white font-['Italiana']">LOOK</div>
    </div>
    <div class="pl-32 text-6xl font-['Italiana']">BOOK</div>
  </div>
</template>

