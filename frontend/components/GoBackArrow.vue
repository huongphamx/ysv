<template>
  <div class="my-10 w-fit group" @click="$router.back()">
    <div class="goback-body">
      <UIcon name="i-iconamoon-arrow-top-left-1-light" class="text-2xl" /><span>GO BACK</span>
    </div>
    <div class="-mt-0.5 ml-1 h-[1px] bg-[var(--gray)] hidden group-hover:block"></div>
  </div>
</template>


<style scoped>
.goback-body {
  color: var(--gray);
  display: none;

  @media screen and (min-width: 1280px) {
    width: fit-content;
    display: flex;
    align-items: center;
    column-gap: 0.5rem;

    &:hover {
      cursor: pointer;
    }
  }
}
</style>