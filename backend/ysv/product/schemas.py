import uuid

from pydantic import BaseModel


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
    collection_id: uuid.UUID
    name: str
    is_available: bool = True
    price: int
    descriptions: str
    preview_pic: str


class ProductDetailRead(ProductRead):
    pictures: list[ProductPictureRead]
