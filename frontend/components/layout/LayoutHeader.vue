<script lang="ts" setup>
import { Collection } from '@/types'

export interface CollectionGroup {
  alphabet: string,
  collections: Collection[]
}

const route = useRoute()
const collectionList = useCollectionList()
const cart = useCart()

const sortedCollectionGroups = computed(() => {
  const sortedCollections = collectionList.value.sort((a, b) => a.name.localeCompare(b.name, 'en', { sensitivity: 'base' }))
  const data = sortedCollections.reduce((r, e) => {
    // get first letter of name of current element
    let alphabet = e.name[0]
    // if there is no property in accumulator with this letter create it
    // @ts-ignore
    if (!r[alphabet]) r[alphabet] = { alphabet, collections: [e] }
    // @ts-ignore
    else r[alphabet].record.push(e)

    return r
  }, {})
  return Object.values(data)
})

const props = defineProps({
  isShowBottomLine: {
    type: Boolean,
    default: false,
  }
})

const borderColor = computed(() => {
  return route.path === '/' ? 'white' : 'black'
})

const links = [
  { to: '/about', text: 'ABOUT' },
  { to: '/events', text: 'EVENTS' },
  { to: '/contact', text: 'CONTACT' },
  { to: '/payment-delivery', text: 'PAYMENT & DELIVERY' },
  { to: '/cooperation', text: 'COOPERATION' },
]

const isShowedMobileMenu = ref(false)
</script>


<template>
  <div class="z-10 py-2" :class="{ 'xl:border-b': isShowBottomLine }">
    <div class="h-12 mycontainer mx-auto flex justify-between items-center"
      :class="{ 'text-white': $route.path === '/' }">
      <div class="text-2xl font-['Italiana']">
        <NuxtLink to="/" @click="isShowedMobileMenu = false">YSV</NuxtLink>
      </div>

      <div class="w-2/3 justify-between hidden xl:flex">
        <NuxtLink v-for="link, i in links" :key="i" :to="link.to"
          :class="{ 'active': $route.path === link.to, 'link': $route.path !== link.to }">
          {{ link.text }}
        </NuxtLink>

        <UPopover mode="hover">
          <div class="flex items-center">COLLECTIONS
            <UIcon name="i-ph-arrow-down-right" />
          </div>
          <template #panel>
            <div class="p-2">
              <div v-for="g, i in (sortedCollectionGroups as CollectionGroup[])" :key="i">
                <div class="border-b text-gray-500">{{ g.alphabet }}</div>
                <div v-for="c, i in g.collections" class="my-2 text-black">
                  <NuxtLink :to="`/catalog/${c.id}`" class="underline">{{ c.name.toUpperCase() }}</NuxtLink>
                </div>
              </div>
            </div>
          </template>
        </UPopover>
      </div>
      <div class="hidden xl:flex">
        <UPopover :ui="{ rounded: '' }">
          <UButton icon="i-ph-shopping-cart" color="black" variant="ghost" :ui="{ icon: { size: { sm: 'h-6 w-6' } } }" />

          <template #panel>
            <template v-if="cart.length > 0">
              <div class="p-3 max-h-[600px] overflow-auto">
                <div class="text-lg font-['Italiana']">YOUR BAG ({{ cart.length }})</div>
                <div class="divide-y">
                  <div v-for="item in cart" :key="item.product_variant_id" class="flex py-4">
                    <img :src="item.product_preview_pic" alt="" class="w-[66px] h-[84px] object-cover">
                    <div class="ml-4">
                      <div class="flex text-[13px] font-bold max-w-[230px]">
                        <div>{{ item.collection_name }}</div>
                        <div class="ml-3">${{ item.product_price }}</div>
                      </div>
                      <div class="text-[11px] text-gray-500">COLOR: {{ item.product_variant_name.toUpperCase() }}</div>
                      <div class="text-[11px] text-gray-500">SIZE: {{ item.product_variant_size }}</div>
                      <div class="flex">
                        <UButton icon="i-ph-minus" size="xs" color="black" :ui="{ rounded: '' }" />
                        <UButton icon="i-ph-plus" size="xs" color="black" :ui="{ rounded: '' }" class="mx-2" />
                        <UButton icon="i-ph-trash" size="xs" variant="outline" color="black" :ui="{ rounded: '' }"
                          class="ml-auto" />
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </template>
            <template v-else>
              <div class="p-3">
                <div class="text-lg font-['Italiana']">YOUR BAG ({{ cart.length }})</div>
                You don't have any item in bag!
              </div>
            </template>
          </template>
        </UPopover>
      </div>

      <div class="xl:hidden">
        <div class="relative">
          <UButton icon="i-ph-list" color="black" variant="ghost" :ui="{ icon: { size: { sm: 'h-6 w-6' } } }"
            @click="isShowedMobileMenu = true" />

          <div v-if="isShowedMobileMenu" class="absolute top-0 -right-0 w-[210px] bg-white text-black">
            <div class="text-right">
              <UButton icon="i-ph-x" color="white" variant="ghost" :ui="{ icon: { size: { sm: 'h-6 w-6' } } }"
                @click="isShowedMobileMenu = false" />
            </div>

            <div class="px-5 pb-5">
              <UPopover mode="hover">
                <div class="flex items-center">COLLECTIONS
                  <UIcon name="i-ph-arrow-down-right" />
                </div>
                <template #panel>
                  <div class="p-2">
                    <div v-for="g, i in (sortedCollectionGroups as CollectionGroup[])" :key="i">
                      <div class="border-b text-gray-500">{{ g.alphabet }}</div>
                      <div v-for="c, i in g.collections" class="my-2 text-black">
                        <NuxtLink :to="`/catalog/${c.id}`" class="underline">{{ c.name.toUpperCase() }}</NuxtLink>
                      </div>
                    </div>
                  </div>
                </template>
              </UPopover>

              <div v-for="link, i in links" :key="i" class="first:mt-0 last:mb-0 my-4">
                <NuxtLink :to="link.to" :class="{ 'active': $route.path === link.to, 'link': $route.path !== link.to }"
                  @click="isShowedMobileMenu = false">
                  {{ link.text }}
                </NuxtLink>
              </div>

              <UPopover mode="hover">
                <div class="flex items-center gap-3">CART
                  <UIcon name="i-ph-shopping-cart" />
                </div>
                <template #panel>
                  <div class="p-2">
                    <div v-for="g, i in (sortedCollectionGroups as CollectionGroup[])" :key="i">
                      <div class="border-b text-gray-500">{{ g.alphabet }}</div>
                      <div v-for="c, i in g.collections" class="my-2 text-black">
                        <NuxtLink :to="`/catalog/${c.id}`" class="underline">{{ c.name.toUpperCase() }}</NuxtLink>
                      </div>
                    </div>
                  </div>
                </template>
              </UPopover>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>


<style scoped>
.active {
  border-bottom: 2px solid black;
}

.link {
  border-bottom: 2px solid transparent;
}

.link:hover {
  border-bottom-color: v-bind('borderColor');
}
</style>