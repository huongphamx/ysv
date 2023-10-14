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
      timeout: 2000,
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
    <div class="btn-add-to-cart" @click="addToCart">
      ADD TO CART
      <UIcon name="i-iconamoon-arrow-bottom-right-1" class="text-2xl" />
    </div>
    <div class="underline text-gray-500 text-sm md:text-base">
      <a href="https://api.whatsapp.com/send?phone=971545602477" target="_blank">CONTACT VIA WHATSAPP</a>
    </div>
  </div>
</template>


<style scoped>
.btn-add-to-cart {
  margin-bottom: 10px;
  width: 200px;
  height: 40px;
  background-color: var(--black);
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;

  &:hover {
    cursor: pointer;
  }

  @media screen and (min-width: 768px) {
    width: 304px;
    height: 50px;
  }
}
</style>
