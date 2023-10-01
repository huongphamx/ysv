from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from ysv.database.session import get_async_db
from ysv.user.deps import current_admin
from .models import Product, ProductPicture
from .schemas import ProductCreate, ProductRead, ProductDetailRead, ProductUpdate

router = APIRouter()


@router.get("/", response_model=list[ProductRead])
async def read_product_list(*, db: AsyncSession = Depends(get_async_db)):
    products = (
        await db.scalars(select(Product).options(selectinload(Product.collection)))
    ).all()
    return products


@router.post("/", dependencies=[Depends(current_admin)], status_code=status.HTTP_200_OK)
async def create_product(
    *, db: AsyncSession = Depends(get_async_db), product_in: ProductCreate
):
    product_obj = Product(
        collection_id=product_in.collection_id,
        name=product_in.name,
        is_available=product_in.is_available,
        price=product_in.price,
        descriptions=product_in.descriptions,
        preview_pic=product_in.preview_pic,
    )
    for url in product_in.pictures:
        picture_obj = ProductPicture(url=url)
        product_obj.pictures.append(picture_obj)

    db.add(product_obj)
    await db.commit()
    return {"detail": "PRODUCT_CREATED"}


@router.get("/{product_id}", response_model=ProductDetailRead)
async def read_product(*, db: AsyncSession = Depends(get_async_db), product_id: str):
    product_db = await db.scalar(
        select(Product)
        .where(Product.id == product_id)
        .options(selectinload(Product.collection))
        .options(selectinload(Product.pictures))
    )
    if product_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="PRODUCT_NOT_EXISTED"
        )
    return product_db


@router.put(
    "/{product_id}",
    dependencies=[Depends(current_admin)],
    status_code=status.HTTP_200_OK,
)
async def update_product(
    *,
    db: AsyncSession = Depends(get_async_db),
    product_id: str,
    product_data: ProductUpdate
):
    product_db = await db.scalar(
        select(Product)
        .where(Product.id == product_id)
        .options(selectinload(Product.pictures))
    )
    if product_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="PRODUCT_NOT_EXISTED"
        )
    product_db.collection_id = product_data.collection_id
    product_db.name = product_data.name
    product_db.is_available = product_data.is_available
    product_db.price = product_data.price
    product_db.descriptions = product_data.descriptions
    product_db.preview_pic = product_data.preview_pic

    existing_pictures = (
        await db.scalars(
            select(ProductPicture).where(ProductPicture.product_id == product_id)
        )
    ).all()
    existing_picture_urls = [pic.url for pic in existing_pictures]
    to_add_picture_urls = [
        url for url in product_data.pictures if url not in existing_picture_urls
    ]
    for url in to_add_picture_urls:
        picture_obj = ProductPicture(url=url)
        product_db.pictures.append(picture_obj)

    db.add(product_db)
    await db.commit()

    return {"detail": "PRODUCT_UPDATED"}


@router.delete(
    "/{product_id}",
    dependencies=[Depends(current_admin)],
    status_code=status.HTTP_200_OK,
)
async def delete_product(*, db: AsyncSession = Depends(get_async_db), product_id: str):
    product_db = await db.scalar(select(Product).where(Product.id == product_id))
    if product_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="PRODUCT_NOT_EXISTED"
        )
    await db.delete(product_db)

    return {"detail": "PRODUCT_DELETED"}
