<script lang="ts" setup>
definePageMeta({
  layout: 'admin',
  middleware: 'admin',
  pageTransition: false,
})
</script>


<template>
  <div class="h-screen p-5 overflow-auto">
    <NuxtPage />
  </div>
</template>
