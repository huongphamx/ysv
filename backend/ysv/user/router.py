from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_users.password import PasswordHelper
from sqlalchemy.ext.asyncio import AsyncSession

from ysv.database.session import get_async_db
from ysv.user.deps import current_admin

from .auth_backend import auth_backend
from .user_manager import app_users
from .models import User
from .schemas import UserPasswordUpdate

router = APIRouter()
password_helper = PasswordHelper()

router.include_router(
    app_users.get_auth_router(auth_backend),
)


@router.patch("/change-password", status_code=status.HTTP_200_OK)
async def change_password(
    *,
    db: AsyncSession = Depends(get_async_db),
    admin_user: User = Depends(current_admin),
    password_data: UserPasswordUpdate
):
    verified, updated_password_hash = password_helper.verify_and_update(
        password_data.old_password, admin_user.hashed_password
    )
    if not verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="BAD_CREDENTIALS"
        )
    if updated_password_hash is not None:
        admin_user.hashed_password = updated_password_hash

    if password_data.new_password == password_data.old_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="BAD_PASSWORD"
        )

    admin_user.hashed_password = password_helper.hash(password_data.new_password)
    db.add(admin_user)
    await db.commit()
    return {"detail": "PASSWORD_UPDATED"}
