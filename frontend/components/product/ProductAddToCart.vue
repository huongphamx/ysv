<script setup lang="ts">
const selectedProductVariant = useSelectedProductVariant()
const cartIdCookie = useCartIdCookie()

const addToCart = async () => {
  const { data: addItemSuccess, error } = await useCustomFetch(`/v1/carts/${cartIdCookie.value}`, {
    method: 'post',
    body: { product_size_variant_id: selectedProductVariant.value?.id }
  })
  if (addItemSuccess.value) {
    await getCartItems()
  }
}
</script>

<template>
  <div>
    <div class="my-4 flex items-center gap-5">
      <UButton label="ADD TO CART" trailing-icon="i-ph-arrow-down-right" color="black"
        :ui="{ rounded: '', padding: { 'sm': 'px-16 py-4' } }" @click="addToCart" />
    </div>
    <div class="mb-5 underline text-gray-500 text-sm md:text-base"><a href="https://whatsapp.com" target="_blank">CONTACT
        VIA
        WHATSAPP</a></div>
  </div>
</template>

