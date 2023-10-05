<script setup lang="ts">
import { Collection } from '@/types'

export interface CollectionGroup {
  alphabet: string,
  collections: Collection[]
}

const collectionList = useCollectionList()

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
</script>


<template>
  <UPopover mode="hover">
    <div class="flex items-center">COLLECTIONS
      <UIcon name="i-ph-arrow-down-right" />
    </div>
    <template #panel>
      <div class="p-2">
        <div v-for="g, i in (sortedCollectionGroups as CollectionGroup[])" :key="i">
          <div class="border-b text-gray-500">{{ g.alphabet }}</div>
          <div v-for="c, i in g.collections" class="my-2 text-black">
            <NuxtLink :to="`/catalog/${c.id}`" class="underline">{{ c.name.toUpperCase() }}</NuxtLink>
          </div>
        </div>
      </div>
    </template>
  </UPopover>
</template>

