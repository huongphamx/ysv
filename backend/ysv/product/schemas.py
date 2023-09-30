import uuid

from pydantic import BaseModel


class ProductCreate(BaseModel):
    collection_id: str
    name: str
    price: int
    descriptions: str
    preview_pic: str
    is_available: bool = True


class ProductRead(BaseModel):
    id: uuid.UUID
    collection_id: str
    name: str
    price: int
    descriptions: str
    preview_pic: str
    is_available: bool = True
