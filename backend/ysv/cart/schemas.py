from typing import Literal

from pydantic import BaseModel


class CartCreate(BaseModel):
    cart_id: str


class CartItemCreate(BaseModel):
    product_size_variant_id: str


class CartItemUpdate(BaseModel):
    action: Literal["increase_item", "decrease_item", "delete_item"]
    item_id: str
