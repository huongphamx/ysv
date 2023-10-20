<script lang="ts" setup>
import { Collection } from '@/types'

const props = defineProps<{
  collections: Collection[],
}>()

const toast = useToast()
const collectionList = useCollectionList()

const collection1 = ref<Collection | undefined>(props.collections.find(c => c.home_position === 1))
const collection2 = ref<Collection | undefined>(props.collections.find(c => c.home_position === 2))
const collection3 = ref<Collection | undefined>(props.collections.find(c => c.home_position === 3))
const collection4 = ref<Collection | undefined>(props.collections.find(c => c.home_position === 4))
const collection5 = ref<Collection | undefined>(props.collections.find(c => c.home_position === 5))
const collection6 = ref<Collection | undefined>(props.collections.find(c => c.home_position === 6))
const collection7 = ref<Collection | undefined>(props.collections.find(c => c.home_position === 7))
const collection8 = ref<Collection | undefined>(props.collections.find(c => c.home_position === 8))
const collection9 = ref<Collection | undefined>(props.collections.find(c => c.home_position === 9))
const collection10 = ref<Collection | undefined>(props.collections.find(c => c.home_position === 10))


async function saveHomeCollections() {
  const postData = [
    collection1.value?.id,
    collection2.value?.id,
    collection3.value?.id,
    collection4.value?.id,
    collection5.value?.id,
    collection6.value?.id,
    collection7.value?.id,
    collection8.value?.id,
    collection9.value?.id,
    collection10.value?.id,
  ]
  const collectionIds = postData.filter(c => c !== undefined)
  if (new Set(collectionIds).size !== collectionIds.length) {
    toast.add({ title: 'Error', description: 'Duplicate two or more collections', icon: 'i-ph-x-circle', color: 'red' })
    return
  }
  const { data, error } = await useCustomFetch('/v1/collections/add-home-collections', {
    method: 'post',
    body: { collection_ids: postData },
  })
  if (error.value) {
    toast.add({ title: 'Error', description: error.value.data.detail, icon: 'i-ph-x-circle', color: 'red' })
  } else if (data.value) {
    toast.add({ title: 'Success', description: 'Home collections saved', icon: 'i-ph-check-circle', color: 'green' })
    await getCollectionList()
    collection1.value = collectionList.value.find(c => c.home_position === 1)
    collection2.value = collectionList.value.find(c => c.home_position === 2)
    collection3.value = collectionList.value.find(c => c.home_position === 3)
    collection4.value = collectionList.value.find(c => c.home_position === 4)
    collection5.value = collectionList.value.find(c => c.home_position === 5)
    collection6.value = collectionList.value.find(c => c.home_position === 6)
    collection7.value = collectionList.value.find(c => c.home_position === 7)
    collection8.value = collectionList.value.find(c => c.home_position === 8)
    collection9.value = collectionList.value.find(c => c.home_position === 9)
    collection10.value = collectionList.value.find(c => c.home_position === 10)
  }
}

function clearCollections() {
  collection1.value = undefined
  collection2.value = undefined
  collection3.value = undefined
  collection4.value = undefined
  collection5.value = undefined
  collection6.value = undefined
  collection7.value = undefined
  collection8.value = undefined
  collection9.value = undefined
  collection10.value = undefined
}
</script>


<template>
  <div>
    <div class="flex gap-5 items-center mb-2">1.
      <USelectMenu placeholder="Select Collection 1" v-model="collection1" searchable :options="collections"
        option-attribute="name" class="flex-1" />
    </div>
    <div class="flex gap-5 items-center mb-2">2.
      <USelectMenu placeholder="Select Collection 2" v-model="collection2" searchable :options="collections"
        option-attribute="name" class="flex-1" />
    </div>
    <div class="flex gap-5 items-center mb-2">3.
      <USelectMenu placeholder="Select Collection 3" v-model="collection3" searchable :options="collections"
        option-attribute="name" class="flex-1" />
    </div>
    <div class="flex gap-5 items-center mb-2">4.
      <USelectMenu placeholder="Select Collection 4" v-model="collection4" searchable :options="collections"
        option-attribute="name" class="flex-1" />
    </div>
    <div class="flex gap-5 items-center mb-2">5.
      <USelectMenu placeholder="Select Collection 5" v-model="collection5" searchable :options="collections"
        option-attribute="name" class="flex-1" />
    </div>
    <div class="flex gap-5 items-center mb-2">6.
      <USelectMenu placeholder="Select Collection 6" v-model="collection6" searchable :options="collections"
        option-attribute="name" class="flex-1" />
    </div>
    <div class="flex gap-5 items-center mb-2">7.
      <USelectMenu placeholder="Select Collection 7" v-model="collection7" searchable :options="collections"
        option-attribute="name" class="flex-1" />
    </div>
    <div class="flex gap-5 items-center mb-2">8.
      <USelectMenu placeholder="Select Collection 8" v-model="collection8" searchable :options="collections"
        option-attribute="name" class="flex-1" />
    </div>
    <div class="flex gap-5 items-center mb-2">9.
      <USelectMenu placeholder="Select Collection 9" v-model="collection9" searchable :options="collections"
        option-attribute="name" class="flex-1" />
    </div>
    <div class="flex gap-5 items-center mb-2">10.
      <USelectMenu placeholder="Select Collection 10" v-model="collection10" searchable :options="collections"
        option-attribute="name" class="flex-1" />
    </div>
    <div>
      <UButton label="Save" class="my-2" @click="saveHomeCollections" />
      <UButton label="Clear" color="gray" class="m-2" @click="clearCollections" />
    </div>
  </div>
</template>


<style scoped></style>

