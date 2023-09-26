<script setup lang="ts">
import { object, string, number, array } from 'yup'
import { useFileDialog } from "@vueuse/core";

const { params } = useRoute()
const productId = params.id

const title = productId ? 'Edit Product' : 'Create new Product'

const productForm = ref()
const productFormState = ref({
  name: undefined,
  price: undefined,
  description: undefined,
  images: undefined,
})
const productFormSchema = object({
  name: string().required('Product name required'),
  price: number().required('Set a price').min(0, 'Min is 0'),
  description: string().required('Give some description'),
  images: array().of(string()),
})
async function submitSaveProduct() {
  await productForm.value!.validate()

}




const { files, open, reset, onChange } = useFileDialog({
  accept: 'image/*'
})
const imgUrls = ref<string[]>([])
onChange((files) => {
  if (files) {
    for (const file of files) {
      const url = URL.createObjectURL(file)
      imgUrls.value.push(url)
    }
  }
})
const resetImgList = () => {
  reset()
  imgUrls.value = []
}
const deleteImage = (url: string) => {
  imgUrls.value = imgUrls.value.filter(u => u !== url)
}

definePageMeta({
  alias: ['/admin/products/create']
})
</script>

<template>
  <div>
    <div class="text-2xl font-bold">{{ title }}</div>

    <UForm ref="productForm" :state="productFormState" :schema="productFormSchema" :validate-on="['submit']"
      @submit="submitSaveProduct">
      <UFormGroup name="name" required label="Product name">
        <UInput v-model="productFormState.name" />
      </UFormGroup>

      <UFormGroup name="price" required label="Price">
        <UInput type="number" v-model="productFormState.price" />
      </UFormGroup>

      <UFormGroup name="description" required label="Description">
        <UTextarea v-model="productFormState.description" />
      </UFormGroup>

      <UFormGroup name="images" required label="Images">
        <UTextarea v-model="productFormState.images" />
      </UFormGroup>

      <UButton type="button" :disabled="!files" @click="resetImgList">
        Reset
      </UButton>

      <div class="flex gap-2 flex-wrap items-center">
        <template v-if="files">
          <div v-for="url, i in imgUrls" :key="i" class="relative group border rounded-md p-1">
            <img :src="url" alt="Uploading Image" class="h-[200px] group-hover:opacity-50">
            <UButton icon="i-ph-trash" size="lg" color="red"
              class="invisible group-hover:visible absolute top-1/2 right-1/2 translate-x-1/2"
              @click="deleteImage(url)" />
          </div>
        </template>
        <div class="w-20 h-20 border-2 border-dashed hover:cursor-pointer flex justify-center items-center"
          @click="open()">
          <uIcon name="i-ph-plus" class="text-4xl" />
        </div>
      </div>

      <UButton type="submit" label="Save" />
    </UForm>
  </div>
</template>