from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from ysv.database.base_model import Base


class ClothesSize(Base):
    __tablename__ = "clothes_size"

    label: Mapped[str] = mapped_column(String(3))
    # bust: Mapped[str]
    # waist: Mapped[str]
    # hips: Mapped[str]
    # converse_to_us: Mapped[str]
    # converse_to_uk_aus: Mapped[str]
    # converse_to_france: Mapped[str]
    # converse_to_italy: Mapped[str]
    # converse_to_japan: Mapped[str]
    # converse_to_denmark: Mapped[str]
