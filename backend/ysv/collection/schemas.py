import uuid

from pydantic import BaseModel, HttpUrl

UUID_ID = uuid.UUID


class CollectionRead(BaseModel):
    id: UUID_ID
    name: str
    descriptions: str
    preview_pic: HttpUrl
    is_on_sale: bool


class CollectionCreate(BaseModel):
    name: str
    descriptions: str
    preview_pic: HttpUrl
    is_on_sale: bool = True


class CollectionUpdate(BaseModel):
    name: str
    descriptions: str
    preview_pic: HttpUrl
    is_on_sale: bool
