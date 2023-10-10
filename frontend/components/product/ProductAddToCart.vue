<script setup lang="ts">
const toast = useToast()

const selectedProductVariant = useSelectedProductVariant()
const cartIdCookie = useCartIdCookie()

const addToCart = async () => {
  if (!selectedProductVariant.value) {
    toast.add({
      description: 'Please select a size ',
      icon: 'i-ph-warning-circle',
      timeout: 5000,
      closeButton: { icon: '' },
      ui: {
        title: 'text-white',
        description: 'text-white text-lg',
        background: 'bg-black opacity-80',
        icon: { color: 'text-white', base: 'w-10 h-10' },
        progress: { base: 'h-0' }
      }
    })
    return
  }
  const { data: addItemSuccess, error } = await useCustomFetch(`/v1/carts/${cartIdCookie.value}`, {
    method: 'post',
    body: { product_size_variant_id: selectedProductVariant.value?.id }
  })
  if (addItemSuccess.value) {
    toast.add({
      description: 'Product added to cart',
      icon: 'i-ph-check-circle',
      timeout: 5000,
      closeButton: { icon: '' },
      ui: {
        title: 'text-white',
        description: 'text-white text-lg',
        background: 'bg-black opacity-80',
        icon: { color: 'text-green-500', base: 'w-10 h-10' },
        progress: { base: 'h-0' }
      }
    })
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
    <div class="mb-5 underline text-gray-500 text-sm md:text-base">
      <a href="https://api.whatsapp.com/send?phone=971545602477" target="_blank">CONTACT VIA WHATSAPP</a>
    </div>
  </div>
</template>

