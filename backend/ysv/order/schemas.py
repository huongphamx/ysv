from uuid import UUID

from pydantic import BaseModel, ConfigDict


class OrderCreate(BaseModel):
    fname: str
    lname: str
    country: str
    city: str
    state: str
    street_address: str
    zip_code: str
    phone_number: str
    email: str
    cart_id: str


class OrderRead(BaseModel):
    id: UUID
    fname: str
    lname: str
    country: str
    city: str
    state: str
    street_address: str
    zip_code: str
    phone_number: str
    email: str | None
    is_paid: bool
    is_delivered: bool

    model_config = ConfigDict(from_attributes=True)


class OrderUpdate(BaseModel):
    is_delivered: bool
