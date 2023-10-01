import { Collection } from '@/types'

export const useCollectionList = () => useState<Collection[]>('collection-list', () => [])

export async function getCollectionList() {
  const collectionList = useCollectionList()

  const { data, error } = await useCustomFetch<Collection[]>('/v1/collections/')
  if (error.value) {
    // todo: toast
  } else if (data.value) {
    collectionList.value = data.value
  }
}