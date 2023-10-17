<script lang="ts" setup>
const isShowedHeaderLine = useIsShowedHeaderLine()
isShowedHeaderLine.value = true

const config = useRuntimeConfig()
const cloudfrontDistributionDomain = config.public.cloudfrontDistributionDomain

useHead({
  title: 'Payment & Delivery - YSV'
})
</script>


<template>
  <div class=" mycontainer mx-auto">
    <GoBackArrow />
    <div class="delivery-body">
      <div class="delivery-main">
        <img :src="`${cloudfrontDistributionDomain}/img/delivery-01.webp`" alt="" v-motion="slideVisibleOnceMotion"
          class="delivery-hero-image">
        <div class="description">
          <div class="text-medium" v-motion="slideVisibleOnceBottomMotion">DELIVERY/SHIPPING
          </div>
          <div class="text-small" v-motion="slideVisibleOnceBottomMotion">
            <p>After “placing an order” we will contact you within 24 hours.</p><br>
            <p>Delivery shipping in UAE within 1-3 days is 20$</p><br>
            <p>Worldwide Shipping within 8-12 Days is 50$.</p><br>
            <p>It is possible to pay by Cryptocurrency.</p>
          </div>
        </div>
      </div>
      <img :src="`${cloudfrontDistributionDomain}/img/delivery-02.webp`" alt="" class="delivery-sub-hero"
        v-motion="slideVisibleOnceRightMotion">
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
    margin-bottom: 100px;
  }

  @media screen and (min-width: 1280px) {
    margin-bottom: 150px;
    display: flex;
  }
}

.delivery-main {
  @media screen and (min-width: 768px) {
    display: flex;
    flex-direction: row-reverse;
  }

  @media screen and (min-width: 1280px) {
    display: block;
    margin-left: auto;
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
    width: 412px;
    height: 600px;
  }
}

.description {
  margin-top: 20px;

  .text-small {
    margin-top: 15px;

    @media screen and (min-width: 480px) {
      margin-top: 20px;
    }
  }

  @media screen and (min-width: 768px) {
    width: 300px;
    margin-right: 20px;
    margin-top: 0;
  }

  @media screen and (min-width: 1280px) {
    width: 370px;
    margin-top: 30px;
    margin-right: 0;
  }
}

.delivery-sub-hero {
  display: none;

  @media screen and (min-width:1280px) {
    display: block;
    width: 736px;
    height: 1040px;
    margin-left: 20px;
  }
}
</style>
