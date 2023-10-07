<script lang="ts" setup>
const collectionList = useCollectionList()

useHead({
  title: 'Home - YSV'
})
</script>


<template>
  <div class="-mt-16 relative">
    <video controls class="hero-video">
      <source src="https://ysv-dev.s3.ap-northeast-1.amazonaws.com/hero.mp4" type="video/mp4">
    </video>
    <div class="mycontainer mx-auto">
      <div class="absolute bottom-0 text-6xl sm:text-8xl md:text-9xl 2xl:text-[200px] text-white font-['Italiana']">YSV
      </div>
    </div>
  </div>
  <div class="mycontainer mx-auto">
    <div class="text-6xl sm:text-8xl md:text-9xl 2xl:text-[200px] pl-16 md:pl-32 font-['Italiana']">BRAND</div>

    <div class="mt-10 mb-5 grid 2xl:grid-cols-2 gap-5">
      <div class="hidden 2xl:block"><img src="/img/main-prod-01.webp" alt=""></div>

      <div class="grid grid-cols-2 gap-3">
        <div>
          <img src="/img/main-prod-02.webp" alt="main prod 1" class="rect-img">
          <div class="text-sm sm:text-base md:text-lg">THE FLOWING SILHOUETTE AND ETHEREAL DESIGN MAKE IT THE PERFECT
            CHOICE FOR ANY
            SPECIAL
            OCCASION.</div>
          <div class="hidden 2xl:block">WHETHER YOU'RE ATTENDING A GLAMOROUS EVENT OR SIMPLY
            WANT TO FEEL
            LIKE A
            PRINCESS, THIS
            DRESS
            WILL MAKE YOU FEEL LIKE YOU'RE WALKING ON AIR. GET READY TO DAZZLE AND MAKE A STATEMENT.</div>
        </div>

        <div>
          <div class="text-xl sm:text-2xl md:text-3xl lg:text-4xl font-['Italiana']">EXCLUSIVE SIHOUETTE COLLECTION</div>
          <div class="text-sm sm:text-base my-5">NEW OF 2023</div>
          <UButton label="VIEW ALL" trailing-icon="i-ph-arrow-down-right" variant="outline" color="gray"
            :ui="{ rounded: '' }" />
          <img src="/img/main-prod-03.webp" alt="main prod 2" class="mt-8 rect-img">
        </div>
      </div>
    </div>

    <div class="mb-10 text-sm sm:text-base md:text-lg 2xl:hidden">WHETHER YOU'RE ATTENDING A GLAMOROUS EVENT OR SIMPLY
      WANT TO FEEL
      LIKE A
      PRINCESS, THIS
      DRESS
      WILL MAKE YOU FEEL LIKE YOU'RE WALKING ON AIR. GET READY TO DAZZLE AND MAKE A STATEMENT.</div>

    <div>
      <div class="text-[40px] sm:text-6xl md:text-8xl xl:text-9xl text-center font-['Italiana']">COLLECTIONS</div>
      <div class="my-5">
        <div class="2xl:hidden">
          <div class="grid grid-cols-2 gap-4 justify-items-center">
            <CollectionCard :collection="collectionList[0]" />
            <CollectionCard :collection="collectionList[1]" />
            <CollectionCard :collection="collectionList[2]" />
            <CollectionCard :collection="collectionList[3]" />
          </div>
          <div class="my-4 mx-auto"><img src="/img/home-collection-square-1.webp" alt="" class="square-img"></div>
          <div class="grid grid-cols-2 gap-4 justify-items-center mb-4">
            <CollectionCard :collection="collectionList[4]" />
            <CollectionCard :collection="collectionList[5]" />
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
                <CollectionCard :collection="collectionList[0]" />
                <CollectionCard :collection="collectionList[1]" />
              </div>
              <img src="/img/home-collection-square-1.webp" alt="" class="square-img">
            </div>
            <div>
              <img src="/img/home-collection-square-2.webp" alt="" class="square-img">
              <div class="my-6 grid grid-cols-2 gap-3">
                <CollectionCard :collection="collectionList[2]" />
                <CollectionCard :collection="collectionList[3]" />
              </div>
            </div>
          </div>
          <div class="grid grid-cols-2 gap-3">
            <div>
              <div class="mb-6 grid grid-cols-2 gap-3">
                <CollectionCard :collection="collectionList[4]" />
                <CollectionCard :collection="collectionList[5]" />
              </div>
              <img src="/img/home-collection-square-3.webp" alt="" class="square-img">
            </div>
            <div>
              <div class="mb-6 grid grid-cols-2 gap-3">
                <CollectionCard :collection="collectionList[6]" />
                <CollectionCard :collection="collectionList[7]" />
              </div>
              <div class="mb-6 grid grid-cols-2 gap-3">
                <CollectionCard :collection="collectionList[8]" />
                <CollectionCard :collection="collectionList[9]" />
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


<style scoped>
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
