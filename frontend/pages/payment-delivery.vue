<script lang="ts" setup>
const isShowedHeaderLine = useIsShowedHeaderLine()
isShowedHeaderLine.value = true

useHead({
  title: 'Payment & Delivery - YSV'
})
</script>


<template>
  <div class="delivery-body mycontainer mx-auto">
    <GoBackArrow />
    <div class="delivery-main">
      <img src="/img/delivery-02.webp" class="delivery-hero-image" v-motion="slideVisibleOnceRightMotion">
      <div class="xl:max-w-[412px]">
        <img src="/img/delivery-01.webp" class="delivery-sub-hero-image" v-motion="slideVisibleOnceLeftMotion">
        <div class="mt-[30px] md:mt-0 xl:mt-[30px] text-medium" v-motion="slideVisibleOnceBottomMotion">DELIVERY/SHIPPING
        </div>
        <div class="mt-1 text-small uppercase delivery-description" v-motion="slideVisibleOnceBottomMotion">
          <p>After “placing an order” we will contact you within 24 hours.</p><br>
          <p>Delivery shipping in UAE within 1-3 days starts from 4 $ TO 15 $</p><br>
          <p>Worldwide shipping starts from 54 $ depending on your country and Delivery company. Delivery time up to 10-15
            days. </p><br>
          <p>It is possible to pay by Cryptocurrency.</p>
        </div>
      </div>
    </div>
  </div>
</template>


<style scoped>
.delivery-body {
  margin-bottom: 50px;

  @media screen and (min-width: 480px) {
    margin-bottom: 80px;
  }

  @media screen and (min-width: 768px) {
    margin-top: 50px;
    margin-bottom: 100px;
  }

  @media screen and (min-width: 1280px) {
    margin-bottom: 150px;
  }
}

.delivery-main {
  @media screen and (min-width: 768px) {
    display: flex;
    flex-direction: row-reverse;
    gap: 1rem;
  }

  @media screen and (min-width: 1276px) {
    gap: 1.25rem;
  }
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
  margin-top: 15px;
  width: 300px;

  @media screen and (min-width: 480px) {
    margin-top: 20px;
    width: 359px;
  }

  @media screen and (min-width: 768px) {
    width: 299px;
  }

  @media screen and (min-width: 1278px) {
    width: 369px;
  }
}
</style>
