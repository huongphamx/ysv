from sqlalchemy import String, Table, Column, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ysv.database.base_model import Base


class ClothesSize(Base):
    __tablename__ = "clothes_size"

    label: Mapped[str] = mapped_column(String(3))
    standard_tall: Mapped[str] = mapped_column(nullable=True)


class ProductSizeVariant(Base):
    __tablename__ = "product_size_variant"

    product_id: Mapped[str] = mapped_column(ForeignKey("product.id"), primary_key=True)
    clothes_size_id: Mapped[str] = mapped_column(
        ForeignKey("clothes_size.id"), primary_key=True
    )
    is_pre_order: Mapped[bool] = mapped_column(default=False)
    clothes_size: Mapped["ClothesSize"] = relationship()
