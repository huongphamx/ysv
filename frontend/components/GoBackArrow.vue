<template>
  <div class="main text-gray-500" @click="$router.back()">
    <UIcon name="i-iconamoon-arrow-top-left-1-light" class="text-2xl" /><span>GO BACK</span>
  </div>
</template>


<style scoped>
.main {
  display: none;

  @media screen and (min-width: 1280px) {
    margin-top: 32px;
    display: flex;
    align-items: center;
    gap: 0.5rem;

    &:hover {
      cursor: pointer;
    }
  }
}
</style>