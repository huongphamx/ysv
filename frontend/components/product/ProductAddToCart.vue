<script setup lang="ts">
import { useCurrentProduct } from '~/composables/product';

const selectedProductVariant = useSelectedProductVariant()
const cartVariantIds = useCartVariantIdsCookie()
const cart = useCart()
const currentProduct = useCurrentProduct()

const addToCart = () => {
  cart.value.push(
    {
      product_variant_id: selectedProductVariant.value?.id!,
      collection_name: currentProduct.value?.collection.name!,
      product_variant_name: currentProduct.value?.name!,
      product_variant_size: selectedProductVariant.value?.size!,
      product_preview_pic: currentProduct.value?.preview_pic!,
      product_price: currentProduct.value?.price!,
    }
  )
  cartVariantIds.value.push({ id: selectedProductVariant.value?.id!, quantity: 1 })
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

