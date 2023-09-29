<script setup lang="ts">
import { object, string, boolean, array } from 'yup'

const { params } = useRoute()
const collectionId: string = params.id

const title = collectionId ? 'Edit Collection' : 'Create new Collection'

const collectionForm = ref()
const collectionFormState = ref({
  name: undefined,
  description: undefined,
  preview_picture: [],
  is_available: true
})
const collectionFormSchema = object({
  name: string().required('Collection name is required'),
  description: string().required('Add more description'),
  preview_picture: array().of(string()),
  is_available: boolean(),
})

definePageMeta({
  alias: ['/admin/collections/create']
})
</script>


<template>
  <div>
    <div class="text-2xl font-bold">{{ title }}</div>
    <UForm ref="collectionForm" :state="collectionFormState" :schema="collectionFormSchema" class="flex flex-col gap-3"
      :validate-on="['submit']" @submit="submitSaveCollection">
      <UFormGroup name="name" required label="Name" class="lg:w-2/3 ">
        <UInput v-model="collectionFormState.name" />
      </UFormGroup>

      <UFormGroup name="description" required label="Description"
        help="To add a list of description item, enter new line for each item" class="lg:w-2/3 ">
        <UTextarea v-model="collectionFormState.description" rows="5" />
      </UFormGroup>

      <UFormGroup name="preview_picture" label="Preview Picture"></UFormGroup>
      <UploadImage v-model="collectionFormState.preview_picture" max-image="1" />

      <div>
        <UButton type="submit" label="Save Collection" />
      </div>
    </UForm>
  </div>
</template>
