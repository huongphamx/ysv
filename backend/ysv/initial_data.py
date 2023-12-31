import asyncio
import logging

from sqlalchemy import select
from fastapi_users.password import PasswordHelper

from ysv.config import common_settings
from ysv.user.models import User
from ysv.product.size.models import ClothesSize
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


async def init_clothes_sizes():
    async with async_session() as db:
        sizes = (await db.scalars(select(ClothesSize))).all()
        if len(sizes) == 0:
            sizes = ["XS", "S", "M", "L"]
            standard_talls = ["158-168", "163-174", "169-180", "169-180"]
            for size, standard_tall in zip(sizes, standard_talls):
                size_obj = ClothesSize(label=size, standard_tall=standard_tall)
                db.add(size_obj)
            await db.commit()


async def main() -> None:
    logger.info("Creating admin if not existed")
    await create_first_admin()
    logger.info("Admin created")

    logger.info("Init clothes sizes")
    await init_clothes_sizes()
    logger.info("Done init clothes sizes")


if __name__ == "__main__":
    asyncio.run(main())
