from fastapi import APIRouter

from ysv.collection.router import router as collection_router
from ysv.media.router import router as media_router
from ysv.user.router import router as user_router

router = APIRouter()

router.include_router(collection_router, prefix="/collections", tags=["collections"])
router.include_router(media_router, prefix="/media", tags=["media"])
router.include_router(user_router, prefix="/auth", tags=["auth"])
