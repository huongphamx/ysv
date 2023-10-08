import uuid
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import expression
from sqlalchemy.types import UUID, DateTime

UUID_ID = uuid.UUID


class utcnow(expression.FunctionElement):
    type = DateTime()
    inherit_cache = True


@compiles(utcnow, "postgresql")
def pg_utcnow(element, compiler, **kw):
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


class Base(AsyncAttrs, DeclarativeBase):
    id: Mapped[UUID_ID] = mapped_column(
        UUID, primary_key=True, default=uuid.uuid4, sort_order=-10
    )
    created_at: Mapped[datetime] = mapped_column(
        server_default=utcnow(), sort_order=9998
    )
    updated_at: Mapped[datetime] = mapped_column(
        onupdate=utcnow(), sort_order=9998, nullable=True
    )
