export const useIsLoggedIn = () => useState<boolean>('is-logged-in', () => false)
export const useAccessToken = () => useCookie('access_token', { maxAge: 3600 })

// export async function logOut() {
//   const isLoggedIn = useIsLoggedIn()
//   const userInfo = useUserInfo()
//   const accessToken = useAccessToken()

//   await useCustomFetch('/v1/auth/logout', { method: 'post' })
//   isLoggedIn.value = false
//   userInfo.value = null
//   accessToken.value = null
// }