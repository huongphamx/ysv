<script setup lang="ts">
import { v4 as uuidv4 } from 'uuid'
import { useWindowSize } from '@vueuse/core'

const { width, height } = useWindowSize()

const cart = useCart()
const cartIdCookie = useCartIdCookie()

if (cartIdCookie.value) {
  getCartItems()
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
  <UPopover :mode="width > 1280 ? 'hover' : 'click'" :ui="{ rounded: '', ring: 'ring-black' }">
    <IconCart />

    <template #panel>
      <template v-if="cart && cart.length > 0">
        <CustomerBag />
        <NuxtLink to="/checkout">
          <div class="p-3">
            <div class="go-to-checkout-btn">GO TO CHECKOUT</div>
          </div>
        </NuxtLink>
      </template>
      <template v-else>
        <div class="p-3">
          <div class="text-lg font-['Italiana']">YOUR BAG ({{ cart.length }})</div>
          You don't have any item in bag!
        </div>
      </template>
    </template>
  </UPopover>
</template>


<style scoped>
.go-to-checkout-btn {
  width: 100%;
  height: 46px;
  background-color: var(--black);
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;

  &:hover {
    cursor: pointer;
    background-color: var(--gray);
  }
}
</style>
