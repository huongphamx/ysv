from fastapi import APIRouter, Depends, Query, status, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from ysv.database.session import get_async_db
from ysv.product.models import Product
from ysv.product.size.models import ProductSizeVariant, ClothesSize
from .schemas import CartCreate, CartItemUpdate, CartItemCreate
from .models import Cart, CartItem

router = APIRouter()


@router.post("/", status_code=status.HTTP_200_OK)
async def create_cart(*, db: AsyncSession = Depends(get_async_db), cart_in: CartCreate):
    cart_obj = Cart(id=cart_in.cart_id)
    db.add(cart_obj)
    await db.commit()
    return {"detail": "CART_CREATED"}


@router.get("/{cart_id}")
async def get_cart_item_list(*, db: AsyncSession = Depends(get_async_db), cart_id: str):
    cart_items = []
    cart_db = await db.scalar(
        select(Cart).where(Cart.id == cart_id).options(selectinload(Cart.cart_items))
    )
    if cart_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="CART_NOT_EXISTED"
        )
    for item in cart_db.cart_items:
        product_size_variant_id = item.product_size_variant_id
        product_size_variant_db = await db.scalar(
            select(ProductSizeVariant).where(
                ProductSizeVariant.id == product_size_variant_id
            )
        )
        if product_size_variant_db is None:
            continue

        product_db = await db.scalar(
            select(Product)
            .where(Product.id == product_size_variant_db.product_id)
            .options(selectinload(Product.collection))
        )
        if product_db is None:
            continue
        clothes_size_db = await db.scalar(
            select(ClothesSize).where(
                ClothesSize.id == product_size_variant_db.clothes_size_id
            )
        )
        if clothes_size_db is None:
            continue

        cart_items.append(
            {
                "id": item.id,
                "quantity": item.quantity,
                "product_id": product_size_variant_db.product_id,
                "preview_pic": product_db.preview_pic,
                "collection": product_db.collection.name,
                "price": product_db.price,
                "color": product_db.name,
                "size": clothes_size_db.label,
            }
        )
    return cart_items


@router.post("/{cart_id}", status_code=status.HTTP_200_OK)
async def add_cart_item(
    *,
    db: AsyncSession = Depends(get_async_db),
    cart_id: str,
    cart_item_in: CartItemCreate
):
    cart_item_db = await db.scalar(
        select(CartItem)
        .where(CartItem.cart_id == cart_id)
        .where(CartItem.product_size_variant_id == cart_item_in.product_size_variant_id)
    )
    if cart_item_db is None:
        cart_item_obj = CartItem(
            cart_id=cart_id,
            product_size_variant_id=cart_item_in.product_size_variant_id,
            quantity=1,
        )
        db.add(cart_item_obj)
    else:
        cart_item_db.quantity += 1
        db.add(cart_item_db)
    await db.commit()
    return {"detail": "CART_ITEM_ADDED"}


@router.put("/{cart_id}", status_code=status.HTTP_200_OK)
async def update_cart_item(
    *,
    db: AsyncSession = Depends(get_async_db),
    cart_id: str,
    cart_item_data: CartItemUpdate
):
    cart_item_db = await db.scalar(
        select(CartItem).where(CartItem.id == cart_item_data.item_id)
    )
    if cart_item_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="CART_ITEM_NOT_EXISTED"
        )
    if str(cart_item_db.cart_id) != cart_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="CART_ITEM_NOT_CORRECTED"
        )
    if cart_item_data.action == "increase_item":
        cart_item_db.quantity += 1
        db.add(cart_item_db)
    elif cart_item_data.action == "decrease_item":
        if cart_item_db.quantity == 1:
            await db.delete(cart_item_db)
        else:
            cart_item_db.quantity -= 1
            db.add(cart_item_db)
    else:
        await db.delete(cart_item_db)
    await db.commit()
    return {"detail": "CART_ITEM_UPDATED"}
