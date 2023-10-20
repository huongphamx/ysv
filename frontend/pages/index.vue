<script lang="ts" setup>
const config = useRuntimeConfig()
const cloudfrontDistributionDomain = config.public.cloudfrontDistributionDomain

const collectionList = useCollectionList()
await getCollectionList()
const mainCollection = computed(() => {
  return collectionList.value.find(c => c.is_main_collection)
})
const showCollections = computed(() => {
  return collectionList.value.filter(c => c.is_show_in_home)
})

const isShowedHeaderLine = useIsShowedHeaderLine()
isShowedHeaderLine.value = false

useHead({
  title: 'Home - YSV'
})
</script>


<template>
  <div class="home-body">
    <div class="-mt-16 relative">
      <video autoplay preload="auto" playsinline muted loop class="hero-video">
        <source :src="`${cloudfrontDistributionDomain}/hero.mp4`" type="video/mp4">
      </video>
      <div class="mycontainer mx-auto">
        <div class="hero-text in-image" v-motion="slideVisibleOnceBottomMotion">
          YSV
        </div>
      </div>
    </div>
    <div class="mycontainer mx-auto">
      <div class="hero-text out-image" v-motion="slideVisibleOnceBottomMotion">BRAND</div>
      <template v-if="mainCollection">
        <HomeMainCollectionMobile :main-collection="mainCollection" />
        <HomeMainCollectionTablet :main-collection="mainCollection" />
        <HomeMainCollectionDesktop :main-collection="mainCollection" />
      </template>
      <div class="mt-12">
        <div class="collections-text" v-motion="slideVisibleOnceBottomMotion">COLLECTIONS</div>
        <div class="my-3">
          <HomeCollectionsMobile :show-collections="showCollections" />
          <HomeCollectionsDesktop :show-collections="showCollections" />
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped>
.home-body {
  margin-bottom: 50px;

  @media screen and (min-width: 480px) {
    margin-bottom: 80px;
  }

  @media screen and (min-width: 480px) {
    margin-bottom: 80px;
  }

  @media screen and (min-width: 1280px) {
    margin-bottom: 150px;
  }
}

.hero-video {
  width: 100%;
  height: 550px;
  object-fit: cover;

  @media screen and (min-width: 480px) {
    height: 615px;
  }

  @media screen and (min-width: 1280px) {
    height: 1180px;
  }
}

.block-main-collection {
  margin-top: 50px;

  @media screen and (min-width: 480px) {
    margin-top: 80px;
  }

  @media screen and (min-width: 768px) {
    margin-top: 100px;
  }

  @media screen and (min-width: 1280px) {
    margin-top: 150px;
  }
}

.collections-text {
  font-family: 'Italiana';
  font-size: 40px;
  font-weight: 400;
  line-height: normal;

  @media screen and (min-width: 480px) {
    font-size: 60px;
    margin-top: 60px;
    margin-bottom: 20px;
  }

  @media screen and (min-width: 640px) {
    font-size: 100px;
    margin-bottom: 20px;
  }

  @media screen and (min-width: 1280px) {
    font-size: 200px;
    margin-top: 150px;
  }
}
</style>
