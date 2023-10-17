<script setup lang="ts">
const isShowedHeaderLine = useIsShowedHeaderLine()
isShowedHeaderLine.value = true

useHead({
  title: 'Payment cancel - YSV'
})
</script>


<template>
  <div class="page-body mycontainer mx-auto flex flex-col gap-5 items-center justify-center">
    <div>
      <UIcon name="i-ph-x-circle" class="text-6xl text-red-500" />
    </div>
    <div class="text-lg md:text-3xl 2xl:text-4xl">
      PAYMENT CANCELED
    </div>
    <div class="text-base md:text-lg 2xl:text-xl">SOMETHING WENT WRONG, PLEASE TRY AGAIN</div>
    <NuxtLink to="/">
      <div class="go-back-btn">GO HOME</div>
    </NuxtLink>
  </div>
</template>


<style scoped>
.page-body {
  margin-top: 70px;
  margin-bottom: 150px;

  @media screen and (min-width: 480px) {
    margin-top: 135px;
    margin-bottom: 155px;
  }

  @media screen and (min-width: 768px) {
    margin-top: 93px;
  }

  @media screen and (min-width: 1000px) {
    margin-bottom: 135px;
  }

  @media screen and (min-width: 1280px) {
    margin-top: 150px;
  }
}

.go-back-btn {
  width: 140px;
  height: 50px;
  margin-top: 30px;
  border: 1px solid;
  display: flex;
  justify-content: center;
  align-items: center;

  &:hover {
    background-color: var(--black);
    color: white;
  }

  @media screen and (min-width: 480px) {
    width: 200px;
    height: 60px;
  }

  @media screen and (min-width: 768px) {
    width: 300px;
    height: 70px;
    border: 2px solid;
    font-size: 18px;
  }

  @media screen and (min-width: 1280px) {
    width: 412px;
    font-size: 20px;
  }
}
</style>
