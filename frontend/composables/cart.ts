
import { ProductVariantExtended, CartItem } from '@/types'

const CART_MAX_AGE = 3600 * 24 * 30 // 30days
export const useCartItemIdsCookie = () => useCookie<{ id: string, quantity: number }[]>('cart-variant-ids-cookie', { maxAge: CART_MAX_AGE, sameSite: 'lax', default: () => [] })
export const useCart = () => useState<CartItem[]>('cart', () => [])

export const useSelectedProductVariant = () => useState<ProductVariantExtended | null>('selected-product-variant', () => null)
