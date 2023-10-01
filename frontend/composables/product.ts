import { Product } from '@/types'

export const useProductList = () => useState<Product[]>('product-list', () => [])

export async function getProductList() {
  const productList = useProductList()

  const { data, error } = await useCustomFetch<Product[]>('/v1/products/')
  if (error.value) {
    // todo: toast
  } else if (data.value) {
    productList.value = data.value
  }
}