<script setup lang="ts">
import { useConfirmDialog } from '@vueuse/core'
import { Collection } from '@/types'

const collectionTableCols = [{
  key: 'name',
  label: 'Name',
}, {
  key: 'descriptions',
  label: 'Descriptions',
}, {
  key: 'preview_pic',
  label: 'Preview Picture',
}, {
  key: 'is_on_sale',
  label: 'On Sale',
}, {
  key: 'actions',
}]

const collectionList = useCollectionList()
await getCollectionList()

const { isRevealed: isShowedDeleteCollection, reveal: showDeleteCollection, confirm: confirmDeleteCollection } = useConfirmDialog()
async function deleteCollection(collectionId: string) {
  const { data: isConfirmed, isCanceled } = await showDeleteCollection()
  if (!isCanceled && isConfirmed) {
    const { data, error } = await useCustomFetch(`/v1/collections/${collectionId}`, { method: 'delete' })
    if (error.value) {
      // todo: toast
    } else if (data.value) {
      await getCollectionList()
    }
  }
}
</script>


<template>
  <div>
    <div class="text-2xl font-bold">Collections</div>
    <div class="my-2 flex gap-5">
      <div class="flex">
        <UInput placeholder="Search Collection" />
        <UButton icon="i-ph-magnifying-glass" />
      </div>
      <UButton label="Add Collection" icon="i-ph-plus" to="/admin/collections/create" />
    </div>

    <div>
      <UTable :columns="collectionTableCols" :rows="collectionList">
        <template #descriptions-data="{ row }: { row: Collection }">
          <div class="h-full">
            <li v-for="d, i in row.descriptions.split(/\r?\n/)" :key="i">{{ d }}</li>
          </div>
        </template>

        <template #preview_pic-data="{ row }: { row: Collection }">
          <img :src="row.preview_pic" alt="Collection preview picture" class="h-[150px]">
        </template>

        <template #is_on_sale-data="{ row }">
          <UIcon :name="row.is_on_sale ? 'i-ph-check' : 'i-ph-x'" class="text-3xl"
            :class="row.is_on_sale ? 'text-green-500' : 'text-red-500'" />
        </template>

        <template #actions-data="{ row }">
          <div class="max-w-[100px] flex gap-3">
            <UButton label="Edit" icon="i-ph-pencil" @click="$router.push(`/admin/collections/edit/${row.id}`)" />
            <UButton label="Delete" icon="i-ph-trash" color="red" @click="deleteCollection(row.id)" />
            <UModal :modelValue="isShowedDeleteCollection" prevent-close :transition="false">
              <div class="p-5">
                <div class="text-center text-2xl font-bold">Delete this collection?</div>
                <div class="my-5 text-center">Deleted collection can not be recovered.
                  Are you sure you want to delete?
                </div>
                <div class="flex justify-center gap-5">
                  <UButton @click="confirmDeleteCollection(true)" color="red">Yes, Delete</UButton>
                  <UButton @click="confirmDeleteCollection(false)" color="gray">Cancel</UButton>
                </div>
              </div>
            </UModal>
          </div>
        </template>
      </UTable>
    </div>
  </div>
</template>

