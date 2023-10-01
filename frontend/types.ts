import { string } from "yup"

export interface Collection {
  id: string,
  name: string,
  descriptions: string,
  preview_pic: string,
  is_on_sale: boolean,
}

export interface ProductPicture {
  id: string,
  url: string
}

export interface Product {
  id: string,
  collection_id: string,
  collection: Collection,
  name: string,
  is_available: boolean,
  price: number,
  descriptions: string,
  preview_pic: string,
  pictures: ProductPicture[],
}