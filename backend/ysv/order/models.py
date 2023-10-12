from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ysv.database.base_model import Base

if TYPE_CHECKING:
    from ysv.product.size.models import ProductSizeVariant


class OrderItem(Base):
    __tablename__ = "order_item"

    order_id: Mapped[str] = mapped_column(ForeignKey("order.id"), primary_key=True)
    product_size_variant_id: Mapped[str] = mapped_column(
        ForeignKey("product_size_variant.id"), primary_key=True
    )
    quantity: Mapped[int]
    product_size_variant: Mapped["ProductSizeVariant"] = relationship()


class Order(Base):
    __tablename__ = "order"

    fname: Mapped[str]
    lname: Mapped[str]
    country: Mapped[str]
    city: Mapped[str]
    state: Mapped[str]
    street_address: Mapped[str]
    zip_code: Mapped[str]
    phone_number: Mapped[str]
    email: Mapped[str] = mapped_column(nullable=True)
    cart_id: Mapped[str]
    is_paid: Mapped[bool] = mapped_column(default=False)
    is_delivered: Mapped[bool] = mapped_column(default=False)

    order_items: Mapped[list["OrderItem"]] = relationship()
