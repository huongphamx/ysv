import { ProductVariantExtended, CartItem } from '@/types'

const CART_MAX_AGE = 3600 * 24 * 30 // 30days
export const useCartIdCookie = () => useCookie<string>('cart-id', { maxAge: CART_MAX_AGE, sameSite: 'lax' })
export const useCart = () => useState<CartItem[]>('cart', () => [])

export const useSelectedProductVariant = () => useState<ProductVariantExtended | null>('selected-product-variant', () => null)

export async function getCartItems() {
  const cart = useCart()
  const cartId = useCartIdCookie()

  const { data: cartItems, error } = await useCustomFetch<CartItem[]>(`/v1/carts/${cartId.value}`)
  if (cartItems.value) {
    cart.value = cartItems.value!
  }
}