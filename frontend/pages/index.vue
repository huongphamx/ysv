<script lang="ts" setup>
import { useWindowSize } from '@vueuse/core'

const { width } = useWindowSize()
const config = useRuntimeConfig()

const isHeroVideoPlaying = ref(false)
const collectionList = useCollectionList()
await getCollectionList()
const mainCollection = computed(() => {
  return collectionList.value.find(c => c.is_main_collection)
})
const showCollections = computed(() => {
  return collectionList.value.filter(c => c.is_show_in_home)
})
const mainCollectionPics = computed(() => {
  return mainCollection.value?.main_collection_pics?.split('$')
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
      <video autoplay preload="auto" playsinline muted loop class="hero-video" @play="isHeroVideoPlaying = true">
        <source :src="`${config.public.s3BaseUrl}/hero.mp4`" type="video/mp4">
      </video>
      <div class="mycontainer mx-auto">
        <div v-if="isHeroVideoPlaying" class="hero-text in-image" v-motion="{
          initial: { opacity: 0, y: 50 },
          enter: { opacity: 1, y: 0, transition: { duration: 800 } },
          delay: 500
        }">
          YSV
        </div>
      </div>
    </div>
    <div class="mycontainer mx-auto">
      <div v-if="isHeroVideoPlaying" class="hero-text out-image" v-motion="{
        initial: { opacity: 0, y: 50 },
        enter: { opacity: 1, y: 0, transition: { duration: 800 } },
        delay: 500
      }">BRAND</div>
      <template v-if="width < 768">
        <HomeMainCollectionMobile :main-collection="mainCollection" />
      </template>
      <template v-else-if="width >= 768 && width < 1280">
        <HomeMainCollectionTablet :main-collection="mainCollection" />
      </template>
      <template v-else>
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
    margin-bottom: 40px;
  }

  @media screen and (min-width: 640px) {
    font-size: 100px;
    margin-bottom: 20px;
  }

  @media screen and (min-width: 1280px) {
    font-size: 200px;
    margin-top: 150px;
    margin-bottom: 50px;
  }
}
</style>
