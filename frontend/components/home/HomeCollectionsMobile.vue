<script lang="ts" setup>
import { Collection } from '@/types'

const props = defineProps<{
  showCollections: Collection[]
}>()

const config = useRuntimeConfig()
const cloudfrontDistributionDomain = config.public.cloudfrontDistributionDomain

const collection1 = computed(() => {
  return props.showCollections.find(c => c.home_position === 1)
})
const collection2 = computed(() => {
  return props.showCollections.find(c => c.home_position === 2)
})
const collection3 = computed(() => {
  return props.showCollections.find(c => c.home_position === 3)
})
const collection4 = computed(() => {
  return props.showCollections.find(c => c.home_position === 4)
})
const collection5 = computed(() => {
  return props.showCollections.find(c => c.home_position === 5)
})
const collection6 = computed(() => {
  return props.showCollections.find(c => c.home_position === 6)
})
</script>


<template>
  <div class="xl:hidden">
    <div class="grid grid-cols-2 gap-5 justify-items-center">
      <CollectionCard v-if="collection1" :collection="collection1" />
      <CollectionCard v-if="collection2" :collection="collection2" />
      <CollectionCard v-if="collection3" :collection="collection3" />
      <CollectionCard v-if="collection4" :collection="collection4" />
    </div>
    <div class="my-5 mx-auto" v-motion="slideVisibleOnceBottomMotion"><img
        :src="`${cloudfrontDistributionDomain}/img/home-collection-square-1.webp`" alt="" class="square-img"></div>
    <div class="grid grid-cols-2 gap-5 justify-items-center mb-5">
      <CollectionCard v-if="collection5" :collection="collection5" />
      <CollectionCard v-if="collection6" :collection="collection6" />
    </div>
    <div>
      <NuxtLink to="/lookbook">
        <div class="lookbook-btn">LOOKBOOK
          <UIcon name="i-iconamoon-arrow-bottom-right-1-light" class="text-2xl" />
        </div>
      </NuxtLink>
    </div>
  </div>
</template>


<style scoped>
.lookbook-btn {
  width: 100%;
  height: 40px;
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
    height: 70px;
  }

  @media screen and (min-width: 768px) {
    height: 100px;
    border: 2px solid;
  }
}
</style>
