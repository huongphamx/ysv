<script lang="ts" setup>
const links = [{
  label: 'Statistics',
  icon: 'i-ph-chart-pie',
  to: '/admin/statistics'
}, {
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
}]
</script>


<template>
  <div class="p-2 bg-gray-300 border-r">
    <div class="h-20 text-4xl flex justify-center items-center">YSV</div>
    <UVerticalNavigation :links="links"
      :ui="{ padding: 'px-5 py-3', size: 'text-md', font: '', icon: { base: 'w-6 h-6' } }" />
  </div>
</template>

