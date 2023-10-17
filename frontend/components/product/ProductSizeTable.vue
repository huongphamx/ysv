<script setup lang="ts">
import { ProductVariant, ProductVariantExtended } from '@/types'

const props = defineProps<{
  variants: ProductVariant[],
}>()

const selectedProductVariant = useSelectedProductVariant()

const sizeList = useSizeList()
await getSizeList()
const sizeOrder = ['XS', 'S', 'M', 'L'];

const unSortedSizeVariants = props.variants.map(v => {
  return {
    id: v.id,
    size: sizeList.value.find(s => s.id === v.clothes_size_id)?.label!,
    product_id: v.product_id,
    clothes_size_id: v.clothes_size_id,
    is_pre_order: v.is_pre_order,
    standard_tall: sizeList.value.find(s => s.id === v.clothes_size_id)?.standard_tall!
  }
})
const sortedSizeVariants: ProductVariantExtended[] = unSortedSizeVariants.sort((a, b) => {
  const sizeA = sizeOrder.indexOf(a.size)
  const sizeB = sizeOrder.indexOf(b.size)

  return sizeA - sizeB
})

const selectSize = (v: ProductVariantExtended) => {
  selectedProductVariant.value = v
}
</script>

<template>
  <div>
    <table>
      <tbody>
        <tr>
          <td v-for="v in sortedSizeVariants.slice(0, 2)" :key="v.id" class="group"
            :class="{ 'active-td': selectedProductVariant?.size === v.size }" @click="selectSize(v)">
            <div class="group-hover:hidden">{{ v.size }}</div>
            <div class="absolute w-full bottom-0 right-0 group-hover:hidden">{{ v.is_pre_order ? 'Pre-order' : '' }}</div>
            <div class="absolute w-full top-1/2 -translate-y-1/2 hidden group-hover:block">{{ v.standard_tall }} cm</div>
          </td>
        </tr>
        <tr>
          <td v-for="v in sortedSizeVariants.slice(2, 4)" :key="v.id" class="group"
            :class="{ 'active-td': selectedProductVariant?.size === v.size }" @click="selectSize(v)">
            <div class="group-hover:hidden">{{ v.size }}</div>
            <div class="absolute w-full bottom-0 right-0 group-hover:hidden">{{ v.is_pre_order ? 'Pre-order' : '' }}</div>
            <div class="absolute w-full top-1/2 -translate-y-1/2 hidden group-hover:block">{{ v.standard_tall }} cm</div>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="mt-2 xl:-mb-0.5 underline text-gray-500 text-sm md:text-base">
      <NuxtLink to="/size-guide">SIZE GUIDE</NuxtLink>
    </div>
  </div>
</template>


<style scoped>
table {
  border: 2px solid var(--black);
  border-collapse: collapse;
  color: var(--black);
  font-size: 14px;

  @media screen and (min-width: 768px) {
    font-size: 16px;
  }
}

td {
  width: 75px;
  height: 45px;
  border: 2px solid var(--black);
  text-align: center;
  position: relative;

  &:hover {
    cursor: pointer;
  }

  &.active-td {
    background-color: var(--black);
    color: white;
  }

  @media screen and (min-width: 768px) {
    width: 99px;
    height: 72px;
  }
}
</style>

