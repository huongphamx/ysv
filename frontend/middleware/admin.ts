export default defineNuxtRouteMiddleware((to, from) => {
  const isLoggedIn = useIsLoggedIn()
  const accessTokenCookie = useAccessTokenCookie()
  const accessToken = useAccessToken()

  if (!isLoggedIn.value) {
    if (!accessTokenCookie.value) {
      return navigateTo('/admin/login')
    } else {
      accessToken.value = accessTokenCookie.value
      isLoggedIn.value = true
    }
  }
})