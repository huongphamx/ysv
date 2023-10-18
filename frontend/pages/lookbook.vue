<script lang="ts" setup>
const config = useRuntimeConfig()
const cloudfrontDistributionDomain = config.public.cloudfrontDistributionDomain

const collectionList = useCollectionList()
await getCollectionList()

const isShowedHeaderLine = useIsShowedHeaderLine()
isShowedHeaderLine.value = false

useHead({
  title: 'Lookbook - YSV'
})
</script>


<template>
  <div class="mycontainer mx-auto">
    <div class="relative">
      <img :src="`${cloudfrontDistributionDomain}/img/lookbook-hero.webp`" alt="event hero"
        class="hero-image object-right" v-motion="slideVisibleOnceMotion" />
      <div class="hero-text in-image" v-motion="slideVisibleOnceBottomMotion">LOOK</div>
    </div>
    <div class="hero-text out-image text-book" v-motion="slideVisibleOnceBottomMotion">BOOK</div>
    <div class="lookbook-body">
      <div v-for="collection in collectionList" :key="collection.id" class="lookbook-collection">
        <template v-if="collection.lookbook_layout_code === 'two'">
          <LookbookTwoItems :collection="collection" />
        </template>
        <template v-else-if="collection.lookbook_layout_code === 'two_reversed'">
          <LookbookTwoItemsReverse :collection="collection" />
        </template>
        <template v-else-if="collection.lookbook_layout_code === 'three'">
          <LookbookThreeItems :collection="collection" />
        </template>
      </div>
    </div>
  </div>
</template>


<style scoped>
.lookbook-body {
  margin-top: 50px;
  margin-bottom: 50px;

  @media screen and (min-width: 480px) {
    margin-top: 80px;
    margin-bottom: 80px;
  }

  @media screen and (min-width: 768px) {
    margin-top: 100px;
    margin-bottom: 100px;
  }

  @media screen and (min-width: 1280px) {
    margin-top: 150px;
    margin-bottom: 150px;
  }
}

.lookbook-collection {
  margin-top: 50px;
  margin-bottom: 50px;


  @media screen and (min-width: 480px) {
    margin-top: 80px;
    margin-bottom: 80px;
  }

  /* @media screen and (min-width: 768px) {
    margin-top: 100px;
    margin-bottom: 100px;
  }

  @media screen and (min-width: 1280px) {
    margin-top: 150px;
    margin-bottom: 150px;
  } */
}
</style>