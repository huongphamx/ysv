<script lang="ts" setup>
</script>


<template>
  <div>
    <div class="text-2xl font-bold">Products</div>
    <div class="my-2 flex gap-5">
      <div class="flex">
        <UInput placeholder="Search Product" />
        <UButton icon="i-ph-magnifying-glass" />
      </div>
      <UButton label="Add Product" icon="i-ph-plus" to="/admin/products/create" />
    </div>
  </div>
</template>
