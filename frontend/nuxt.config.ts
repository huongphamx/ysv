// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  modules: ['@nuxt/ui', '@nuxt/image'],

  css: ['@/assets/css/main.css'],

  ui: {
    icons: ['heroicons', 'ph']
  },

  image: {
    format: ['webp'],
    quality: 50,
  },

  runtimeConfig: {
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://localhost:8000/api',
      frontendDomain: process.env.NUXT_PUBLIC_FRONTEND_DOMAIN || 'localhost:3000',
    }
  },
})
