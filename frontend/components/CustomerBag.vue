<script setup lang="ts">
const props = defineProps({
  border: {
    type: Boolean,
    default: false,
  },
  title: {
    type: String,
    default: 'YOUR BAG',
  }
})

const cart = useCart()

const totalPrice = computed(() => {
  let total = 0
  for (const item of cart.value) {
    total += item.price * item.quantity
  }
  return total
})


</script>


<template>
  <div class="p-3 max-h-[600px] overflow-auto text-black" :class="{ 'border border-black': border }">
    <div class="text-lg font-['Italiana']"><span>{{ title }}</span> ({{ cart.length }})</div>
    <div class="divide-y">
      <div v-for="item in cart" :key="item.id" class="flex py-4">
        <img :src="item.preview_pic" alt="" class="w-[66px] h-[84px] object-cover">
        <div class="ml-4">
          <NuxtLink :to="`/${item.product_id}`" class="hover:underline">
            <div class="flex text-[13px] font-bold">
              <div>{{ item.collection }}</div>
              <div class="ml-3">${{ item.price }}</div>
            </div>
            <div class="text-[11px] text-gray-500">COLOR: {{ item.color.toUpperCase() }}</div>
            <div class="text-[11px] text-gray-500">SIZE: {{ item.size }}</div>
          </NuxtLink>
          <div class="flex items-center">
            <UButton icon="i-ph-minus" size="xs" color="black" :ui="{ rounded: '' }" />
            <span class="mx-2">{{ item.quantity }}</span>
            <UButton icon="i-ph-plus" size="xs" color="black" :ui="{ rounded: '' }" />
            <UButton icon="i-ph-trash" size="xs" variant="outline" color="black" :ui="{ rounded: '' }" class="ml-auto" />
          </div>
        </div>
      </div>
    </div>

    <div class="border-t py-4">
      <div class="flex"><span>TOTAL:</span> <span class="ml-auto">${{ totalPrice }}</span></div>
      <!-- <div class="mt-1 text-gray-500 flex"><span>SHIPPING</span> <span class="ml-auto">FREE</span></div> -->
    </div>
  </div>
</template>
