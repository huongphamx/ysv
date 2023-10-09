<script lang="ts" setup>
definePageMeta({
  layout: 'default-line-header',
})

useHead({
  title: 'Payment & Delivery - YSV'
})
</script>


<template>
  <GoBackArrow />
  <div class="mt-5 delivery-main">
    <img src="/img/delivery-02.webp" class="delivery-hero-image">
    <div class="xl:max-w-[412px]">
      <img src="/img/delivery-01.webp" class="delivery-sub-hero-image">
      <div class="mt-[30px] md:mt-0 xl:mt-[20px] text-medium">DELIVERY/SHIPPING</div>
      <div class="mt-1 mb-10 text-small uppercase delivery-description">
        <p>After “placing an order” we will contact you within 24 hours.</p>
        <p>Delivery shipping in UAE within 1-3 days starts from 4 $ -15 $</p>
        <p>Worldwide shipping starts from 54 $ depending on your country and Delivery company. Delivery time up to 10-15
          days. </p>
        <p>It is possible to pay by Cryptocurrency.</p>
      </div>
    </div>
  </div>
</template>


<style scoped>
.delivery-main {
  @media screen and (min-width: 768px) {
    display: flex;
    flex-direction: row-reverse;
    gap: 1rem;
  }

  @media screen and (min-width: 1276px) {}
}

.delivery-hero-image {
  width: 300px;
  height: 400px;
  object-fit: cover;

  @media screen and (min-width: 480px) {
    width: 420px;
    height: 400px;
  }

  @media screen and (min-width: 768px) {
    width: 300px;
    height: 400px;
  }

  @media screen and (min-width: 1280px) {
    width: 736px;
    height: 1040px;
  }
}

.delivery-sub-hero-image {
  display: none;

  @media screen and (min-width: 1280px) {
    display: unset;
    width: 412px;
    height: 600px;
  }
}

.delivery-description {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  margin-bottom: 40px;

  @media screen and (min-width: 480px) {
    gap: 1.5rem;
    margin-bottom: 80px;
  }
}
</style>
