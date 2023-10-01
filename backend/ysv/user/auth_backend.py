from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)

from ysv.config import common_settings

bearer_transport = BearerTransport(tokenUrl="/api/v1/auth/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=common_settings.SECRET_KEY, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
