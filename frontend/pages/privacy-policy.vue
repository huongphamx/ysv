<script setup lang="ts">
const isShowedHeaderLine = useIsShowedHeaderLine()
isShowedHeaderLine.value = true

useHead({
  title: 'Privacy policy - YSV'
})
</script>

<template>
  <div class="mycontainer mx-auto">
    <div class="privacy-body mx-auto">
      <div class="text-medium text-center mb-10">Privacy Policy</div>
      <p class="text-center">At YSV, we value your privacy and are committed to protecting your personal information. This
        Privacy Policy outlines how we collect, use, and safeguard your data. By using our website, you consent to the
        practices described in this policy.
      </p>
      <br>
      <div class="">
        <div class="privacy-head">Information We Collect</div>
        <ul class="list-disc px-5 md:px-10">
          <li><span class="font-bold">Personal Information:</span> When you make a purchase or create an account, we may
            collect your name, email address,
            shipping address, and payment details.</li>
          <li><span class="font-bold">Usage Information:</span> We gather data on how you interact with our website,
            including your IP address, browser
            type,
            and device information.</li>
          <li><span class="font-bold">Cookies:</span> We use cookies and similar technologies to enhance your browsing
            experience and collect information
            about your preferences.</li>
        </ul>
      </div>
      <br>
      <div class="">
        <div class="privacy-head">How We Use Your Information</div>
        <ul class="list-disc px-5 md:px-10">
          <li><span class="font-bold">To Process Orders:</span> We use your personal information to fulfill your orders
            and
            provide customer support.</li>
          <li><span class="font-bold">To Improve Our Services:</span> We analyze usage data to enhance our website,
            products, and services.</li>
          <li><span class="font-bold">Marketing Communications:</span> With your consent, we may send promotional emails
            and
            updates about our products.
          </li>
        </ul>
      </div>
      <br>
      <div class="">
        <div class="privacy-head">Sharing Your Information</div>
        <ul class="list-disc px-5 md:px-10">
          <li><span class="font-bold">Third-Party Services:</span> We may share data with trusted service providers to
            process payments and perform
            essential functions.</li>
          <li><span class="font-bold">Legal Requirements:</span> We may disclose your information if required by law or to
            protect our rights and the
            safety of others.</li>
        </ul>
      </div>
      <br>
      <div class="">
        <div class="privacy-head">Your Choices</div>
        <ul class="list-disc px-5 md:px-10">
          <li><span class="font-bold">Marketing Preferences:</span> You can opt out of marketing communications by
            following
            the unsubscribe instructions
            in our emails.</li>
        </ul>
      </div>
      <br>
      <div class="">
        <div class="privacy-head">Data Security</div>
        <div class="text-center">We implement security measures to protect your information, but no method is entirely
          foolproof. Please ensure
          your account information is kept secure.</div>
      </div>
      <br>
      <div class="">
        <div class="privacy-head">Changes to this Policy</div>
        <div class="text-center">We may update this Privacy Policy to reflect changes in our practices. Check this page
          for
          the latest
          information.</div>
      </div>
      <br>
      <div class="">
        <div class="privacy-head">Contact Us</div>
        <div class="text-center">If you have questions or concerns about our Privacy Policy, please contact us at
          ysv.shukshina@gmail.com.</div>
      </div>
      <br>
    </div>
  </div>
</template>


<style scoped>
.privacy-body {
  width: 100%;
  max-width: 280px;
  font-size: 14px;
  margin-top: 50px;
  margin-bottom: 50px;

  @media screen and (min-width: 480px) {
    max-width: 400px;
    margin-bottom: 80px;
  }

  @media screen and (min-width: 768px) {
    max-width: 600px;
    font-size: 16px;
    margin-bottom: 100px;
  }

  @media screen and (min-width: 1280px) {
    max-width: 800px;
    font-size: 18px;
    margin-bottom: 150px;
  }
}

.privacy-head {
  text-align: center;
  text-transform: uppercase;
  font-size: 18px;
  margin-bottom: 10px;

  @media screen and (min-width: 768px) {
    font-size: 20px;
  }

  @media screen and (min-width: 1280px) {
    font-size: 22px;
  }
}
</style>