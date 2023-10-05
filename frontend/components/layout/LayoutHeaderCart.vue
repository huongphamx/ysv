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
  <UPopover mode="hover" :ui="{ rounded: '' }">
    <UButton icon="i-ph-shopping-cart" color="black" variant="ghost" :ui="{ icon: { size: { sm: 'h-6 w-6' } } }" />

    <template #panel>
      <template v-if="cart.length > 0">
        <CustomerBag />
        <div class="p-3">
          <UButton label="GO TO CHECKOUT" block color="black" :ui="{ rounded: '' }" to="/checkout" />
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