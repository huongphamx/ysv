from datetime import datetime, timedelta
from typing import Any

import jwt
from passlib.context import CryptContext

JWT_ALGORITHM = "HS256"
context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain_password: str):
    return context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str):
    return context.verify(plain_password, hashed_password)


def generate_jwt(
    data: dict,
    secret: str,  # todo: why this maybe SecretStr in fastapi-users?
    lifetime_seconds: int | None = None,
    algorithm: str = JWT_ALGORITHM,
) -> str:
    payload = data.copy()
    if lifetime_seconds:
        expire = datetime.utcnow() + timedelta(seconds=lifetime_seconds)
        payload["exp"] = expire
    return jwt.encode(payload, secret, algorithm=algorithm)


def decode_jwt(
    encoded_jwt: str,
    secret: str,
    audience: list[str],
    algorithms: list[str] = [JWT_ALGORITHM],
) -> dict[str, Any]:
    return jwt.decode(
        encoded_jwt,
        secret,
        audience=audience,
        algorithms=algorithms,
    )
