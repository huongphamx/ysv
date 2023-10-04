<script setup lang="ts">
const selectedProductVariant = useSelectedProductVariant()
const cartItemIds = useCartItemIdsCookie()
const cart = useCart()

const addToCart = () => {
  const existingItemIds = cartItemIds.value.map(i => i.id)
  if (existingItemIds.includes(selectedProductVariant.value?.id!)) {
    cartItemIds.value = cartItemIds.value.map(item => {
      if (item.id === selectedProductVariant.value?.id) {
        item.quantity += 1
      }
      return item
    })
    // todo: update cart item quantify
  } else {
    cartItemIds.value.push({ id: selectedProductVariant.value?.id!, quantity: 1 })
    // todo: get item detail from api and add to cart
  }
}
</script>

<template>
  <div class="my-4 flex items-center gap-5">
    <UButton label="ADD TO CART" trailing-icon="i-ph-arrow-down-right" color="black"
      :ui="{ rounded: '', padding: { 'sm': 'px-16' } }" :disabled="selectedProductVariant === null" @click="addToCart" />
    <!-- <UButton icon="i-ph-heart" color="gray" :ui="{ rounded: '' }" /> -->
    <span v-if="selectedProductVariant === null" class="text-gray-500">Select a size</span>
  </div>
  <div class="underline text-gray-500"><a href="https://whatsapp.com" target="_blank">CONTACT VIA WHATSAPP</a></div>
</template>

