// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true, viteInspect: false, },

  modules: ['@nuxt/ui', '@nuxt/image', '@nuxtjs/google-fonts'],

  colorMode: { preference: 'light' },

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

  googleFonts: {
    families: {
      'IBM Plex Sans': true,
      Italiana: true
    }
  }
})
