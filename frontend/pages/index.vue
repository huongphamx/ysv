<script lang="ts" setup>
const config = useRuntimeConfig()

const collectionList = useCollectionList()
await getCollectionList()
const mainCollection = collectionList.value.find(c => c.is_main_collection)
const showCollections = collectionList.value.filter(c => c.is_show_in_home)
const mainCollectionPics = computed(() => {
  return mainCollection?.main_collection_pics?.split('$')
})
useHead({
  title: 'Home - YSV'
})
</script>


<template>
  <div class="-mt-16 relative">
    <!-- <video autoplay class="hero-video" poster="/img/poster.webp"> -->
    <video autoplay class="hero-video">
      <source :src="`${config.public.s3BaseUrl}/hero.mp4`" type="video/mp4">
    </video>
    <div class="mycontainer mx-auto">
      <div class="hero-text in-image">YSV
      </div>
    </div>
  </div>
  <div class="mycontainer mx-auto">
    <div class="hero-text out-image">BRAND</div>

    <div class="mt-10 mb-5 grid 2xl:grid-cols-2 gap-5">
      <div class="hidden 2xl:block"><img :src="mainCollectionPics![0]" alt=""></div>

      <div class="grid grid-cols-2 gap-3">
        <div>
          <img :src="mainCollectionPics![1]" alt="main prod 1" class="rect-img">
          <div class="text-sm sm:text-base md:text-lg">{{ mainCollection?.main_collection_description?.toUpperCase() }}
          </div>
        </div>

        <div>
          <div class="text-xl sm:text-2xl md:text-3xl lg:text-4xl font-['Italiana']">{{ mainCollection?.name }} COLLECTION
          </div>
          <div class="text-sm sm:text-base my-5">NEW OF 2023</div>
          <UButton :to="`/catalog/${mainCollection?.id}`" label="VIEW ALL" trailing-icon="i-ph-arrow-down-right"
            variant="outline" color="gray" :ui="{ rounded: '' }" />
          <img :src="mainCollectionPics![2]" alt="main prod 2" class="mt-8 rect-img">
        </div>
      </div>
    </div>

    <div>
      <div class="text-[40px] sm:text-6xl md:text-8xl xl:text-9xl text-center font-['Italiana']">COLLECTIONS</div>
      <div class="my-5">
        <div class="2xl:hidden">
          <div class="grid grid-cols-2 gap-4 justify-items-center">
            <CollectionCard :collection="showCollections[0]" />
            <CollectionCard :collection="showCollections[1]" />
            <CollectionCard :collection="showCollections[2]" />
            <CollectionCard :collection="showCollections[3]" />
          </div>
          <div class="my-4 mx-auto"><img src="/img/home-collection-square-1.webp" alt="" class="square-img"></div>
          <div class="grid grid-cols-2 gap-4 justify-items-center mb-4">
            <CollectionCard :collection="showCollections[4]" />
            <CollectionCard :collection="showCollections[5]" />
          </div>
          <div>
            <UButton block size="xl" label="LOOKBOOK" trailing-icon="i-ph-arrow-down-right" to="/lookbook"
              variant="outline" color="gray" :ui="{ rounded: '' }" />
          </div>
        </div>

        <div class="hidden 2xl:block">
          <div class="grid grid-cols-2 gap-3">
            <div>
              <div class="mb-6 grid grid-cols-2 gap-3">
                <CollectionCard :collection="showCollections[0]" />
                <CollectionCard :collection="showCollections[1]" />
              </div>
              <img src="/img/home-collection-square-1.webp" alt="" class="square-img">
            </div>
            <div>
              <img src="/img/home-collection-square-2.webp" alt="" class="square-img">
              <div class="my-6 grid grid-cols-2 gap-3">
                <CollectionCard :collection="showCollections[2]" />
                <CollectionCard :collection="showCollections[3]" />
              </div>
            </div>
          </div>
          <div class="grid grid-cols-2 gap-3">
            <div>
              <div class="mb-6 grid grid-cols-2 gap-3">
                <CollectionCard :collection="showCollections[4]" />
                <CollectionCard :collection="showCollections[5]" />
              </div>
              <img src="/img/home-collection-square-3.webp" alt="" class="square-img">
            </div>
            <div>
              <div class="mb-6 grid grid-cols-2 gap-3">
                <CollectionCard :collection="showCollections[6]" />
                <CollectionCard :collection="showCollections[7]" />
              </div>
              <div class="mb-6 grid grid-cols-2 gap-3">
                <CollectionCard :collection="showCollections[8]" />
                <CollectionCard :collection="showCollections[9]" />
              </div>
              <UButton block size="xl" label="LOOKBOOK" trailing-icon="i-ph-arrow-down-right" to="/lookbook"
                variant="outline" color="gray" :ui="{ rounded: '', base: 'h-[145px]' }" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped lang="postcss">
.hero-video {
  width: 100%;
  height: 550px;
  object-fit: cover;
}

@media screen and (min-width: 640px) {
  .hero-video {
    height: 615px;
  }
}

@media screen and (min-width: 1280px) {
  .hero-video {
    height: 800px;
  }
}

@media screen and (min-width: 1536px) {
  .hero-video {
    height: 1000px;
  }
}
</style>
