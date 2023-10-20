from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ysv.database.base_model import Base

if TYPE_CHECKING:
    from ysv.product.models import Product


class Collection(Base):
    __tablename__ = "collection"

    name: Mapped[str] = mapped_column(String(255))
    descriptions: Mapped[str] = mapped_column(String(1000))
    preview_pic: Mapped[str]
    is_on_sale: Mapped[bool] = mapped_column(default=True)
    is_main_collection: Mapped[bool] = mapped_column(default=False)
    main_collection_description: Mapped[str] = mapped_column(nullable=True)
    main_collection_description_2: Mapped[str] = mapped_column(nullable=True)
    main_collection_pics: Mapped[str] = mapped_column(nullable=True)
    is_show_in_home: Mapped[bool] = mapped_column(default=False)
    home_position: Mapped[int | None] = mapped_column(nullable=True)
    lookbook_layout_code: Mapped[str] = mapped_column(default="two")
    products: Mapped[list["Product"]] = relationship(
        back_populates="collection", cascade="all, delete-orphan"
    )
