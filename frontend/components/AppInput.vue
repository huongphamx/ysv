<script setup lang="ts">
const props = defineProps<{
  modelValue: string | undefined,
  label: string,
}>()

const emit = defineEmits<{
  'update:modelValue': [value: string | undefined]
}>()

const value = computed({
  get() {
    return props.modelValue
  },
  set(value) {
    emit('update:modelValue', value)
  }
})

defineOptions({
  inheritAttrs: false
})
</script>


<template>
  <label class="text-small text-[#888888]">{{ label }}</label>
  <input v-model="value" class="w-full mt-1 py-2 px-4 border-b border-gray-400 focus:outline-none bg-gray-100"
    v-bind="$attrs" />
</template>


<style scoped>
.text-small {
  font-size: 14px;
  text-transform: uppercase;

  @media screen and (min-width: 480px) {
    font-size: 16px;
  }
}
</style>
