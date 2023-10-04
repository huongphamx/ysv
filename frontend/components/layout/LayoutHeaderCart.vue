<script setup lang="ts">
import { CartItem } from '@/types'

const cart = useCart()
const cartItemIds = useCartItemIdsCookie()
const itemIds = cartItemIds.value.map(i => i.id)

const { data, error } = await useCustomFetch<CartItem[]>(`/v1/cart/items/`, { params: { ids: itemIds } })
cart.value = data.value!.map(item => {
  item.quantity = cartItemIds.value.find(i => i.id === item.id)?.quantity!
  return item
})

// todo: handle add/remove button
</script>

<template>
  <UPopover :ui="{ rounded: '' }">
    <UButton icon="i-ph-shopping-cart" color="black" variant="ghost" :ui="{ icon: { size: { sm: 'h-6 w-6' } } }" />

    <template #panel>
      <template v-if="cart.length > 0">
        <div class="p-3 max-h-[600px] overflow-auto text-black">
          <div class="text-lg font-['Italiana']">YOUR BAG ({{ cart.length }})</div>
          <div class="divide-y">
            <div v-for="item in cart" :key="item.id" class="flex py-4">
              <img :src="item.preview_pic" alt="" class="w-[66px] h-[84px] object-cover">
              <div class="ml-4">
                <div class="flex text-[13px] font-bold max-w-[230px]">
                  <div>{{ item.collection }}</div>
                  <div class="ml-3">${{ item.price }}</div>
                </div>
                <div class="text-[11px] text-gray-500">COLOR: {{ item.color.toUpperCase() }}</div>
                <div class="text-[11px] text-gray-500">SIZE: {{ item.size }}</div>
                <div class="flex items-center">
                  <UButton icon="i-ph-minus" size="xs" color="black" :ui="{ rounded: '' }" />
                  <span class="mx-2">{{ item.quantity }}</span>
                  <UButton icon="i-ph-plus" size="xs" color="black" :ui="{ rounded: '' }" />
                  <UButton icon="i-ph-trash" size="xs" variant="outline" color="black" :ui="{ rounded: '' }"
                    class="ml-auto" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </template>
      <template v-else>
        <div class="p-3 text-black">
          <div class="text-lg font-['Italiana']">YOUR BAG ({{ cart.length }})</div>
          You don't have any item in bag!
        </div>
      </template>
    </template>
  </UPopover>
</template>