from fastapi import APIRouter

from .auth_backend import auth_backend
from .user_manager import app_users

router = APIRouter()

router.include_router(
    app_users.get_auth_router(auth_backend),
)
router.include_router(
    app_users.get_reset_password_router(),
)
