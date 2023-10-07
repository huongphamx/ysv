import uuid

from pydantic import BaseModel
from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    pass


class UserPasswordUpdate(BaseModel):
    old_password: str
    new_password: str
