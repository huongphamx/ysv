export const useIsLoggedIn = () => useState<boolean>('is-logged-in', () => false)
export const useAccessTokenCookie = () => useCookie('access_token', { maxAge: 3600 })
export const useAccessToken = () => useState<string>('access-token')

// export async function logOut() {
//   const isLoggedIn = useIsLoggedIn()
//   const userInfo = useUserInfo()
//   const accessToken = useAccessToken()

//   await useCustomFetch('/v1/auth/logout', { method: 'post' })
//   isLoggedIn.value = false
//   userInfo.value = null
//   accessToken.value = null
// }