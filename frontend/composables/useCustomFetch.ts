import type { UseFetchOptions } from 'nuxt/app'
import { defu } from 'defu'

export function useCustomFetch<T>(url: string, options: UseFetchOptions<T> = {}) {
  const accessToken = useAccessToken()
  const config = useRuntimeConfig()

  const defaults: UseFetchOptions<T> = {
    baseURL: config.public.apiBase ?? 'http://localhost:8000/api',
    // cache request
    key: url,

    // set user token if connected
    headers: accessToken.value
      ? { Authorization: `Bearer ${accessToken.value}` }
      : {},

    onResponse(_ctx) {
      // _ctx.response._data = new myBusinessResponse(_ctx.response._data)
      // console.log(_ctx.response.headers)
    },

    onResponseError(_ctx) {
      if (_ctx.response.status === 401 || _ctx.response.status === 403) {
        navigateTo('/login')
      }
    }
  }

  // for nice deep defaults, please use unjs/defu
  const params = defu(options, defaults)

  return useFetch(url, params)
}
