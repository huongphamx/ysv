<script setup lang="ts">
import { object, string, number } from 'yup'
import { countriesCode } from '@/countries'

const currentStep = ref(1)

const cart = useCart()
const cartIdCookie = useCartIdCookie()

const checkoutForm = ref()
const checkoutFormState = ref({
  fname: '',
  lname: '',
  country: '',
  city: '',
  state: '',
  street_address: '',
  zip_code: '',
  phone_number: undefined,
  email: '',
})
const checkoutFormSchema = object({
  fname: string().required('Enter first name'),
  lname: string().required('Enter last name'),
  country: string().required('Enter country'),
  city: string().required('Enter city'),
  state: string().required('Enter state/province'),
  street_address: string().required('Enter street address'),
  zip_code: string().required('Enter Zip/Postal code'),
  phone_number: string().required('Enter phone number'),
  email: string().required('Enter email address').email('Invalid email address'),
})
const dialCode = computed(() => {
  return countriesCode.find(c => c.name ===
    checkoutFormState.value.country)?.dial_code
})

async function submitCheckoutInfo() {
  await checkoutForm.value!.validate()
  currentStep.value = 2
}
const isWaitingCheckout = ref(false)
async function checkout() {
  isWaitingCheckout.value = true
  const { data, error } = await useCustomFetch<{ checkout_url: string }>('/v1/orders/', {
    method: 'post',
    body: {
      ...checkoutFormState.value,
      phone_number: dialCode.value + ' ' + checkoutFormState.value.phone_number,
      cart_id: cartIdCookie.value
    }
  })
  isWaitingCheckout.value = false
  if (error.value) {
    //todo: toast
  } else if (data.value) {
    window.location.href = data.value.checkout_url
  }
}

const totalPrice = computed(() => {
  let total = 0
  for (const item of cart.value) {
    total += item.price * item.quantity
  }
  return total
})
const shippingFee = computed(() => {
  return checkoutFormState.value.country === 'United Arab Emirates' ? 5 : 20
})
const showCartItems = ref(false)

const isShowedHeaderLine = useIsShowedHeaderLine()
isShowedHeaderLine.value = false

useHead({
  title: 'Checkout - YSV'
})
</script>


