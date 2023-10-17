import { Order, OrderItem } from '@/types'

export interface FetchOrderParams {
  phone_number?: string,
  page?: number,
  size?: number,
}

export interface FetchOrderListResponse {
  items: Order[],
  total: number,
  page: number,
  size: number,
  pages: number,
}

export const useOrderList = () => useState<Order[]>('order-list', () => [])
export const useTotalOrder = () => useState<number>('total-order', () => 0)
export const usePageOrder = () => useState<number>('page-order', () => 1)

export async function getOrderList(params?: FetchOrderParams) {
  const orderList = useOrderList()
  const totalOrder = useTotalOrder()
  const pageOrder = usePageOrder()

  const { data, error } = await useCustomFetch<FetchOrderListResponse>('/v1/orders/', { params: { ...params, size: 10 } })
  if (error.value) {
    // todo: toast
  } else if (data.value) {
    orderList.value = data.value.items
    totalOrder.value = data.value.total
    pageOrder.value = data.value.page
  }
}