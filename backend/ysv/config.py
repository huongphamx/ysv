from pydantic_settings import BaseSettings


class CommonSettings(BaseSettings):
    SECRET_KEY: str = "unsecure-secret-key"
    FRONTEND_DOMAIN: str = "http://localhost:3000"
    REDIS_URL: str = "redis://localhost:6379"
    POSTGRES_URL: str = (
        "postgresql+asyncpg://postgres:mysecretpassword@localhost:5432/eexam"
    )
    ORIGIN_REGEXES: str = "http://.*\.localhost:3000"


class SMTPSettings(BaseSettings):
    MAIL_USERNAME: str = "admin@gmail.com"
    MAIL_PASSWORD: str = "app_password"
    MAIL_FROM: str = "admin@gmail.com"
    MAIL_PORT: int = 587
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_FROM_NAME: str = "Wizzy QR Team"
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True


common_settings = CommonSettings()
smtp_settings = SMTPSettings()
