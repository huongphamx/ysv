<script setup lang="ts">
import { useFileDialog } from "@vueuse/core";

const props = defineProps<{
  modelValue: string[],
  maxImage?: number,
}>()
const emit = defineEmits<{
  'update:modelValue': [data: string[]],
}>()

const isAbleToAddImage = computed(() => {
  if (props.maxImage) { return props.modelValue.length < props.maxImage }
  return true
})
const isUploading = ref(false)
const { files, open, onChange } = useFileDialog({
  accept: 'image/*',
  reset: false,
  multiple: props.maxImage !== 1
})
onChange(async (files) => {
  if (files) {
    const newUrl: string[] = []
    for (const file of files) {
      isUploading.value = true
      const formData = new FormData()
      formData.append('media_file', file)
      const {data, error} = await useCustomFetch<string>('/v1/media/upload', {
        method: 'post',
        body: formData
      })
      if (error.value) {
        // todo: toast
      } else if (data.value) {
        newUrl.push(data.value)
        isUploading.value = false
      }
    }
    emit('update:modelValue', props.modelValue.concat(newUrl))
  }
})

const deleteImage = (url: string) => {
  // todo: confirm delete
  // todo: call delete api
  const remainUrls = props.modelValue.filter(u => u !== url)
  emit('update:modelValue', remainUrls)
}
</script> 


<template>
  <div>
    <div class="my-2 flex gap-2 flex-wrap items-center">
      <template v-if="modelValue">
        <div v-for="url, i in modelValue" :key="i" class="relative group border rounded-md p-1">
          <img :src="url" alt="Uploading Image" class="h-[200px] group-hover:opacity-50">
          <UButton icon="i-ph-trash" size="lg" color="red"
            class="invisible group-hover:visible absolute top-1/2 right-1/2 translate-x-1/2" @click="deleteImage(url)" />
        </div>
      </template>
      <template v-if="isUploading">
        <div class="w-[200px] h-[200px] border-2 border-dashed hover:cursor-pointer flex flex-col justify-center items-center"
        @click="open()">
        <UIcon name="i-ph-circle-notch" class="text-4xl animate-spin" />
      </div>
      </template>
      <div v-if="isAbleToAddImage && !isUploading"
        class="w-[200px] h-[200px] border-2 border-dashed hover:cursor-pointer flex flex-col justify-center items-center"
        @click="open()">
        <UIcon name="i-ph-plus" class="text-4xl" />
        <div v-if="maxImage">{{ `${modelValue.length}/${maxImage} ${maxImage > 1 ? 'pictures' : 'picture'}` }}</div>
      </div>
    </div>
  </div>
</template>

