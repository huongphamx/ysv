<script setup lang="ts">
import { useConfirmDialog } from '@vueuse/core'

const props = defineProps({
  border: {
    type: Boolean,
    default: false,
  },
  title: {
    type: String,
    default: 'YOUR BAG',
  }
})

const cart = useCart()
const cartIdCookie = useCartIdCookie()

const totalPrice = computed(() => {
  let total = 0
  for (const item of cart.value) {
    total += item.price * item.quantity
  }
  return total
})

async function increaseCartItem(itemId: string) {
  const { error } = await useCustomFetch(`/v1/carts/${cartIdCookie.value}`, {
    method: 'put',
    body: { action: 'increase_item', item_id: itemId }
  })
  if (!error.value) {
    await getCartItems()
  }
}
async function decreaseCartItem(itemId: string) {
  const { error } = await useCustomFetch(`/v1/carts/${cartIdCookie.value}`, {
    method: 'put',
    body: { action: 'decrease_item', item_id: itemId }
  })
  if (!error.value) {
    await getCartItems()
  }
}
async function deleteCartItem(itemId: string) {
  const { error } = await useCustomFetch(`/v1/carts/${cartIdCookie.value}`, {
    method: 'put',
    body: { action: 'delete_item', item_id: itemId }
  })
  if (!error.value) {
    await getCartItems()
  }
}
</script>


<template>
  <div class="p-3 max-h-[600px] overflow-auto text-black" :class="{ 'border border-black': border }">
    <div class="text-lg font-['Italiana']"><span>{{ title }}</span> ({{ cart.length }})</div>
    <div class="divide-y">
      <div v-for="item in cart" :key="item.id" class="flex py-4">
        <img :src="item.preview_pic" alt="" class="w-[66px] h-[84px] object-cover">
        <div class="ml-4">
          <NuxtLink :to="`/p/${item.product_id}`" class="hover:underline">
            <div class="flex text-[13px] font-bold uppercase w-[200px]" :class="border ? 'sm:w-[300px]' : ''">
              <div>{{ item.collection }} collection</div>
              <div class="ml-auto">${{ item.price }}</div>
            </div>
            <div class="text-[11px] text-gray-500">COLOR: {{ item.color.toUpperCase() }}</div>
            <div class="text-[11px] text-gray-500">SIZE: {{ item.size }}</div>
          </NuxtLink>
          <div class="flex items-center">
            <UButton icon="i-ph-minus" size="xs" color="black" :ui="{ rounded: '' }" @click="decreaseCartItem(item.id)" />
            <span class="mx-2">{{ item.quantity }}</span>
            <UButton icon="i-ph-plus" size="xs" color="black" :ui="{ rounded: '' }" @click="increaseCartItem(item.id)" />
            <UButton icon="i-ph-trash" size="xs" variant="outline" color="black" :ui="{ rounded: '' }" class="ml-auto"
              @click="deleteCartItem(item.id)" />
          </div>
        </div>
      </div>
    </div>

    <div class="border-t py-4">
      <div class="flex"><span>TOTAL:</span> <span class="ml-auto">${{ totalPrice }}</span></div>
      <!-- <div class="mt-1 text-gray-500 flex"><span>SHIPPING</span> <span class="ml-auto">FREE</span></div> -->
    </div>
  </div>
</template>
