<script setup lang="ts">
import { object, string } from 'yup'
import { countriesCode } from '@/countries'

const currentStep = ref(2)

const cart = useCart()

const checkoutForm = ref()
const checkoutFormState = ref({
  fname: '',
  lname: '',
  country: '',
  city: '',
  state: '',
  street_address: '',
  zip_code: '',
  phone_number: '',
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
})

async function submitCheckoutInfo() {
  // await checkoutForm.value!.validate()
  currentStep.value = 2
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

useHead({
  title: 'Checkout - YSV'
})
</script>


<template>
  <div class="mycontainer mx-auto">
    <div class="my-6 hidden xl:block">
      <div class="flex items-center gap-2 hover:cursor-pointer" @click="$router.back()">
        <UIcon name="i-ph-arrow-up-left" class="text-xl" /><span>GO BACK</span>
      </div>
    </div>

    <div class="w-[400px] mx-auto flex flex-col justify-center">
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
            <div class="my-4 pb-2 text-4xl text-center font-['Italiana'] border-b">SHIPPING ADDRESS</div>
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
              <div class="relative">
                <AppInput label="PHONE NUMBER" v-model="checkoutFormState.phone_number" class="pl-10" />
                <span class="absolute top-1/2 left-0">{{ countriesCode.find(c => c.name ===
                  checkoutFormState.country)?.dial_code
                }}</span>
              </div>
            </UFormGroup>
            <div class="my-4 pb-2 text-4xl text-center font-['Italiana'] border-b">SHIPPING FEE</div>
            <div>
              <template v-if="checkoutFormState.country === 'United Arab Emirates'">
                <div>You are in United Arab Emirates.</div>
                <div>SHIPPING FEE: ${{ shippingFee }}</div>
              </template>
              <template v-else>
                <div>You are outside of United Arab Emirates.</div>
                <div>SHIPPING FEE: ${{ shippingFee }}</div>
              </template>
            </div>
            <UButton type="submit" label="GO TO CHECKOUT" block color="black" />
          </UForm>

          <CustomerBag class="my-5" border />

        </template>
        <template v-else>
          <UButton label="CHECKOUT NOW" block :ui="{ rounded: '' }" color="black" class="my-5" />
          <div class="border border-black p-3">
            <div class="border-b border-gray-500">ORDER SUMMARY</div>
            <div class="mt-4 flex text-gray-500"><span>SUBTOTAL</span><span class="ml-auto">${{ totalPrice }}</span></div>
            <div class="flex text-gray-500"><span>SHIPPING</span><span class="ml-auto">${{ shippingFee }}</span></div>
            <div class="my-4 pb-5 border-b flex"><span>TOTAL</span><span class="ml-auto">${{ totalPrice + shippingFee
            }}</span></div>
            <div class="flex items-center">{{ cart.length }} ITEM(S) IN CART
              <span class="ml-auto">
                <UButton @click="showCartItems = !showCartItems" icon="i-ph-arrow-down-right" variant="ghost"
                  color="black" />
              </span>
            </div>
          </div>
          <CustomerBag v-if="showCartItems" class="my-2" border title="YOUR ORDER" />
          <div>
            <div class="py-3 border-b flex items-center"><span>SHIP TO:</span>
              <UButton label="EDIT" variant="ghost" color="blue" @click="currentStep = 1" class="ml-auto" />
            </div>

            <div class="text-gray-500">{{ `${checkoutFormState.fname.toUpperCase()}
                          ${checkoutFormState.lname.toUpperCase()}` }}</div>
            <div class="text-gray-500">{{ `${checkoutFormState.country.toUpperCase()}` }}</div>
            <div class="text-gray-500">{{ `${checkoutFormState.city.toUpperCase()}` }}</div>
            <div class="text-gray-500">{{ `${checkoutFormState.state.toUpperCase()}` }}</div>
            <div class="text-gray-500">{{ `${checkoutFormState.street_address.toUpperCase()}` }}</div>
            <div class="text-gray-500">{{ `PHONE: ${checkoutFormState.phone_number}` }}</div>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>


<style scoped>
.stepper {
  display: flex;
  align-items: center;
  color: #C3C3C3;
}

.stepper::before {
  content: '';
  flex: 1;
  height: 2px;
  background-color: #C3C3C3;
}

.stepper::after {
  content: '';
  flex: 1;
  height: 2px;
  background-color: #C3C3C3;
}

.stepper-active {
  color: black;
}

.stepper-active::before {
  background-color: #000;
}

.stepper-active::after {
  background-color: #000;
}
</style>
