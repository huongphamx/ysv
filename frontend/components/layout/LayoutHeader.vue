<script lang="ts" setup>
const route = useRoute()

const borderColor = computed(() => {
  return route.path === '/' ? 'white' : 'black'
})

const links = [
  { to: '/about', text: 'ABOUT' },
  { to: '/events', text: 'EVENTS' },
  { to: '/payment-delivery', text: 'PAYMENT & DELIVERY' },
  { to: '/cooperation', text: 'COOPERATION' },
  { to: '/lookbook', text: 'LOOKBOOK' },
]

const isShowedMobileMenu = useIsShowedMobileMenu()
const isShowedHeaderLine = useIsShowedHeaderLine()
</script>


<template>
  <div class="z-10 py-2" :class="{ 'xl:border-b xl:border-black': isShowedHeaderLine }">
    <div class="h-12 mycontainer mx-auto flex justify-between items-center"
      :class="{ 'text-white': $route.path === '/' }">
      <div class="text-4xl font-['Italiana']">
        <NuxtLink to="/" @click="isShowedMobileMenu = false">YSV</NuxtLink>
      </div>

      <div class="w-2/3 justify-between hidden xl:flex">
        <NuxtLink v-for="link, i in links" :key="i" :to="link.to"
          :class="{ 'active': $route.path === link.to, 'link': $route.path !== link.to }">
          {{ link.text }}
        </NuxtLink>
        <LayoutHeaderCollections />
      </div>
      <div class="hidden xl:block">
        <LayoutHeaderCart />
      </div>

      <div class="xl:hidden">
        <div class="relative">
          <UButton icon="i-ph-list" color="black" variant="ghost" :ui="{ icon: { size: { sm: 'h-6 w-6' } } }"
            @click="isShowedMobileMenu = true" />
          <div v-if="isShowedMobileMenu"
            class="absolute top-0 -right-0 w-[210px] bg-white text-[var(--black)] border border-black">
            <div class="text-right">
              <UButton icon="i-ph-x" color="white" variant="ghost" :ui="{ icon: { size: { sm: 'h-6 w-6' } } }"
                @click="isShowedMobileMenu = false" />
            </div>
            <div class="px-5 pb-5">
              <LayoutHeaderCollections />
              <div v-for="link, i in links" :key="i" class="first:mt-0 last:mb-0 my-4">
                <NuxtLink :to="link.to" :class="{ 'active': $route.path === link.to, 'link': $route.path !== link.to }"
                  @click="isShowedMobileMenu = false">
                  {{ link.text }}
                </NuxtLink>
              </div>
              <LayoutHeaderCart />
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>


<style scoped>
.active {
  border-bottom: 1px solid black;
}

.link {
  border-bottom: 1px solid transparent;
}

.link:hover {
  border-bottom-color: v-bind('borderColor');
}
</style>