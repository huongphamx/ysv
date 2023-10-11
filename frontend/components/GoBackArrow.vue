<template>
  <div class="goback-body text-gray-500" @click="$router.back()">
    <UIcon name="i-iconamoon-arrow-top-left-1-light" class="text-2xl" /><span>GO BACK</span>
  </div>
</template>


<style scoped>
.goback-body {
  display: none;

  @media screen and (min-width: 1280px) {
    width: fit-content;
    margin-top: 40px;
    margin-bottom: 40px;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    border-bottom: 1px solid transparent;

    &:hover {
      cursor: pointer;
      border-bottom: 1px solid;
    }
  }
}
</style>