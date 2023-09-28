from fastapi import APIRouter

from ysv.media.router import router as media_router
from ysv.user.router import router as user_router

router = APIRouter()

router.include_router(media_router, prefix="/media", tags=["media"])
router.include_router(user_router, prefix="/auth", tags=["auth"])
