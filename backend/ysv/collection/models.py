from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from ysv.database.base_model import Base


class Collection(Base):
    __tablename__ = "collection"

    name: Mapped[str] = mapped_column(String(255))
    descriptions: Mapped[str] = mapped_column(String(1000))
    preview_pic: Mapped[str]
    is_on_sale: Mapped[bool] = mapped_column(default=True)
