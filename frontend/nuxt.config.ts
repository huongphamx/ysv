// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true, viteInspect: false, },

  modules: ['@nuxt/ui', '@nuxtjs/google-fonts'],

  css: ['@/assets/css/main.css', '@/assets/css/image.css'],

  ui: {
    icons: ['heroicons', 'ph']
  },

  runtimeConfig: {
    public: {
      apiBase: 'http://localhost:8000/api',
      frontendDomain: process.env.NUXT_PUBLIC_FRONTEND_DOMAIN || 'localhost:3000',
      s3BaseUrl: 'https://ysv-dev.s3.ap-northeast-1.amazonaws.com'
    }
  },

  //routeRules: {
    // Admin dashboard renders only on client-side
   // '/admin/**': { ssr: false },
 // },
  ssr: false,

  googleFonts: {
    families: {
      'IBM Plex Sans': true,
      Italiana: true
    }
  }
})
