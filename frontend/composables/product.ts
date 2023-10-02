import { Product } from '@/types'

export interface FetchProductParams {
  collection_id?: string,
}

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