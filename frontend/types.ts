export interface ProductVariant {
  id: string,
  product_id: string,
  clothes_size_id: string,
  is_pre_order: boolean,
}

export interface ProductVariantExtended extends ProductVariant {
  size: string,
  standard_tall: string,
}

export interface CartItem {
  quantity: number,
  id: string,
  preview_pic: string,
  collection: string,
  price: number,
  color: string,
  size: string,
}

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
  size_variants: ProductVariant[],
}


export interface ClothesSize {
  id: string,
  label: string,
  standard_tall: string,
}