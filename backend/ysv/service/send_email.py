from pathlib import Path

from fastapi_mail import ConnectionConfig, FastMail
from pydantic import BaseModel, EmailStr

from ysv.config import smtp_settings


class EmailSchema(BaseModel):
    email: list[EmailStr]


conf = ConnectionConfig(
    MAIL_USERNAME=smtp_settings.MAIL_USERNAME,
    MAIL_PASSWORD=smtp_settings.MAIL_PASSWORD,
    MAIL_FROM=smtp_settings.MAIL_FROM,  # type:ignore
    MAIL_PORT=smtp_settings.MAIL_PORT,
    MAIL_SERVER=smtp_settings.MAIL_SERVER,
    MAIL_FROM_NAME=smtp_settings.MAIL_FROM_NAME,
    MAIL_STARTTLS=smtp_settings.MAIL_STARTTLS,
    MAIL_SSL_TLS=smtp_settings.MAIL_SSL_TLS,
    USE_CREDENTIALS=smtp_settings.USE_CREDENTIALS,
    VALIDATE_CERTS=smtp_settings.VALIDATE_CERTS,
    TEMPLATE_FOLDER=Path(__file__).parent.parent / "templates",
)


fm = FastMail(conf)
