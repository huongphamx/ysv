from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ysv.database.base_model import Base

if TYPE_CHECKING:
    from ysv.collection.models import Collection


class ProductPicture(Base):
    __tablename__ = "product_picture"

    product_id: Mapped[str] = mapped_column(ForeignKey("product.id"))
    product: Mapped["Product"] = relationship(back_populates="pictures")
    url: Mapped[str]


class Product(Base):
    __tablename__ = "product"

    collection_id: Mapped[str] = mapped_column(ForeignKey("collection.id"))
    collection: Mapped["Collection"] = relationship(back_populates="products")
    name: Mapped[str]
    is_available: Mapped[bool] = mapped_column(default=True)
    price: Mapped[int]
    descriptions: Mapped[str]
    preview_pic: Mapped[str]
    pictures: Mapped[list["ProductPicture"]] = relationship(back_populates="product")
