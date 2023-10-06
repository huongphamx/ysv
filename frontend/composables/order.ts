import { Order, OrderItem } from '@/types'

export interface FetchOrderParams {
  name: string,
}

export const useOrderList = () => useState<Order[]>('order-list', () => [])

export async function getOrderList(params?: FetchOrderParams) {
  const orderList = useOrderList()

  const { data, error } = await useCustomFetch<Order[]>('/v1/orders/', { params })
  if (error.value) {
    // todo: toast
  } else if (data.value) {
    orderList.value = data.value
  }
}