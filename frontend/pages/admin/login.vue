<script lang="ts" setup>
import { object, string } from 'yup'

const loginForm = ref()
const loginFormState = ref({
  email: '',
  password: '',
})
const loginFormSchema = object({
  email: string().required('Email is required'),
  password: string().required('Password is required'),
})
const accessTokenCookie = useAccessTokenCookie()
const accessToken = useAccessToken()
const isLoggedIn = useIsLoggedIn()
async function submitLogin() {
  await loginForm.value!.validate()
  const loginFormData = new FormData()
  loginFormData.append('username', loginFormState.value.email)
  loginFormData.append('password', loginFormState.value.password)
  const { data, error } = await useCustomFetch<{ access_token: string, token_type: string }>('/v1/auth/login', {
    method: 'post',
    body: loginFormData
  })
  if (error.value) {
    // todo: toast
  } else if (data.value) {
    isLoggedIn.value = true
    accessTokenCookie.value = data.value.access_token
    accessToken.value = data.value.access_token
    await navigateTo('/admin/')
  }
}

definePageMeta({
  layout: 'blank',
})
</script>


<template>
  <div class="mt-10 flex justify-center">
    <div class="border p-5 rounded-lg md:w-1/2 lg:w-1/3">
      <div class="text-xl font-bold text-center">YSV Admin Login</div>
      <UForm ref="loginForm" :state="loginFormState" :schema="loginFormSchema" :validate-on="['submit', 'input']"
        class="flex flex-col gap-3" @submit="submitLogin">
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

