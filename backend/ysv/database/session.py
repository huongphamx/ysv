from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

from ysv.config import common_settings

async_engine = create_async_engine(common_settings.POSTGRES_URL)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
