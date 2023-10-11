<script lang="ts" setup>
import { useWindowSize } from '@vueuse/core'
const { width } = useWindowSize()

const collectionList = useCollectionList()
await getCollectionList()

const isShowedHeaderLine = useIsShowedHeaderLine()
isShowedHeaderLine.value = false

useHead({
  title: 'Lookbook - YSV'
})
</script>


<template>
  <div class="lookbook-body mycontainer mx-auto mb-10">
    <div class="relative">
      <img src="/img/lookbook-hero.webp" alt="event hero" class="hero-image" />
      <div class="hero-text in-image">LOOK</div>
    </div>
    <div class="hero-text out-image">BOOK</div>
    <div v-for="collection in collectionList" :key="collection.id">
      <template v-if="collection.lookbook_layout_code === 'two' && width >= 768">
        <LookbookTwoItems :collection="collection" />
      </template>
      <template v-else-if="collection.lookbook_layout_code === 'two_reversed' && width >= 1280">
        <LookbookTwoItemsReverse :collection="collection" />
      </template>
      <template v-else-if="collection.lookbook_layout_code === 'three' && width >= 1280">
        <LookbookThreeItems :collection="collection" />
      </template>
      <template v-else>
        <LookbookMobile :collection="collection" />
      </template>
    </div>
  </div>
</template>


<style scoped>
.lookbook-body {
  margin-bottom: 50px;

  @media screen and (min-width: 480px) {
    margin-bottom: 80px;
  }

  @media screen and (min-width: 768px) {
    margin-bottom: 100px;
  }

  @media screen and (min-width: 1280px) {
    margin-bottom: 150px;
  }
}
</style>