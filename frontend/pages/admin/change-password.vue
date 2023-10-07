<script setup lang="ts">
import { object, string } from 'yup'

const form = ref()
const formState = ref({
  old_password: undefined,
  new_password: undefined,
})
const formSchema = object({
  old_password: string().required('Enter old password'),
  new_password: string().required('Enter new password'),
})
const changeSuccessMsg = ref('')
async function submitChangePassword() {
  await form.value!.validate()
  const { data, error } = await useCustomFetch('/v1/auth/change-password', {
    method: 'patch',
    body: { old_password: formState.value.old_password, new_password: formState.value.new_password }
  })
  if (error.value) {
    if (error.value.data.detail === 'BAD_CREDENTIALS') form.value.setErrors([{ path: 'old_password', message: 'Password not correct' }])
    if (error.value.data.detail === 'BAD_PASSWORD') form.value.setErrors([{ path: 'new_password', message: 'Same as old password' }])
  } else if (data.value) {
    changeSuccessMsg.value = 'Password changed'
    formState.value.new_password = undefined
    formState.value.new_password = undefined
  }
}

definePageMeta({
  layout: 'admin',
  middleware: 'admin',
})
</script>


<template>
  <div class="h-screen overflow-auto p-5">
    <div class="text-2xl font-bold">Change password</div>
    <div class="my-5 lg:w-1/2 2xl:w-1/3">
      <div v-if="changeSuccessMsg" class="my-5 p-2 rounded-md bg-green-50 border border-green-500 flex items-center">
        <span>{{ changeSuccessMsg }}</span>
        <UButton icon="i-ph-x" @click="changeSuccessMsg = ''" class="ml-auto" variant="ghost" />
      </div>
      <UForm ref="form" :state="formState" :schema="formSchema" @submit="submitChangePassword"
        class="flex flex-col gap-3">
        <UFormGroup required name="old_password" label="Old password">
          <UInput v-model="formState.old_password" />
        </UFormGroup>

        <UFormGroup required name="new_password" label="New password">
          <UInput v-model="formState.new_password" />
        </UFormGroup>

        <div>
          <UButton type="submit" label="Change password" />
        </div>
      </UForm>
    </div>
  </div>
</template>
