import { Product } from '@/types'

export interface FetchProductParams {
  collection_id?: string,
}

export const useCurrentProduct = () => useState<Product | null>('current-product', () => null)
export const useProductList = () => useState<Product[]>('product-list', () => [])

export async function getProductList(params?: FetchProductParams) {
  const productList = useProductList()

  const { data, error } = await useCustomFetch<Product[]>('/v1/products/', { params })
  if (error.value) {
    // todo: toast
  } else if (data.value) {
    productList.value = data.value
  }
}

export async function adminGetProductList(params?: FetchProductParams) {
  const productList = useProductList()

  const { data, error } = await useCustomFetch<Product[]>('/v1/products/admin/', { params })
  if (error.value) {
    // todo: toast
  } else if (data.value) {
    productList.value = data.value
  }
}