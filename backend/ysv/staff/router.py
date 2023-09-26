import secrets

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ysv.common.utils.security import verify_password
from ysv.database.session import get_async_db
from ysv.service.async_redis import redis_aclient
from ysv.staff.deps import oauth2_scheme
from ysv.staff.models import User

router = APIRouter()


@router.post("/login")
async def login_staff_get_token(
    *,
    db: AsyncSession = Depends(get_async_db),
    credentials: OAuth2PasswordRequestForm = Depends(),
):
    user_db = await db.scalar(select(User).where(User.email == credentials.username))
    if user_db is None or not user_db.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="LOGIN_BAD_CREDENTIALS"
        )
    if not user_db.is_verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="LOGIN_USER_NOT_VERIFIED"
        )
    password_verified = verify_password(credentials.password, user_db.hashed_password)
    if not password_verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="LOGIN_BAD_CREDENTIALS"
        )
    token = secrets.token_urlsafe()
    await redis_aclient.set(f"user_token:{token}", str(user_db.id), ex=3600)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/logout", status_code=status.HTTP_200_OK)
async def logout(token: str = Depends(oauth2_scheme)):
    await redis_aclient.delete(f"user_token:{token}")
    return {"detail": "LOGGED_OUT"}
