import uuid

from pydantic import BaseModel, HttpUrl

UUID_ID = uuid.UUID


class CollectionRead(BaseModel):
    id: UUID_ID
    name: str
    descriptions: str
    preview_pic: HttpUrl
    is_on_sale: bool
    is_main_collection: bool
    is_show_in_home: bool
    home_position: int | None
    main_collection_description: str | None = None
    main_collection_description_2: str | None = None
    main_collection_pics: str | None = None
    lookbook_layout_code: str


class CollectionCreate(BaseModel):
    name: str
    descriptions: str
    preview_pic: HttpUrl
    is_on_sale: bool = True
    lookbook_layout_code: str


class CollectionUpdate(BaseModel):
    name: str
    descriptions: str
    preview_pic: HttpUrl
    is_on_sale: bool
    lookbook_layout_code: str


class CollectionAddMain(BaseModel):
    collection_id: str
    main_collection_description: str
    main_collection_description_2: str
    main_collection_pics: str


class CollectionShowHome(BaseModel):
    collection_ids: list[str | None]
