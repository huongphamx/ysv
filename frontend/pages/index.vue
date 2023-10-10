<script lang="ts" setup>
const config = useRuntimeConfig()

const collectionList = useCollectionList()
await getCollectionList()
const mainCollection = collectionList.value.find(c => c.is_main_collection)
const showCollections = collectionList.value.filter(c => c.is_show_in_home)
const mainCollectionPics = computed(() => {
  return mainCollection?.main_collection_pics?.split('$')
})

const isShowedHeaderLine = useIsShowedHeaderLine()
isShowedHeaderLine.value = false

useHead({
  title: 'Home - YSV'
})
</script>


<template>
  <div>
    <div class="-mt-16 relative">
      <video autoplay muted loop class="hero-video">
        <source :src="`${config.public.s3BaseUrl}/hero.mp4`" type="video/mp4">
      </video>
      <div class="mycontainer mx-auto">
        <div class="hero-text in-image">YSV
        </div>
      </div>
    </div>
    <div class="mycontainer mx-auto">
      <div class="hero-text out-image">BRAND</div>
      <div class="mt-10 md:mt-20 xl:mt-32 grid xl:grid-cols-2 gap-3">
        <div class="hidden xl:block"><img :src="mainCollectionPics![0]" alt=""></div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <img :src="mainCollectionPics![1]" alt="main prod 1" class="rect-image">
            <div class="mt-4 text-small">
              {{ mainCollection?.main_collection_description }}
              <div class="hidden xl:block">{{ mainCollection?.main_collection_description_2 }}</div>
            </div>
          </div>
          <div>
            <div class="text-medium">{{ mainCollection?.name }} COLLECTION
            </div>
            <div class="text-small my-5">NEW OF 2023</div>
            <UButton :to="`/catalog/${mainCollection?.id}`" label="VIEW ALL" variant="outline" color="black"
              :ui="{ rounded: '', gap: { sm: 'gap-x-0' } }">
              <template #trailing>
                <UIcon name="i-iconamoon-arrow-bottom-right-1-light" class="text-2xl" />
              </template>
            </UButton>
            <img :src="mainCollectionPics![2]" alt="main prod 2" class="mt-8 rect-image">
          </div>
        </div>
        <div class="text-small mt-2 xl:hidden">{{ mainCollection?.main_collection_description_2 }}</div>
      </div>
      <div class="mt-12">
        <div class="collections-text">COLLECTIONS</div>
        <div class="my-3">
          <HomeCollectionsMobile :show-collections="showCollections" />
          <HomeCollectionsDesktop :show-collections="showCollections" />
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped>
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

.collections-text {
  font-family: 'Italiana';
  font-size: 40px;
  line-height: 1;

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
    margin-bottom: 20px;
  }
}
</style>
