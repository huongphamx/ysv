<script lang="ts" setup>
import { useConfirmDialog } from '@vueuse/core'

const orderList = useOrderList()
await getOrderList()

const orderTableCols = [{
  key: 'name',
  label: 'Name',
}, {
  key: 'country',
  label: 'Country',
}, {
  key: 'city',
  label: 'City',
}, {
  key: 'state',
  label: 'State/Province',
}, {
  key: 'street_address',
  label: 'Street address',
}, {
  key: 'zip_code',
  label: 'Zip/Postal Code',
}, {
  key: 'phone_number',
  label: 'Phone number',
}, {
  key: 'is_paid',
  label: 'Is paid',
}, {
  key: 'is_delivered',
  label: 'Is delivered',
},]

const { isRevealed: isShowedDeliver, reveal: showDeliver, confirm: confirmDeliver } = useConfirmDialog()
async function deliverOrder(orderId: string) {
  const { data: isConfirmed, isCanceled } = await showDeliver()
  if (!isCanceled && isConfirmed) {
    const { data, error } = await useCustomFetch(`/v1/orders/${orderId}`, {
      method: 'put',
      body: { is_delivered: true }
    })
    if (error.value) {
      // todo: toast
    } else if (data.value) {
      await getOrderList()
    }
  }
}

const searchPhoneNumber = ref('')
async function searchOrderByPhone() {
  await getOrderList({ phone_number: searchPhoneNumber.value })
}

definePageMeta({
  layout: 'admin',
  middleware: 'admin',
})
useHead({
  title: 'Order management - Admin'
})
</script>


<template>
  <div>
    <div class="text-2xl font-bold">Orders</div>
    <div class="my-2 flex gap-5">
      <div class="flex">
        <UInput placeholder="Search by Phone number" v-model="searchPhoneNumber" />
        <UButton icon="i-ph-magnifying-glass" @click="searchOrderByPhone" />
      </div>
    </div>

    <div>
      <UTable :columns="orderTableCols" :rows="orderList">
        <template #name-data="{ row }">
          {{ row.fname + row.lname }}
        </template>

        <template #is_paid-data="{ row }">
          <UIcon :name="row.is_paid ? 'i-ph-check-circle' : 'i-ph-x-circle'" class="text-2xl"
            :class="row.is_paid ? 'text-green-500' : 'text-red-500'" />
        </template>

        <template #is_delivered-data="{ row }">
          <div class="flex items-center">
            <UIcon :name="row.is_delivered ? 'i-ph-check-circle' : 'i-ph-x-circle'" class="text-2xl"
              :class="row.is_delivered ? 'text-green-500' : 'text-red-500'" />
            <UButton v-if="!row.is_delivered" label="Deliver" @click="deliverOrder(row.id)" />
            <UModal :modelValue="isShowedDeliver" prevent-close :transition="false">
              <div class="p-5">
                <div class="text-center text-2xl font-bold">Mark this order as delivered?</div>
                <div class="flex justify-center gap-5">
                  <UButton @click="confirmDeliver(true)">Yes</UButton>
                  <UButton @click="confirmDeliver(false)" color="gray">Cancel</UButton>
                </div>
              </div>
            </UModal>
          </div>
        </template>
      </UTable>
    </div>
  </div>
</template>
