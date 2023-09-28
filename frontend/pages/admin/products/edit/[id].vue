<script setup lang="ts">
import { object, string, number, array } from 'yup'

const { params } = useRoute()
const productId = params.id

const title = productId ? 'Edit Product' : 'Create new Product'

const productForm = ref()
const productFormState = ref({
  name: undefined,
  price: undefined,
  description: undefined,
  images: [],
})
const productFormSchema = object({
  name: string().required('Product name required'),
  price: number().required('Set a price').min(0, 'Min is 0'),
  description: string().required('Give some description'),
  images: array().of(string()),
})
const imageUrlsError = ref('')
watch(() => productFormState.value.images, (newList) => {
  if (newList.length > 0) { imageUrlsError.value = '' }
  else if (newList.length === 0) { imageUrlsError.value = 'Please choose images' }
})
async function submitSaveProduct() {
  await productForm.value!.validate()
  if (productFormState.value.images.length < 1) {
    imageUrlsError.value = 'Please choose images'
  }
}

definePageMeta({
  alias: ['/admin/products/create']
})
</script>

<template>
  <div>
    <div class="text-2xl font-bold">{{ title }}</div>
    <UForm ref="productForm" :state="productFormState" :schema="productFormSchema" :validate-on="['submit']"
      @submit="submitSaveProduct" class="flex flex-col gap-3">
      <UFormGroup name="name" required label="Product name" class="lg:w-2/3 ">
        <UInput v-model="productFormState.name" />
      </UFormGroup>

      <UFormGroup name="price" required label="Price" class="lg:w-2/3 ">
        <UInput type="number" v-model="productFormState.price" />
      </UFormGroup>

      <UFormGroup name="description" required label="Description" class="lg:w-2/3 ">
        <UTextarea v-model="productFormState.description" />
      </UFormGroup>

      <div
        class="text-sm font-medium text-gray-700 dark:text-gray-200 after:content-['*'] after:ms-0.5 after:text-red-500 dark:after:text-red-400">
        Pictures</div>
      <UploadImage v-model="productFormState.images" />
      <div v-if="imageUrlsError" class="mt-2 text-red-500 dark:text-red-400 text-sm">{{ imageUrlsError }}</div>

      <div>
        <UButton type="submit" label="Save Product" />
      </div>
    </UForm>
  </div>
</template>