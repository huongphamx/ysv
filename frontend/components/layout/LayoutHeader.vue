<script lang="ts" setup>
import { Collection } from '@/types'
const collectionList = useCollectionList()

export interface CollectionGroup {
  alphabet: string,
  collections: Collection[]
}

const sortedCollectionGroups = computed(() => {
  const sortedCollections = collectionList.value.sort((a, b) => a.name.localeCompare(b.name, 'en', { sensitivity: 'base' }))
  const data = sortedCollections.reduce((r, e) => {
    // get first letter of name of current element
    let alphabet = e.name[0]
    // if there is no property in accumulator with this letter create it
    // @ts-ignore
    if (!r[alphabet]) r[alphabet] = { alphabet, collections: [e] }
    // @ts-ignore
    else r[alphabet].record.push(e)

    return r
  }, {})
  return Object.values(data)
})

const props = defineProps({
  isShowBottomLine: {
    type: Boolean,
    default: false,
  }
})
</script>


<template>
  <div class="z-10 py-2" :class="{ 'border-b': isShowBottomLine }">
    <div class="h-12 mycontainer mx-auto flex justify-between items-center text-white">
      <div class="text-2xl font-['Italiana']">
        <NuxtLink to="/">YSV</NuxtLink>
      </div>
      <div class="w-2/3 flex justify-between">
        <NuxtLink to="/about">ABOUT</NuxtLink>
        <NuxtLink to="/events">EVENTS</NuxtLink>
        <NuxtLink to="/contact">CONTACT</NuxtLink>
        <NuxtLink to="/payment-delivery">PAYMENT & DELIVERY</NuxtLink>
        <NuxtLink to="/cooperation">COOPERATION</NuxtLink>
        <UPopover mode="hover">
          <div class="flex items-center">COLLECTIONS
            <UIcon name="i-ph-arrow-down-right" />
          </div>
          <template #panel>
            <div class="p-2">
              <div v-for="g, i in (sortedCollectionGroups as CollectionGroup[])" :key="i">
                <div class="border-b text-gray-500">{{ g.alphabet }}</div>
                <div v-for="c, i in g.collections" class="my-2">
                  <NuxtLink :to="`/collections/${c.id}`" class="underline">{{ c.name.toUpperCase() }}</NuxtLink>
                </div>
              </div>
            </div>
          </template>
        </UPopover>
      </div>
      <div>
        <UButton icon="i-ph-heart" color="gray" variant="ghost" />
      </div>
    </div>
  </div>
</template>

