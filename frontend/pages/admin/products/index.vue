<script lang="ts" setup>
import { Product } from '@/types'

const productTableCols = [{
  key: 'collection',
  label: 'Collection',
}, {
  key: 'name',
  label: 'Color',
}, {
  key: 'descriptions',
  label: 'Descriptions',
}, {
  key: 'preview_pic',
  label: 'Preview Picture',
}, {
  key: 'is_available',
  label: 'Available',
}, {
  key: 'actions',
}]

const productList = useProductList()
await getProductList()
const collectionList = useCollectionList()
await getCollectionList()

</script>


<template>
  <div>
    <div class="text-2xl font-bold">Products</div>
    <div class="my-2 flex gap-5">
      <div class="flex">
        <UInput placeholder="Search Product" />
        <UButton icon="i-ph-magnifying-glass" />
      </div>
      <UButton label="Add Product" icon="i-ph-plus" to="/admin/products/create" />
    </div>

    <div>
      <UTable :columns="productTableCols" :rows="productList">
        <template #collection-data="{ row }">
          {{ collectionList.find(c => c.id === row.collection_id)?.name }}
        </template>

        <template #descriptions-data="{ row }: { row: Product }">
          <div class="h-full">
            <li v-for="d, i in row.descriptions.split(/\r?\n/)" :key="i">{{ d }}</li>
          </div>
        </template>

        <template #preview_pic-data="{ row }: { row: Product }">
          <img :src="row.preview_pic" alt="Collection preview picture" class="h-[150px]">
        </template>

        <template #is_available-data="{ row }">
          <UIcon :name="row.is_available ? 'i-ph-check' : 'i-ph-x'" class="text-3xl"
            :class="row.is_available ? 'text-green-500' : 'text-red-500'" />
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
