import { ClothesSize } from '@/types'

export const useSizeList = () => useState<ClothesSize[]>('size-list', () => [])
export async function getSizeList() {
  const sizeList = useSizeList()
  const { data, error } = await useCustomFetch<ClothesSize[]>('/v1/sizes/')
  if (error.value) {
    // todo: toast
  } else if (data.value) {
    sizeList.value = data.value
  }
}