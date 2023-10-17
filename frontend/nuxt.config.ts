// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true, viteInspect: false, },

  app: {
    pageTransition: { name: 'page', mode: 'out-in' },
  },

  modules: ['@nuxt/ui', '@nuxtjs/google-fonts', '@vueuse/motion/nuxt'],

  css: ['@/assets/css/main.css', '@/assets/css/image.css', '@/assets/css/container.css', '@/assets/css/text.css'],

  postcss: {
    plugins: {
      'postcss-nested': {},
    }
  },

  ui: {
    icons: ['heroicons', 'ph', 'iconamoon']
  },

  runtimeConfig: {
    public: {
      apiBase: 'https://api.pxh-dev.online/api',
      frontendDomain: process.env.NUXT_PUBLIC_FRONTEND_DOMAIN || 'localhost:3000',
      s3BaseUrl: 'https://ysv-dev.s3.ap-northeast-1.amazonaws.com',
      cloudfrontDistributionDomain: 'https://d1oxuz3phc9a42.cloudfront.net'
    }
  },

  colorMode: { preference: 'light' },

  routeRules: {
    // '/admin/**': { ssr: false },
    '/about': { prerender: true },
    '/events': { prerender: true },
    '/payment-delivery': { prerender: true },
    '/cooperation': { prerender: true },
    '/size-guide': { prerender: true },
  },
  // ssr: false,

  googleFonts: {
    families: {
      'IBM Plex Sans': true,
      Italiana: true
    }
  }
})
