from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from ysv.database.session import get_async_db
from ysv.product.schemas import CollectionProductsRead
from ysv.user.deps import current_admin
from .models import Collection
from .schemas import (
    CollectionCreate,
    CollectionRead,
    CollectionUpdate,
    CollectionAddMain,
    CollectionShowHome,
)

router = APIRouter()


@router.get("/", response_model=list[CollectionProductsRead])
async def read_collection_list(
    *,
    db: AsyncSession = Depends(get_async_db),
):
    collections = (
        await db.scalars(
            select(Collection)
            .where(Collection.is_on_sale)
            .options(selectinload(Collection.products))
            .order_by(Collection.created_at)
        )
    ).all()
    return collections


@router.post("/", dependencies=[Depends(current_admin)], response_model=CollectionRead)
async def create_collection(
    *, db: AsyncSession = Depends(get_async_db), collection_in: CollectionCreate
):
    collection_db = await db.scalar(
        select(Collection).where(Collection.name == collection_in.name)
    )
    if collection_db is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="COLLECTION_NAME_EXISTED"
        )
    collection_obj = Collection(
        name=collection_in.name,
        descriptions=collection_in.descriptions,
        preview_pic=collection_in.preview_pic.unicode_string(),
        is_on_sale=collection_in.is_on_sale,
    )
    db.add(collection_obj)
    await db.commit()
    await db.refresh(collection_obj)

    return collection_obj


@router.get("/{collection_id}", response_model=CollectionRead)
async def read_collection(
    *, db: AsyncSession = Depends(get_async_db), collection_id: str
):
    collection_db = await db.scalar(
        select(Collection).where(Collection.id == collection_id)
    )
    return collection_db


@router.put(
    "/{collection_id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(current_admin)],
)
async def update_collection(
    *,
    db: AsyncSession = Depends(get_async_db),
    collection_id: str,
    collection_data: CollectionUpdate,
):
    collection_db = await db.scalar(
        select(Collection).where(Collection.id == collection_id)
    )
    if collection_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="COLLECTION_NOT_EXISTED"
        )
    collection_db.name = collection_data.name
    collection_db.descriptions = collection_data.descriptions
    collection_db.is_on_sale = collection_data.is_on_sale
    collection_db.preview_pic = collection_data.preview_pic.unicode_string()

    db.add(collection_db)
    await db.commit()

    return {"detail": "COLLECTION_UPDATED"}


@router.delete(
    "/{collection_id}",
    dependencies=[Depends(current_admin)],
    status_code=status.HTTP_200_OK,
)
async def delete_collection(
    *, db: AsyncSession = Depends(get_async_db), collection_id: str
):
    collection_db = await db.scalar(
        select(Collection).where(Collection.id == collection_id)
    )
    if collection_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="COLLECTION_NOT_EXISTED"
        )
    await db.delete(collection_db)
    await db.commit()
    return {"detail": "DELETED_COLLECTION"}


@router.post(
    "/add-main-collection",
    dependencies=[Depends(current_admin)],
    status_code=status.HTTP_200_OK,
)
async def add_main_collection(
    *, db: AsyncSession = Depends(get_async_db), data: CollectionAddMain
):
    existing_main_collection = await db.scalar(
        select(Collection).where(Collection.is_main_collection)
    )
    if existing_main_collection is not None:
        existing_main_collection.is_main_collection = False
        db.add(existing_main_collection)
    new_main_collection = await db.scalar(
        select(Collection).where(Collection.id == data.collection_id)
    )
    new_main_collection.is_main_collection = True  # type:ignore
    new_main_collection.main_collection_description = (  # type:ignore
        data.main_collection_description
    )
    new_main_collection.main_collection_pics = data.main_collection_pics  # type:ignore

    db.add(new_main_collection)
    await db.commit()
    return {"detail": "MAIN_COLLECTION_ADDED"}


@router.post(
    "/add-home-collections",
    dependencies=[Depends(current_admin)],
    status_code=status.HTTP_200_OK,
)
async def add_home_collections(
    *, db: AsyncSession = Depends(get_async_db), data: CollectionShowHome
):
    existing_home_collections = (
        await db.scalars(select(Collection).where(Collection.is_show_in_home))
    ).all()
    for collection in existing_home_collections:
        collection.is_show_in_home = False
        db.add(collection)
    for id in data.collection_ids:
        new_collection = await db.scalar(select(Collection).where(Collection.id == id))
        new_collection.is_show_in_home = True  # type:ignore
        db.add(new_collection)
    await db.commit()
    return {"detail": "HOME_COLLECTIONS_ADDED"}
