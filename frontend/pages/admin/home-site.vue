<script lang="ts" setup>
import { useFileDialog } from '@vueuse/core'
import { Collection } from '@/types'

const config = useRuntimeConfig()
const videoSrc = ref(`${config.public.s3BaseUrl}/hero.mp4`)

const { open: openSelectVideo, onChange: onChangeVideo } = useFileDialog({ accept: 'video/mp4' })
onChangeVideo(async (files) => {
  if (files) {
    videoSrc.value = ''
    const formData = new FormData()
    formData.append('media_file', files[0])
    formData.append('object_key', 'hero.mp4')
    const { data, error } = await useCustomFetch('/v1/media/upload', {
      method: 'post',
      body: formData,
    })
    if (error.value) {
      // todo: toast
    } else if (data.value) {
      videoSrc.value = `${config.public.s3BaseUrl}/hero.mp4`
    }
  }
})

const selectedMainCollection = ref<Collection>()
const selectedHomeCollections = ref<Collection[]>([])

const collectionList = useCollectionList()
await getCollectionList()

selectedMainCollection.value = collectionList.value.find(c => c.is_main_collection)
selectedHomeCollections.value = collectionList.value.filter(c => c.is_show_in_home)

async function addMainCollection() {
  if (selectedMainCollection.value) {
    const { data, error } = await useCustomFetch('/v1/collections/add-main-collection', {
      method: 'post',
      body: { collection_id: selectedMainCollection.value.id }
    })
  }
}
const homeCollectionsError = ref('')
watch(selectedHomeCollections, () => {
  homeCollectionsError.value = ''
})
async function addHomeCollections() {
  if (selectedHomeCollections.value.length !== 10) {
    homeCollectionsError.value = 'Select 10 collections'
  } else {
    const { data, error } = await useCustomFetch('/v1/collections/add-home-collections', {
      method: 'post',
      body: { collection_ids: selectedHomeCollections.value.map(c => c.id) }
    })
  }
}
definePageMeta({
  layout: 'admin',
  middleware: 'admin',
})
useHead({
  title: 'Home configuration - Admin',
})
</script>


<template>
  <div class="h-screen overflow-auto p-5">
    <div class="w-full xl:w-1/2 ">
      <div class="text-2xl font-bold">Config Home Site</div>
      <div class="my-5 font-medium text-gray-700 dark:text-gray-200">Home Video</div>
      <video controls class="h-auto mb-3">
        <source :src="videoSrc" type="video/mp4">
      </video>
      <UButton label="Upload new Video" @click="openSelectVideo" />
      <div>* Please upload mp4 video type. You can using online converter to convert video type.</div>
      <div class="my-5 border-b"></div>

      <div class="my-5 font-medium text-gray-700 dark:text-gray-200">Main Collection</div>
      <USelectMenu searchable v-model="selectedMainCollection" :options="collectionList" option-attribute="name" />
      <UButton label="Save" class="my-2" @click="addMainCollection" />

      <div class="my-5 border-b"></div>
      <div class="my-5 font-medium text-gray-700 dark:text-gray-200">Collections to show in Home</div>
      <div>
        <USelectMenu multiple searchable v-model="selectedHomeCollections" :options="collectionList"
          option-attribute="name">
          <template #label>
            {{ selectedHomeCollections.length > 0
              ? selectedHomeCollections.map(c => c.name).join(', ')
              : 'Select collections'
            }}
          </template>
        </USelectMenu>
        <div v-if="homeCollectionsError" class="text-red-500">{{ homeCollectionsError }}</div>
        <UButton label="Save" class="my-2" @click="addHomeCollections" />
      </div>
    </div>
  </div>
</template>
