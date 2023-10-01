<script lang="ts" setup>
import { useFileDialog } from '@vueuse/core'

// todo: config s3 base url
const videoSrc = ref('https://ysv-dev-static-img.s3.ap-northeast-1.amazonaws.com/hero.mp4')

const { open: openSelectVideo, onChange: onChangeVideo } = useFileDialog({ accept: 'video/mp4' })
onChangeVideo(async (files) => {
  // todo: upload file to api
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
      videoSrc.value = 'https://ysv-dev-static-img.s3.ap-northeast-1.amazonaws.com/hero.mp4'
    }
  }
})

definePageMeta({
  layout: 'admin',
  middleware: 'admin',
})
</script>


<template>
  <div class="h-screen overflow-auto p-5">
    <div class="text-2xl font-bold">Config Home Site</div>

    <div class="my-5 font-medium text-gray-700 dark:text-gray-200">Home Video</div>
    <video controls class="w-full h-auto mb-3">
      <source :src="videoSrc" type="video/mp4">
    </video>
    <UButton label="Upload new Video" @click="openSelectVideo" />
    <div>* Please upload mp4 video type. You can using online converter to convert video type.</div>

    <div class="my-5 border-b"></div>
  </div>
</template>
