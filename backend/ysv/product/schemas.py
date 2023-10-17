import uuid

from pydantic import BaseModel

from ysv.collection.schemas import CollectionRead


class ProductSizeVariantCreate(BaseModel):
    id: str
    clothes_size_id: str
    is_pre_order: bool = False
    storage: int


class ProductSizeVariantUpdate(BaseModel):
    id: str
    is_pre_order: bool = False
    storage: int


class ProductSizeVariantRead(BaseModel):
    id: uuid.UUID
    product_id: uuid.UUID
    clothes_size_id: uuid.UUID
    is_pre_order: bool
    storage: int


class ProductCreate(BaseModel):
    collection_id: str
    name: str
    is_available: bool = True
    price: int
    descriptions: str
    preview_pic: str
    pictures: list[str]
    size_variants: list[ProductSizeVariantCreate]


class ProductPictureRead(BaseModel):
    id: uuid.UUID
    url: str


class ProductRead(BaseModel):
    id: uuid.UUID
    collection_id: uuid.UUID
    collection: CollectionRead
    name: str
    is_available: bool = True
    price: int
    descriptions: str
    preview_pic: str


class ProductDetailRead(ProductRead):
    pictures: list[ProductPictureRead]
    size_variants: list[ProductSizeVariantRead]


class ProductUpdate(BaseModel):
    collection_id: str
    name: str
    is_available: bool = True
    price: int
    descriptions: str
    preview_pic: str
    pictures: list[str]
    size_variants: list[ProductSizeVariantUpdate]


class CollectionProductsRead(CollectionRead):
    products: list[ProductRead] | None = None
