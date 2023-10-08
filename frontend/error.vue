<script setup lang="ts">
const props = defineProps({
  error: Object
})

</script>


<template>
  <div class="h-screen flex flex-col">
    <LayoutHeader :is-show-bottom-line="true" />
    <div class="flex-1 mycontainer mx-auto flex flex-col gap-3 items-center justify-center">
      <template v-if="error!.statusCode === 404">
        <span class="error-text">404</span>
        <div class="text-xl sm:text-2xl lg:text-3xl">SORRY, PAGE NOT FOUND</div>
      </template>
      <template v-else>
        <span class="error-text">Error</span>
        <div class="text-xl sm:text-2xl lg:text-3xl">SORRY, SOMETHING WRONG HAPPEN</div>
      </template>
      <div>
        <UButton @click="$router.back()" label="GO BACK" variant="outline" color="black"
          :ui="{ rounded: '', base: 'w-[300px] h-[60px] flex justify-center' }" />
      </div>
    </div>
  </div>
</template>


<style scoped>
.error-text {
  font-size: 150px;
  line-height: 1;
}

@media screen and (min-width:480px) {
  .error-text {
    font-size: 200px;
  }
}

@media screen and (min-width:768px) {
  .error-text {
    font-size: 300px;
  }
}
</style>