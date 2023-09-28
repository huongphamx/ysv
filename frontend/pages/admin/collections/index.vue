<script setup lang="ts">

</script>


<template>
  <div>
    <div class="text-2xl font-bold">Collections</div>
    <div class="my-2 flex gap-5">
      <div class="flex">
        <UInput placeholder="Search Collection" />
        <UButton icon="i-ph-magnifying-glass" />
      </div>
      <UButton label="Add Collection" icon="i-ph-plus" to="/admin/collections/create" />
    </div>
  </div>
</template>

