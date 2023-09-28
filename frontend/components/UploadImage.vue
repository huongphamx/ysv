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
const { files, open, reset, onChange } = useFileDialog({
  accept: 'image/*',
  reset: false,
})
onChange((files) => {
  if (files) {
    const newUrl = []
    for (const file of files) {
      const url = URL.createObjectURL(file)
      newUrl.push(url)
    }
    console.log('on changes')
    emit('update:modelValue', props.modelValue.concat(newUrl))
  }
})

const deleteImage = (url: string) => {
  const remainUrls = props.modelValue.filter(u => u !== url)
  console.log('on delete')
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
      <div v-if="isAbleToAddImage"
        class="w-[200px] h-[200px] border-2 border-dashed hover:cursor-pointer flex flex-col justify-center items-center"
        @click="open()">
        <UIcon name="i-ph-plus" class="text-4xl" />
        <div v-if="maxImage">{{ `${modelValue.length}/${maxImage} ${maxImage > 1 ? 'pictures' : 'picture'}` }}</div>
      </div>
    </div>
  </div>
</template>

