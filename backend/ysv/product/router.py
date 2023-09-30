from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from ysv.database.session import get_async_db
from ysv.user.deps import current_admin
from .models import Product
from .schemas import ProductCreate, ProductRead

router = APIRouter()


@router.post("/", dependencies=[Depends(current_admin)], status_code=status.HTTP_200_OK)
async def create_product(
    *, db: AsyncSession = Depends(get_async_db), product_in: ProductCreate
):
    product_data = product_in.model_dump()
    product_obj = Product(**product_data)
    db.add(product_obj)
    await db.commit()
    return {"detail": "PRODUCT_CREATED"}
