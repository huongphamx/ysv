<script lang="ts" setup>
getCollectionList()
</script>


<template>
  <div class="h-screen flex flex-col">
    <LayoutHeader />
    <div class="flex-1 mycontainer mx-auto">
      <slot />
    </div>
    <LayoutFooter />
  </div>
</template>

