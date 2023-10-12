<script setup lang="ts">
import { object, string, number, array, boolean } from 'yup'
import { v4 as uuidv4 } from 'uuid'
import { Product } from '@/types'

const toast = useToast()

const collectionList = useCollectionList()
getCollectionList()
const sizeList = useSizeList()
await getSizeList()
const sizeOrder = ['XS', 'S', 'M', 'L'];

const { params } = useRoute()
const productId = params.id

const title = productId ? 'Edit Product' : 'Create new Product'

const sizeVariants = ref([{
  id: uuidv4(),
  size: 'XS',
  is_pre_order: false
}, {
  id: uuidv4(),
  size: 'S',
  is_pre_order: false
}, {
  id: uuidv4(),
  size: 'M',
  is_pre_order: false
}, {
  id: uuidv4(),
  size: 'L',
  is_pre_order: true
},])
const sizeTableCols = [{
  key: 'size',
  label: 'Size',
}, {
  key: 'is_pre_order',
  label: 'Is pre-order',
},]

const productForm = ref()
const productFormState = ref({
  collection_id: '',
  name: '',
  is_available: true,
  price: 0,
  descriptions: '',
  preview_pic: [] as string[],
  pictures: [] as string[],
})
const productFormSchema = object({
  collection_id: string().required('Select collection of this product'),
  name: string().required('Product name required'),
  is_available: boolean(),
  price: number().required('Set a price').min(0, 'Min is 0'),
  descriptions: string().required('Give some descriptions'),
  preview_pic: array().of(string()),
  pictures: array().of(string()),
})
// if collectionId not None, i.e. editing -> get collection detail
if (productId) {
  const { data, error } = await useCustomFetch<Product>(`/v1/products/${productId}`)
  if (error.value) {
    // todo: toast
  } else if (data.value) {
    productFormState.value.collection_id = data.value.collection_id
    productFormState.value.name = data.value.name
    productFormState.value.is_available = data.value.is_available
    productFormState.value.price = data.value.price
    productFormState.value.descriptions = data.value.descriptions
    productFormState.value.preview_pic = [data.value.preview_pic]
    productFormState.value.pictures = data.value.pictures.map(o => o.url)
    const unSortedSizeVariants = data.value.size_variants.map(v => {
      return {
        id: v.id,
        size: sizeList.value.find(s => s.id === v.clothes_size_id)?.label!,
        is_pre_order: v.is_pre_order
      }
    })
    sizeVariants.value = unSortedSizeVariants.sort((a, b) => {
      const sizeA = sizeOrder.indexOf(a.size)
      const sizeB = sizeOrder.indexOf(b.size)

      return sizeA - sizeB
    })
  }
}

const imageUrlsError = ref('')
watch(() => productFormState.value.pictures, (newList) => {
  if (newList.length > 0) { imageUrlsError.value = '' }
  else if (newList.length === 0) { imageUrlsError.value = 'Please choose pictures' }
})
const selectedCollection = computed(() => {
  if (!productFormState.value.collection_id) return undefined
  return collectionList.value.find(c => c.id === productFormState.value.collection_id)
})
async function submitSaveProduct() {
  await productForm.value!.validate()
  if (productFormState.value.pictures.length < 1) {
    imageUrlsError.value = 'Please choose pictures'
  }
  const productData = {
    collection_id: productFormState.value.collection_id,
    name: productFormState.value.name,
    is_available: productFormState.value.is_available,
    price: productFormState.value.price,
    descriptions: productFormState.value.descriptions,
    preview_pic: productFormState.value.preview_pic[0],
    pictures: productFormState.value.pictures,
    size_variants: sizeVariants.value.map((size) => {
      return {
        id: size.id,
        is_pre_order: size.is_pre_order,
        clothes_size_id: sizeList.value.find(s => s.label === size.size)?.id
      }
    }),
  }
  const url = productId ? `/v1/products/${productId}` : '/v1/products/'
  const method = productId ? 'put' : 'post'
  const { data, error } = await useCustomFetch(url, {
    method,
    body: productData,
  })
  if (error.value) {
    toast.add({ title: 'Error', description: error.value.data.detail, icon: 'i-ph-x-circle', color: 'red' })
  } else if (data.value) {
    toast.add({ title: 'Success', description: 'Product saved', icon: 'i-ph-check-circle', color: 'green' })
    return navigateTo('/admin/products/')
  }
}

definePageMeta({
  alias: ['/admin/products/create']
})
useHead({
  title: 'Product management - Admin'
})
</script>

<template>
  <div>
    <div class="text-2xl font-bold">
      <UButton label="Back" icon="i-ph-arrow-left" to="/admin/products/" variant="ghost" color="gray" /> {{ title }}
    </div>
    <div class="lg:w-2/3 my-5 p-2 border border-gray-500 rounded-lg">
      <UForm ref="productForm" :state="productFormState" :schema="productFormSchema" :validate-on="['submit', 'input']"
        @submit="submitSaveProduct" class="flex flex-col gap-3">
        <UFormGroup name="collection_id" required label="Collection">
          <USelectMenu placeholder="Select Collection" v-model="productFormState.collection_id" :options="collectionList"
            value-attribute="id" option-attribute="name">
            <template #label>{{ selectedCollection ? selectedCollection.name : 'Select Collection' }}</template>
          </USelectMenu>
        </UFormGroup>

        <UFormGroup name="name" required label="Color">
          <UInput v-model="productFormState.name" />
        </UFormGroup>

        <UFormGroup name="is_available" required label="Set available">
          <UToggle v-model="productFormState.is_available" />
        </UFormGroup>

        <UFormGroup name="price" required label="Price">
          <UInput type="number" v-model="productFormState.price">
            <template #trailing> <span class="text-gray-500 dark:text-gray-400 text-xs">USD</span> </template>
          </UInput>
        </UFormGroup>

        <UFormGroup name="descriptions" required label="Descriptions">
          <UTextarea v-model="productFormState.descriptions" :rows="5" />
        </UFormGroup>

        <UFormGroup name="preview_pic" required label="Preview Picture"></UFormGroup>
        <UploadImage v-model="productFormState.preview_pic" :max-image="1" />

        <div
          class="text-sm font-medium text-gray-700 dark:text-gray-200 after:content-['*'] after:ms-0.5 after:text-red-500 dark:after:text-red-400">
          Pictures</div>
        <UploadImage v-model="productFormState.pictures" />
        <div v-if="imageUrlsError" class="mt-2 text-red-500 dark:text-red-400 text-sm">{{ imageUrlsError }}</div>
        <div v-else class="text-sm">Hold 'Cmd (Ctrl on Windows)' to choose multiple pictures</div>

        <div class="text-sm font-medium text-gray-700 dark:text-gray-200">Config Available Size of Product</div>
        <UTable :rows="sizeVariants" :columns="sizeTableCols">
          <template #is_pre_order-data="{ row }">
            <UToggle v-model="row.is_pre_order" />
          </template>
        </UTable>

        <div class="flex gap-3">
          <UButton type="submit" label="Save Product" />
          <UButton label="Cancel" color="gray" to="/admin/products/" />
        </div>
      </UForm>
    </div>
  </div>
</template>