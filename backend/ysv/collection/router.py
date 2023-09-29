from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ysv.database.session import get_async_db
from ysv.user.deps import current_admin
from .models import Collection
from .schemas import CollectionCreate, CollectionRead

router = APIRouter()


@router.get("/", response_model=list[CollectionRead])
async def read_collection_list(
    *,
    db: AsyncSession = Depends(get_async_db),
):
    # todo: add filter to return first 13 collections
    # todo: order by???
    collections = (await db.scalars(select(Collection).order_by(Collection.name))).all()
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
