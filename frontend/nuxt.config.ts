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
      apiBase: process.env.NUXT_PUBLIC_API_BASE,
      s3BaseUrl: process.env.NUXT_PUBLIC_S3_BASE_URL,
      cloudfrontDistributionDomain: process.env.NUXT_PUBLIC_CLOUDFRONT_DISTRIBUTION_DOMAIN
    }
  },

  colorMode: { preference: 'light' },

  googleFonts: {
    families: {
      'IBM Plex Sans': true,
      Italiana: true
    }
  }
})
