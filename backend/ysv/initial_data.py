import asyncio
import logging

from sqlalchemy import select
from fastapi_users.password import PasswordHelper

from ysv.config import common_settings
from ysv.user.models import User
from ysv.database.session import async_session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def create_first_admin():
    async with async_session() as db:
        admin_user_db = await db.scalar(
            select(User).where(User.email == common_settings.FIRST_ADMIN_EMAIL)
        )
        if admin_user_db is None:
            admin_user_obj = User(
                email=common_settings.FIRST_ADMIN_EMAIL,
                hashed_password=PasswordHelper().hash(
                    common_settings.FIRST_ADMIN_PASSWORD
                ),
                is_active=True,
                is_superuser=True,
                is_verified=True,
            )
            db.add(admin_user_obj)
            await db.commit()


async def main() -> None:
    logger.info("Creating admin if not existed")
    await create_first_admin()
    logger.info("Admin created")


if __name__ == "__main__":
    asyncio.run(main())
