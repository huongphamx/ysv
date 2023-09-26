<script lang="ts" setup>
definePageMeta({
  layout: 'admin',
})
</script>


<template>
  <div class="h-screen p-5 bg-gray-50">
    <div class="text-2xl font-bold">Collections</div>
    <div class="my-2 flex gap-5">
      <div class="flex">
        <UInput placeholder="Search Collection" />
        <UButton icon="i-ph-magnifying-glass" />
      </div>
      <UButton label="Add Collection" icon="i-ph-plus" />
    </div>
  </div>
</template>
