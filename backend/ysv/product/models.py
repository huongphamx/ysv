from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ysv.database.base_model import Base

if TYPE_CHECKING:
    from ysv.collection.models import Collection


class Product(Base):
    __tablename__ = "product"

    collection_id: Mapped[str] = mapped_column(ForeignKey("collection.id"))
    collection: Mapped["Collection"] = relationship(cascade="all, delete-orphan")
    name: Mapped[str]
    price: Mapped[int]
    descriptions: Mapped[str]
    preview_pic: Mapped[str]
    is_available: Mapped[bool] = mapped_column(default=True)
