<script lang="ts" setup>
definePageMeta({
  layout: 'admin',
  middleware: 'admin',
  pageTransition: false,
})
</script>


<template>
  <div class="h-screen overflow-auto p-5">
    <NuxtPage />
  </div>
</template>
