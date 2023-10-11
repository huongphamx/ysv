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
      <div class="block-main-collection grid xl:grid-cols-2 gap-5">
        <div class="hidden xl:block w-[628px] h-[962px]"><img :src="mainCollectionPics![0]" alt=""></div>
        <div class="grid grid-cols-2 gap-3 xl:hidden">
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
            <div class="text-small my-5 xl:my-8">NEW OF 2023</div>
            <NuxtLink :to="`/catalog/${mainCollection?.id}`">
              <div class="view-all-btn">VIEW ALL
                <UIcon name="i-iconamoon-arrow-bottom-right-1-light" class="text-2xl" />
              </div>
            </NuxtLink>
            <img :src="mainCollectionPics![2]" alt="main prod 2" class="mt-8 rect-image">
          </div>
        </div>
        <div class="hidden xl:block">
          <div class="flex gap-5">
            <img :src="mainCollectionPics![1]" alt="main prod 1" class="rect-image home-image">
            <div>
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
            <div class="text-small">
              {{ mainCollection?.main_collection_description }}
              <div class="hidden xl:block">{{ mainCollection?.main_collection_description_2 }}</div>
            </div>
            <img :src="mainCollectionPics![2]" alt="main prod 2" class="rect-image home-image">
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
