<script lang="ts" setup>
import { useFileDialog } from '@vueuse/core'
import { Collection } from '@/types'

const toast = useToast()
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
      toast.add({ title: 'Error', description: error.value.data.detail, icon: 'i-ph-x-circle', color: 'red' })
    } else if (data.value) {
      toast.add({ title: 'Success', description: 'New video has been uploaded', icon: 'i-ph-check-circle', color: 'green' })
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

const mainCollectionPics = selectedMainCollection.value?.main_collection_pics?.split('$')
const mainCollectionPic1 = ref<string[]>([])
const mainCollectionPic2 = ref<string[]>([])
const mainCollectionPic3 = ref<string[]>([])
if (mainCollectionPics) {
  mainCollectionPic1.value = [mainCollectionPics[0]]
  mainCollectionPic2.value = [mainCollectionPics[1]]
  mainCollectionPic3.value = [mainCollectionPics[2]]
}
const mainCollectionDescription = ref(selectedMainCollection.value?.main_collection_description)
const mainCollectionDescription2 = ref(selectedMainCollection.value?.main_collection_description_2)

async function addMainCollection() {
  if (selectedMainCollection.value) {
    const { data, error } = await useCustomFetch('/v1/collections/add-main-collection', {
      method: 'post',
      body: {
        collection_id: selectedMainCollection.value.id,
        main_collection_description: mainCollectionDescription.value,
        main_collection_description_2: mainCollectionDescription2.value,
        main_collection_pics: mainCollectionPic1.value[0] + '$' + mainCollectionPic2.value[0] + '$' + mainCollectionPic3.value[0]
      }
    })
    toast.add({ title: 'Success', description: 'Main collection saved', icon: 'i-ph-check-circle', color: 'green' })
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
    if (error.value) {
      toast.add({ title: 'Error', description: error.value.data.detail, icon: 'i-ph-x-circle', color: 'red' })
    } else if (data.value) {
      toast.add({ title: 'Success', description: 'Home collections saved', icon: 'i-ph-check-circle', color: 'green' })
    }
  }
}
definePageMeta({
  layout: 'admin',
  middleware: 'admin',
  pageTransition: false,
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
      <div class="my-2">
        <UTextarea v-model="mainCollectionDescription" placeholder="Main collection description part 1" />
        <UTextarea v-model="mainCollectionDescription2" placeholder="Main collection description part 2" class="mt-2" />
      </div>
      <div class="my-5 flex">
        <UploadImage v-model="mainCollectionPic1" :max-image="1" />
        <UploadImage v-model="mainCollectionPic2" :max-image="1" />
        <UploadImage v-model="mainCollectionPic3" :max-image="1" />
      </div>
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
