// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  modules: ['@nuxt/ui', '@nuxt/image'],

  ui: {
    icons: ['heroicons', 'ph']
  },

  image: {
    format: ['webp'],
    quality: 50,
  }
})
