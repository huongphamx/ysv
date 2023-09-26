<script lang="ts" setup>

</script>


<template>
  <div class="h-screen flex flex-col">
    <LayoutHeader />
    <div class="flex-1">
      <slot />
    </div>
    <LayoutFooter />
  </div>
</template>

