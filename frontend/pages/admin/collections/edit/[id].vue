<script setup lang="ts">
import { object, string, boolean, array } from 'yup'
import { Collection } from '@/types'

const toast = useToast()
const { params } = useRoute()
const collectionId = params.id as string

const title = collectionId ? 'Edit Collection' : 'Create new Collection'

const collectionForm = ref()
const collectionFormState = ref({
  name: '',
  descriptions: '',
  preview_pic: [] as string[],
  is_on_sale: true,
  lookbook_layout_code: 'two',
})
const collectionFormSchema = object({
  name: string().required('Collection name is required'),
  descriptions: string().required('Add more descriptions'),
  preview_pic: array().of(string()),
  is_on_sale: boolean(),
  lookbook_layout_code: string(),
})
// if collectionId not None, i.e. editing -> get collection detail
if (collectionId) {
  const { data, error } = await useCustomFetch<Collection>(`/v1/collections/${collectionId}`)
  if (error.value) {
    // todo: toast
  } else if (data.value) {
    collectionFormState.value.name = data.value.name
    collectionFormState.value.descriptions = data.value.descriptions
    collectionFormState.value.preview_pic = [data.value.preview_pic]
    collectionFormState.value.is_on_sale = data.value.is_on_sale
    collectionFormState.value.lookbook_layout_code = data.value.lookbook_layout_code
  }
}

async function submitSaveCollection() {
  await collectionForm.value!.validate()
  const collectionData = {
    name: collectionFormState.value.name,
    descriptions: collectionFormState.value.descriptions,
    is_on_sale: collectionFormState.value.is_on_sale,
    preview_pic: collectionFormState.value.preview_pic[0],
    lookbook_layout_code: collectionFormState.value.lookbook_layout_code,
  }
  const url = collectionId ? `/v1/collections/${collectionId}` : '/v1/collections/'
  const method = collectionId ? 'put' : 'post'
  const { data, error } = await useCustomFetch(url, {
    method,
    body: collectionData
  })
  if (error.value) {
    toast.add({ title: 'Error', description: error.value.data.detail, icon: 'i-ph-x-circle', color: 'red' })
  } else if (data.value) {
    toast.add({ title: 'Success', description: 'Collection saved', icon: 'i-ph-check-circle', color: 'green' })
    return navigateTo('/admin/collections/')
  }
}

const lookbookLayouts = [{
  code: 'two',
  name: 'Two Pictures',
}, {
  code: 'two_reversed',
  name: 'Two Pictures Reversed',
}, {
  code: 'three',
  name: 'Three Pictures',
},]

definePageMeta({
  alias: ['/admin/collections/create']
})
useHead({
  title: 'Collection management - Admin'
})
</script>


<template>
  <div>
    <div class="text-2xl font-bold">
      <UButton label="Back" icon="i-ph-arrow-left" to="/admin/collections/" variant="ghost" color="gray" />{{ title }}
    </div>
    <div class="lg:w-2/3 my-5 p-2 border border-gray-500 rounded-lg">
      <UForm ref="collectionForm" :state="collectionFormState" :schema="collectionFormSchema" class="flex flex-col gap-3"
        :validate-on="['submit']" @submit="submitSaveCollection">
        <UFormGroup name="name" required label="Name">
          <UInput v-model="collectionFormState.name" />
        </UFormGroup>

        <UFormGroup name="is_on_sale" label="Set on sale">
          <UToggle v-model="collectionFormState.is_on_sale" />
        </UFormGroup>

        <UFormGroup name="description" required label="Description"
          help="To add a list of description item, enter new line for each item">
          <UTextarea v-model="collectionFormState.descriptions" :rows="5" />
        </UFormGroup>

        <UFormGroup name="preview_pic" label="Preview Picture"></UFormGroup>
        <UploadImage v-model="collectionFormState.preview_pic" :max-image="1" />

        <UFormGroup name="lookbook_layout_code" label="Lookbook Layout"></UFormGroup>
        <USelectMenu v-model="collectionFormState.lookbook_layout_code" :options="lookbookLayouts"
          placeholder="Select layout for lookbook" value-attribute="code" option-attribute="name">
          <template #label> {{
            lookbookLayouts.find(l => l.code === collectionFormState.lookbook_layout_code)?.name }}
          </template>
        </USelectMenu>

        <div class="flex gap-3">
          <UButton type="submit" label="Save Collection" />
          <UButton label="Cancel" color="gray" to="/admin/collections" />
        </div>
      </UForm>
    </div>
  </div>
</template>

