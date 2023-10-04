from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from ysv.database.session import get_async_db
from ysv.product.models import Product
from ysv.product.size.models import ProductSizeVariant, ClothesSize


router = APIRouter()


@router.get("/items/")
async def get_cart_item_list(
    *, db: AsyncSession = Depends(get_async_db), ids: list = Query(default=[])
):
    items = []
    for id in ids:
        product_size_variant_db = await db.scalar(
            select(ProductSizeVariant).where(ProductSizeVariant.id == id)
        )
        if product_size_variant_db is None:
            return None
        product = await db.scalar(
            select(Product)
            .where(Product.id == product_size_variant_db.product_id)
            .options(selectinload(Product.collection))
        )
        if product is None:
            return None
        clothes_size = await db.scalar(
            select(ClothesSize).where(
                ClothesSize.id == product_size_variant_db.clothes_size_id
            )
        )
        if clothes_size is None:
            return None
        items.append(
            {
                "id": id,
                "preview_pic": product.preview_pic,
                "collection": product.collection.name,
                "price": product.price,
                "color": product.name,
                "size": clothes_size.label,
            }
        )
    return items


@router.get("/items/{product_size_variant_id}")
async def get_cart_item(
    *, db: AsyncSession = Depends(get_async_db), product_size_variant_id: str
):
    product_size_variant_db = await db.scalar(
        select(ProductSizeVariant).where(
            ProductSizeVariant.id == product_size_variant_id
        )
    )
    if product_size_variant_db is None:
        return None
    product = await db.scalar(
        select(Product)
        .where(Product.id == product_size_variant_db.product_id)
        .options(selectinload(Product.collection))
    )
    if product is None:
        return None
    clothes_size = await db.scalar(
        select(ClothesSize).where(
            ClothesSize.id == product_size_variant_db.clothes_size_id
        )
    )
    if clothes_size is None:
        return None
    return {
        "id": product_size_variant_id,
        "preview_pic": product.preview_pic,
        "collection": product.collection.name,
        "price": product.price,
        "color": product.name,
        "size": clothes_size.label,
    }
