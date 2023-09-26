from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from ysv.database.base_model import Base


class User(Base):
    __tablename__ = "user"

    email: Mapped[str] = mapped_column(String(100))
    hashed_password: Mapped[str]
