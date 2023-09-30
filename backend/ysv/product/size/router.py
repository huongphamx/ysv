from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ysv.database.session import get_async_db
from .models import ClothesSize
from .schemas import ClothSizeRead

router = APIRouter()


@router.get("/", response_model=list[ClothSizeRead])
async def read_cloth_size_list(*, db: AsyncSession = Depends(get_async_db)):
    sizes = (await db.scalars(select(ClothesSize))).all()
    return sizes