<template>
  <div class="checkout-body mycontainer mx-auto">
    <GoBackArrow />

    <div class="w-full max-w-[420px] mx-auto flex flex-col justify-center">
      <div>
        <div class="grid grid-cols-2">
          <div class="hover:cursor-pointer" @click="currentStep = 1">
            <div class="text-4xl stepper" :class="{ 'stepper-active': currentStep === 1 }">
              <UIcon :name="currentStep === 1 ? 'i-ph-number-circle-one' : 'i-ph-check-circle'" />
            </div>
            <div class="text-center" :class="{ 'text-[#c3c3c3]': currentStep !== 1 }">INFO</div>
          </div>
          <div>
            <div class="text-4xl stepper" :class="{ 'stepper-active': currentStep === 2 }">
              <UIcon name="i-ph-number-circle-two" />
            </div>
            <div class="text-center" :class="{ 'text-[#c3c3c3]': currentStep !== 2 }">CHECKOUT</div>
          </div>
        </div>

        <template v-if="currentStep === 1">
          <UForm ref="checkoutForm" :state="checkoutFormState" :schema="checkoutFormSchema" @submit="submitCheckoutInfo"
            class="flex flex-col gap-3">
            <div class="my-4 pb-2 text-medium text-center border-b">SHIPPING ADDRESS</div>
            <UFormGroup name="fname">
              <AppInput label="FIRST NAME" v-model="checkoutFormState.fname" />
            </UFormGroup>
            <UFormGroup name="lname">
              <AppInput label="LAST NAME" v-model="checkoutFormState.lname" />
            </UFormGroup>
            <UFormGroup name="country">
              <USelectMenu searchable v-model="checkoutFormState.country" :options="countriesCode" option-attribute="name"
                value-attribute="name">
                <div class="w-full">
                  <AppInput readonly label="COUNTRY" :model-value="checkoutFormState.country" />
                </div>
              </USelectMenu>
            </UFormGroup>
            <UFormGroup name="city">
              <AppInput label="CITY" v-model="checkoutFormState.city" />
            </UFormGroup>
            <UFormGroup name="state">
              <AppInput label="STATE/PROVINCE" v-model="checkoutFormState.state" />
            </UFormGroup>
            <UFormGroup name="street_address">
              <AppInput label="STREET ADDRESS" v-model="checkoutFormState.street_address" />
            </UFormGroup>
            <UFormGroup name="zip_code">
              <AppInput label="ZIP/POSTAL CODE" v-model="checkoutFormState.zip_code" />
            </UFormGroup>
            <UFormGroup name="phone_number">
              <AppInput type="number" label="PHONE NUMBER" v-model="checkoutFormState.phone_number"
                :dial-code="dialCode" />
            </UFormGroup>
            <UFormGroup name="email">
              <AppInput label="Email address" v-model="checkoutFormState.email" />
            </UFormGroup>
            <div class="mt-10 mb-4 pb-2 text-medium text-center border-b">SHIPPING FEE</div>
            <div class="text-small">
              <template v-if="checkoutFormState.country === 'United Arab Emirates'">
                <div>You are in United Arab Emirates.</div>
                <div>SHIPPING FEE: ${{ shippingFee }}</div>
              </template>
              <template v-else>
                <div>You are outside of United Arab Emirates.</div>
                <div>SHIPPING FEE: ${{ shippingFee }}</div>
              </template>
            </div>
            <button type="submit">
              <div class="go-checkout-btn">GO TO CHECKOUT</div>
            </button>
          </UForm>

          <CustomerBag class="mt-12" border />

        </template>
        <template v-else>
          <div class="mt-4 go-checkout-btn" @click="checkout">CHECKOUT NOW</div>
          <div class="mt-12 border border-black p-3 text-small">
            <div class="border-b border-gray-500">ORDER SUMMARY</div>
            <div class="mt-4 flex text-gray-500"><span>SUBTOTAL</span><span class="ml-auto">${{ totalPrice }}</span></div>
            <div class="flex text-gray-500"><span>SHIPPING</span><span class="ml-auto">${{ shippingFee }}</span></div>
            <div class="my-4 pb-5 border-b flex"><span>TOTAL</span><span class="ml-auto">${{ totalPrice + shippingFee
            }}</span></div>
            <div class="flex items-center">{{ cart.length }} ITEM(S) IN CART
              <span class="ml-auto">
                <UIcon @click="showCartItems = !showCartItems" name="i-iconamoon-arrow-bottom-right-1-light"
                  class="text-2xl hover:cursor-pointer" />
              </span>
            </div>
          </div>
          <CustomerBag v-if="showCartItems" class="my-2" border title="YOUR ORDER" />
          <div class="text-small mt-3 mb-16">
            <div class="py-3 border-b flex items-center"><span>SHIP TO:</span>
              <UButton label="EDIT" variant="ghost" color="blue" @click="currentStep = 1" class="ml-auto" />
            </div>

            <div class="text-gray-500">{{ `${checkoutFormState.fname}
                          ${checkoutFormState.lname}` }}</div>
            <div class="text-gray-500">{{ `${checkoutFormState.country}` }}</div>
            <div class="text-gray-500">{{ `${checkoutFormState.city}` }}</div>
            <div class="text-gray-500">{{ `${checkoutFormState.state}` }}</div>
            <div class="text-gray-500">{{ `${checkoutFormState.street_address}` }}</div>
            <div class="text-gray-500">{{ `PHONE: ${dialCode} ${checkoutFormState.phone_number}` }}</div>
            <div class="text-gray-500">{{ `EMAIL: ${checkoutFormState.email}` }}</div>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>


<style scoped>
.checkout-body {
  margin-bottom: 50px;

  @media screen and (min-width: 480px) {
    margin-bottom: 80px;
  }

  @media screen and (min-width: 768px) {
    margin-bottom: 100px;
  }

  @media screen and (min-width: 1280px) {
    margin-bottom: 150px;
  }
}

.stepper {
  display: flex;
  align-items: center;
  color: #C3C3C3;

  &::before {
    content: '';
    flex: 1;
    height: 2px;
    background-color: #C3C3C3;
  }

  &::after {
    content: '';
    flex: 1;
    height: 2px;
    background-color: #C3C3C3;
  }

  &-active {
    color: black;

    &::before {
      background-color: #000;
    }

    &::after {
      background-color: #000;
    }
  }
}

.go-checkout-btn {
  width: 100%;
  height: 40px;
  background-color: #272727;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;

  @media screen and (min-width: 480px) {
    height: 45px;
  }

  &:hover {
    cursor: pointer;
  }
}

.text-small {
  font-size: 14px;
  text-transform: uppercase;

  @media screen and (min-width: 480px) {
    font-size: 16px;
  }
}
</style>
