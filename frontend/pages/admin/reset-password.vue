<script setup lang="ts">
import { object, string } from 'yup'

const forgotPasswordForm = ref()
const forgotPasswordFormState = ref({
  email: undefined
})
const forgotPasswordFormSchema = object({
  email: string().required('Please enter your email address').email('Invalid email address')
})

async function submitForgotPassword() {
  await forgotPasswordForm.value!.validate()
  const { data, error } = useCustomFetch('/v1/auth/forgot-password', {
    method: 'post',
    body: { email: forgotPasswordFormState.value.email }
  })
  if (error.value) {
    // todo: toast
  } else if (data.value) {
    // todo: toast
  }
}

definePageMeta({
  layout: 'blank'
})
</script>


<template>
  <div class="mt-10 flex justify-center">
    <div class="border p-5 rounded-lg md:w-1/2 lg:w-1/3">
      <div class="text-xl font-bold text-center">Reset password</div>

      <div class="my-5">An email address with reset password link will be sent to your email.</div>

      <UForm ref="forgotPasswordForm" :state="forgotPasswordFormState" :schema="forgotPasswordFormSchema"
        :validate-on="['submit', 'input']" @submit="submitForgotPassword">
        <UFormGroup name="email" label="Enter your Email Address">
          <UInput placeholder="Email address" v-model="forgotPasswordFormState.email" />
        </UFormGroup>
        <div class="my-5 text-center">
          <UButton type="submit" label="Reset password" />
        </div>

        <div>
          <UButton label="Back to login" to="/admin/login" variant="ghost" />
        </div>
      </UForm>
    </div>
  </div>
</template>

