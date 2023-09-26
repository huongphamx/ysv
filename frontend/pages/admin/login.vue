<script lang="ts" setup>
import { object, string } from 'yup'

const loginForm = ref()
const loginFormState = ref({
  email: undefined,
  password: undefined,
})
const loginFormSchema = object({
  email: string().required('Email is required'),
  password: string().required('Password is required'),
})

definePageMeta({
  layout: 'blank',
})
</script>


<template>
  <div class="h-screen flex justify-center items-center">
    <div class="border p-5 rounded-lg w-1/2">
      <div class="text-xl font-bold text-center">Admin Login</div>
      <UForm ref="loginForm" :state="loginFormState" :schema="loginFormSchema" :validate-on="['submit']">
        <UFormGroup name="email" label="Email address" class="my-2">
          <UInput v-model="loginFormState.email" />
        </UFormGroup>

        <UFormGroup name="password" label="Password" class="my-2">
          <UInput type="password" v-model="loginFormState.password" />
        </UFormGroup>

        <UButton type="submit" label="Login" block />
      </UForm>
    </div>
  </div>
</template>

