<script setup lang="ts">
import { object, string } from 'yup'

const cart = useCart()

const checkoutForm = ref()
const checkoutFormState = ref({
  fname: undefined,
  lname: undefined,
  country: undefined,
  city: undefined,
  state: undefined,
  street_address: undefined,
  zip_code: undefined,
  phone_number: undefined,
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

async function submitCheckout() {
  await checkoutForm.value!.validate()

}
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
        <UForm ref="checkoutForm" :state="checkoutFormState" :schema="checkoutFormSchema" @submit="submitCheckout"
          class="flex flex-col gap-3">
          <div class="my-4 pb-2 text-4xl text-center font-['Italiana'] border-b">SHIPPING ADDRESS</div>

          <UFormGroup name="fname">
            <AppInput label="FIRST NAME" v-model="checkoutFormState.fname" />
          </UFormGroup>

          <UFormGroup name="lname">
            <AppInput label="LAST NAME" v-model="checkoutFormState.lname" />
          </UFormGroup>

          <UFormGroup name="country">
            <AppInput label="COUNTRY" v-model="checkoutFormState.lname" />
          </UFormGroup>

          <UFormGroup name="city">
            <AppInput label="CITY" v-model="checkoutFormState.lname" />
          </UFormGroup>

          <UFormGroup name="state">
            <AppInput label="STATE/PROVINCE" v-model="checkoutFormState.lname" />
          </UFormGroup>

          <UFormGroup name="street_address">
            <AppInput label="STREET ADDRESS" v-model="checkoutFormState.lname" />
          </UFormGroup>

          <UFormGroup name="zip_code">
            <AppInput label="ZIP/POSTAL CODE" v-model="checkoutFormState.lname" />
          </UFormGroup>

          <UFormGroup name="phone_number">
            <AppInput label="PHONE NUMBER" v-model="checkoutFormState.lname" />
          </UFormGroup>

          <div class="my-4 pb-2 text-4xl text-center font-['Italiana'] border-b">SHIPPING METHODS</div>
          <div></div>

          <UButton type="submit" label="GO TO CHECKOUT" block color="black" />
        </UForm>

      </div>

      <CustomerBag />
    </div>
  </div>
</template>

