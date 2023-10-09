<script setup lang="ts">
import { Collection } from '@/types'

export interface CollectionGroup {
  alphabet: string,
  collections: Collection[]
}

const collectionList = useCollectionList()

const sortedCollectionGroups = computed(() => {
  const upperCasedCollections = collectionList.value.map(c => {
    c.name = c.name.toUpperCase()
    return c
  })
  const sortedCollections = upperCasedCollections.sort((a, b) => a.name.localeCompare(b.name, 'en', { sensitivity: 'base' }))
  const data = sortedCollections.reduce((r, e) => {
    // get first letter of name of current element
    let alphabet = e.name[0]
    // if there is no property in accumulator with this letter create it
    // @ts-ignore
    if (!r[alphabet]) r[alphabet] = { alphabet, collections: [e] }
    // @ts-ignore
    else r[alphabet].collections.push(e)

    return r
  }, {})
  return Object.values(data)
})
</script>


<template>
  <UPopover>
    <div class="flex items-center">COLLECTIONS
      <UIcon name="i-ph-arrow-down-right" />
    </div>
    <template #panel>
      <div class="p-2 w-[300px] max-h-[580px] overflow-auto">
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

