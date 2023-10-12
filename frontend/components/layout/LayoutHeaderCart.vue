<script setup lang="ts">
import { v4 as uuidv4 } from 'uuid'
import { useWindowSize } from '@vueuse/core'

const { width, height } = useWindowSize()

const cart = useCart()
const cartIdCookie = useCartIdCookie()

if (cartIdCookie.value) {
  await getCartItems()
} else {
  const cartId = uuidv4()
  const { data, error } = await useCustomFetch('/v1/carts/', {
    method: 'post',
    body: { cart_id: cartId }
  })
  if (error.value) {
    // todo: toast
  } else if (data.value) {
    cartIdCookie.value = cartId
  }
}
const isShowedMobileMenu = useIsShowedMobileMenu()
</script>

<template>
  <UPopover :mode="width > 1280 ? 'hover' : 'click'" :ui="{ rounded: '' }">
    <!-- <UButton icon="i-ph-shopping-cart" color="black" variant="ghost" :ui="{ icon: { size: { sm: 'h-6 w-6' } } }" /> -->
    <IconCart />
    <!-- <IconCartFilled v-else class="w-10 h-10" /> -->

    <template #panel>
      <template v-if="cart.length > 0">
        <CustomerBag />
        <div class="p-3">
          <UButton label="GO TO CHECKOUT" block color="black" :ui="{ rounded: '' }" to="/checkout"
            @click="isShowedMobileMenu = false" />
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
