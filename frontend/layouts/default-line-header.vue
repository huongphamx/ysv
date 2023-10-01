<script lang="ts" setup>
getCollectionList()
</script>


<template>
  <div class="h-screen flex flex-col">
    <LayoutHeader :is-show-bottom-line="true" />
    <div class="flex-1">
      <slot />
    </div>
    <LayoutFooter />
  </div>
</template>

