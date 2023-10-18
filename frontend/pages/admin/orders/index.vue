<script lang="ts" setup>
import { Order } from '@/types'
import { useConfirmDialog } from '@vueuse/core'

const toast = useToast()

const totalOrder = useTotalOrder()
const pageOrder = usePageOrder()

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
},
// {
//   key: 'state',
//   label: 'State/Province',
// }, {
//   key: 'street_address',
//   label: 'Street address',
// }, {
//   key: 'zip_code',
//   label: 'Zip/Postal Code',
// }, 
{
  key: 'phone_number',
  label: 'Phone number',
}, {
  key: 'email',
  label: 'Email address',
}, {
  key: 'is_paid',
  label: 'Is paid',
}, {
  key: 'is_delivered',
  label: 'Is delivered',
}, {
  key: 'actions',
}]

const { isRevealed: isShowedDeliver, reveal: showDeliver, confirm: confirmDeliver } = useConfirmDialog()
async function deliverOrder(orderId: string) {
  const { data: isConfirmed, isCanceled } = await showDeliver()
  if (!isCanceled && isConfirmed) {
    const { data, error } = await useCustomFetch(`/v1/orders/${orderId}`, {
      method: 'put',
      body: { is_delivered: true }
    })
    if (error.value) {
      toast.add({ title: 'Error', description: error.value.data.detail, icon: 'i-ph-x-circle', color: 'red' })
    } else if (data.value) {
      toast.add({ title: 'Success', description: 'Order saved', icon: 'i-ph-check-circle', color: 'green' })
      await getOrderList()
    }
  }
}

const searchPhoneNumber = ref('')
async function searchOrderByPhone() {
  await getOrderList({ phone_number: searchPhoneNumber.value })
}

const isShowedDetail = ref(false)
const orderDetail = ref<Order>()
async function getOrderDetail(orderId: string) {
  const { data, error } = await useCustomFetch<Order>(`/v1/orders/${orderId}`)
  if (error.value) {

  } else if (data.value) {
    orderDetail.value = data.value
    isShowedDetail.value = true
  }
}

async function selectPage(newPage: number) {
  pageOrder.value = newPage
  await getOrderList({ page: newPage })
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
      <UTable :columns="orderTableCols" :rows="orderList" :ui="{ td: { base: 'max-w-[200px] whitespace-normal' } }">
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

        <template #actions-data="{ row }">
          <div class="max-w-[100px] flex gap-3">
            <UButton label="Detail" icon="i-ph-magnifying-glass" @click="getOrderDetail(row.id)" />
            <UModal :modelValue="isShowedDetail" prevent-close :transition="false">
              <div class="p-5">
                <div class="text-center text-2xl font-bold">Order detail</div>
                <div v-if="orderDetail" class="my-5 flex flex-col gap-3">
                  <div>Customer name: {{ `${orderDetail.fname} ${orderDetail.lname}` }}</div>
                  <div>Country: {{ orderDetail.country }}</div>
                  <div>City: {{ orderDetail.city }}</div>
                  <div>State/Province: {{ orderDetail.state }}</div>
                  <div>Street Address: {{ orderDetail.street_address }}</div>
                  <div>Zip/Postal Code: {{ orderDetail.zip_code }}</div>
                  <div>
                    <span class="font-bold">Items:</span>
                    <ol class="list-decimal pl-5">
                      <li v-for="item, i in orderDetail.items" :key="i">
                        Collection: <span>{{ item.collection }}</span>
                        - Color: <span>{{ item.name }}</span>
                        - Size: <span>{{ item.size }}</span>
                        - Quantity: <span>{{ item.quantity }}</span>
                      </li>
                    </ol>
                  </div>

                </div>
                <div>
                  <UButton label="Close" @click="isShowedDetail = false" />
                </div>
              </div>
            </UModal>
          </div>
        </template>
      </UTable>
      <UPagination :model-value="pageOrder" @update:model-value="(newPage: number) => selectPage(newPage)"
        :page-count="10" :total="totalOrder" />
    </div>
  </div>
</template>
