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
  product_id: string,
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
  is_main_collection: boolean,
  is_show_in_home: boolean,
  products?: Product[],
  main_collection_description?: string,
  main_collection_description_2?: string,
  main_collection_pics?: string,
  lookbook_layout_code: 'two' | 'two_reversed' | 'three',
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

export interface OrderItem {

}

export interface Order {
  id: string,
  fname: string,
  lname: string,
  country: string,
  city: string,
  state: string,
  street_address: string,
  zip_code: string,
  phone_number: string,
  is_paid: boolean,
  is_delivered: boolean,
}