from pydantic_settings import BaseSettings


class CommonSettings(BaseSettings):
    SECRET_KEY: str = "unsecure-secret-key"
    FRONTEND_DOMAIN: str = "http://localhost:3000"
    REDIS_URL: str = "redis://localhost:6379"
    POSTGRES_URL: str = (
        "postgresql+asyncpg://postgres:mysecretpassword@localhost:5432/ysv"
    )
    FIRST_ADMIN_EMAIL: str = "admin@example.com"
    FIRST_ADMIN_PASSWORD: str = "password"


class AwsSettings(BaseSettings):
    AWS_S3_REGION: str
    AWS_S3_BUCKET: str
    AWS_CLOUDFRONT_DISTRIBUTION_DOMAIN: str


class StripeSettings(BaseSettings):
    STRIPE_API_KEY: str
    STRIPE_ENDPOINT_SECRET: str


class SMTPSettings(BaseSettings):
    MAIL_USERNAME: str = "admin-ysv@gmail.com"
    MAIL_PASSWORD: str = "app_password"
    MAIL_FROM: str = "admin-ysv@gmail.com"
    MAIL_PORT: int = 587
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_FROM_NAME: str = "YSV"
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True


common_settings = CommonSettings()
aws_settings = AwsSettings()  # type:ignore
stripe_settings = StripeSettings()  # type:ignore
smtp_settings = SMTPSettings()
