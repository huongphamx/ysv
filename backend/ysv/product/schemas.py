import uuid

from pydantic import BaseModel

from ysv.collection.schemas import CollectionRead


class ProductCreate(BaseModel):
    collection_id: str
    name: str
    is_available: bool = True
    price: int
    descriptions: str
    preview_pic: str
    pictures: list[str]


class ProductPictureRead(BaseModel):
    id: uuid.UUID
    url: str


class ProductRead(BaseModel):
    id: uuid.UUID
    collection_id: uuid.UUID  # todo: to remove
    collection: CollectionRead
    name: str
    is_available: bool = True
    price: int
    descriptions: str
    preview_pic: str


class ProductDetailRead(ProductRead):
    pictures: list[ProductPictureRead]


class ProductUpdate(BaseModel):
    collection_id: str
    name: str
    is_available: bool = True
    price: int
    descriptions: str
    preview_pic: str
    pictures: list[str]
