<script lang="ts" setup>
const links = [{
  label: 'Collections',
  icon: 'i-ph-books',
  to: '/admin/collections'
}, {
  label: 'Products',
  icon: 'i-ph-dress',
  to: '/admin/products'
}, {
  label: 'Orders',
  icon: 'i-ph-basket',
  to: '/admin/orders'
}, {
  label: 'Home site',
  icon: 'i-ph-house',
  to: '/admin/home-site'
}, {
  label: 'Event site',
  icon: 'i-ph-clock',
  to: '/admin/event-site'
},]
</script>


<template>
  <div class="p-2 border-r border-gray-500">
    <div class="h-20 text-4xl flex justify-center items-center">YSV</div>
    <UVerticalNavigation :links="links"
      :ui="{ padding: 'px-5 py-3', size: 'text-md', font: '', icon: { base: 'w-6 h-6' } }" />
  </div>
</template>

