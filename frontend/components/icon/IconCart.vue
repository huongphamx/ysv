<script setup lang="ts">
const cart = useCart()
const route = useRoute()
const isShowedMobileMenu = useIsShowedMobileMenu()
const strokeColor = computed(() => {
  return route.path === '/' && !isShowedMobileMenu.value ? 'white' : 'black'
})
</script>

<template>
  <div class="relative">
    <svg width="98" height="106" viewBox="0 0 98 106" xmlns="http://www.w3.org/2000/svg" class="cart-icon">
      <path
        d="M67.2971 30.6033C67.2971 40.9025 58.9383 49.2614 48.639 49.2614C38.3398 49.2614 29.981 40.9025 29.981 30.6033V23.1401C29.981 21.0877 28.3018 19.4085 26.2494 19.4085C24.197 19.4085 22.5178 21.0877 22.5178 23.1401V30.6033C22.5178 45.0446 34.1977 56.7246 48.639 56.7246C63.0804 56.7246 74.7603 45.0446 74.7603 30.6033V23.1401C74.7603 21.0877 73.0811 19.4085 71.0287 19.4085C68.9763 19.4085 67.2971 21.0877 67.2971 23.1401V30.6033Z"
        :fill="strokeColor" />
      <path fill-rule="evenodd" clip-rule="evenodd"
        d="M97.15 86.5775V19.4085C97.15 9.10921 88.7912 0.750397 78.4919 0.750397H18.7861C8.48689 0.750397 0.128082 9.10921 0.128082 19.4085V86.5775C0.128082 96.8767 8.48689 105.236 18.7861 105.236H78.4919C88.7912 105.236 97.15 96.8767 97.15 86.5775ZM89.6868 19.4085V86.5775C89.6868 92.772 84.6864 97.7723 78.4919 97.7723H18.7861C12.5917 97.7723 7.59131 92.772 7.59131 86.5775V19.4085C7.59131 13.214 12.5917 8.21362 18.7861 8.21362H78.4919C84.6864 8.21362 89.6868 13.214 89.6868 19.4085Z"
        :fill="strokeColor" />
    </svg>
    <div v-if="cart.length > 0" class="absolute bottom-0 right-0 rounded-full w-2 h-2 bg-red-500 ring-2 ring-black"></div>
  </div>
</template>


<style scoped>
.cart-icon {
  height: 25px;
  width: 25px;
  fill: none;
}
</style>