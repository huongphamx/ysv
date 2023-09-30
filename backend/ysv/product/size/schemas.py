import uuid

from pydantic import BaseModel


class ClothSizeRead(BaseModel):
    id: uuid.UUID
    label: str
    # bust: str
    # waist: str
    # hips: str
    # converse_to_us: str
    # converse_to_uk_aus: str
    # converse_to_france: str
    # converse_to_italy: str
    # converse_to_japan: str
    # converse_to_denmark: str
