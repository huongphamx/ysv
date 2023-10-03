import uuid

from pydantic import BaseModel


class ClothSizeRead(BaseModel):
    id: uuid.UUID
    label: str
    standard_tall: str
