import uuid

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.types import UUID

UUID_ID = uuid.UUID


class Base(AsyncAttrs, DeclarativeBase):
    id: Mapped[UUID_ID] = mapped_column(
        UUID, primary_key=True, default=uuid.uuid4, sort_order=-10
    )
