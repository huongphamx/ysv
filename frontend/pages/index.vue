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
        <div v-if="isHeroVideoPlaying" class="hero-text in-image" v-motion="slideVisibleOnceBottomMotion">
          YSV
        </div>
      </div>
    </div>
    <div class="mycontainer mx-auto">
      <div v-if="isHeroVideoPlaying" class="hero-text out-image" v-motion="slideVisibleOnceBottomMotion">BRAND</div>
      <div class="block-main-collection grid xl:grid-cols-2 gap-5">
        <div v-if="width >= 1280" v-motion="slideVisibleOnceLeftMotion"><img v-if="mainCollectionPics![0]"
            :src="mainCollectionPics![0]" alt="" class=" w-[628px] h-[962px] object-cover">
        </div>
        <div v-if="width < 1280" class="grid grid-cols-2 gap-3">
          <div>
            <img v-if="mainCollectionPics![1]" :src="mainCollectionPics![1]" alt="main prod 1" class="rect-image"
              v-motion="slideVisibleOnceLeftMotion">
            <div class="mt-4 text-small" v-motion="slideVisibleOnceBottomMotion">
              {{ mainCollection?.main_collection_description }}
              <div v-if="width >= 1280" v-motion="slideVisibleOnceBottomMotion">{{
                mainCollection?.main_collection_description_2 }}</div>
            </div>
          </div>
          <div v-motion="slideVisibleOnceRightMotion">
            <div class="text-medium">{{ mainCollection?.name }} COLLECTION
            </div>
            <div class="text-small my-5 xl:my-8">NEW OF 2023</div>
            <NuxtLink :to="`/catalog/${mainCollection?.id}`">
              <div class="view-all-btn">VIEW ALL
                <UIcon name="i-iconamoon-arrow-bottom-right-1-light" class="text-2xl" />
              </div>
            </NuxtLink>
            <img v-if="mainCollectionPics![2]" :src="mainCollectionPics![2]" alt="main prod 2" class="mt-8 rect-image">
          </div>
        </div>
        <div v-if="width >= 1280">
          <div class="flex gap-5">
            <img v-if="mainCollectionPics![1]" :src="mainCollectionPics![1]" alt="main prod 1"
              class="rect-image home-image" v-motion="slideVisibleOnceRightMotion">
            <div v-motion="slideVisibleOnceRightMotion">
              <div class="text-medium">{{ mainCollection?.name }} COLLECTION
              </div>
              <div class="text-small my-5 xl:my-8">NEW OF 2023</div>
              <NuxtLink :to="`/catalog/${mainCollection?.id}`">
                <div class="view-all-btn">VIEW ALL
                  <UIcon name="i-iconamoon-arrow-bottom-right-1-light" class="text-2xl" />
                </div>
              </NuxtLink>
            </div>
          </div>
          <div class="mt-[30px] flex gap-5">
            <div class="text-small" v-motion="slideVisibleOnceBottomMotion">
              {{ mainCollection?.main_collection_description }}
              <div v-if="width >= 1280" v-motion="slideVisibleOnceBottomMotion">{{
                mainCollection?.main_collection_description_2 }}</div>
            </div>
            <img v-if="mainCollectionPics![2]" :src="mainCollectionPics![2]" alt="main prod 2"
              class="rect-image home-image" v-motion="slideVisibleOnceRightMotion">
          </div>
        </div>
        <div v-if="width < 1280" class="text-small mt-2" v-motion="slideVisibleOnceBottomMotion">{{
          mainCollection?.main_collection_description_2 }}</div>
      </div>
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

.view-all-btn {
  width: 110px;
  height: 30px;
  border: 1px solid;
  display: flex;
  justify-content: center;
  align-items: center;

  &:hover {
    cursor: pointer;
    background-color: var(--black);
    color: white;
  }

  @media screen and (min-width: 480px) {
    width: 142px;
    height: 40px;
  }

  @media screen and (min-width: 768px) {
    width: 174px;
    height: 45px;
    border: 2px solid;
  }

  @media screen and (min-width: 1280px) {
    width: 196px;
    height: 50px;
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
