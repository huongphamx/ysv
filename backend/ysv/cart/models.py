from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ysv.database.base_model import Base

if TYPE_CHECKING:
    from ysv.product.size.models import ProductSizeVariant


class CartItem(Base):
    __tablename__ = "cart_item"

    cart_id: Mapped[str] = mapped_column(ForeignKey("cart.id"), primary_key=True)
    product_size_variant_id: Mapped[str] = mapped_column(
        ForeignKey("product_size_variant.id"), primary_key=True
    )
    quantity: Mapped[int]
    product_size_variant: Mapped["ProductSizeVariant"] = relationship()


class Cart(Base):
    __tablename__ = "cart"

    cart_items: Mapped[list["CartItem"]] = relationship(cascade="all, delete-orphan")
