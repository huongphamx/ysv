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
  <div class="mt-10 flex justify-center">
    <div class="border p-5 rounded-lg md:w-1/2 lg:w-1/3">
      <div class="text-xl font-bold text-center">YSV Admin Login</div>
      <UForm ref="loginForm" :state="loginFormState" :schema="loginFormSchema" :validate-on="['submit']"
        class="flex flex-col gap-3">
        <UFormGroup name="email" label="Email address">
          <UInput v-model="loginFormState.email" />
        </UFormGroup>

        <UFormGroup name="password" label="Password">
          <UInput type="password" v-model="loginFormState.password" />
        </UFormGroup>

        <div class="text-center my-3">
          <UButton type="submit" label="Login" block />
        </div>

        <div class="text-center">
          Forgot password? <NuxtLink to="/admin/reset-password"><span class="text-green-500">Reset password</span>
          </NuxtLink>
        </div>
      </UForm>
    </div>
  </div>
</template>

