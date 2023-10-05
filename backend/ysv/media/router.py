import uuid

from aiobotocore.session import get_session
from fastapi import APIRouter, Body, Depends, UploadFile, status

from ysv.config import aws_settings
from ysv.user.deps import current_admin

router = APIRouter()


@router.post("/upload", dependencies=[Depends(current_admin)])
async def upload_media(
    media_file: UploadFile, object_key: str | None = Body(default=None)
):
    s3_region = aws_settings.AWS_S3_REGION
    s3_bucket = aws_settings.AWS_S3_BUCKET
    _, _, ext = media_file.filename.partition(".")  # type: ignore
    if not object_key:
        object_key = f"{str(uuid.uuid4())}.{ext}"
    object_data = media_file.file

    session = get_session()
    async with session.create_client("s3") as client:
        await client.put_object(
            ACL="public-read",
            Bucket=s3_bucket,
            Key=object_key,
            Body=object_data,
            ContentType=media_file.content_type,
        )
    return f"https://{s3_bucket}.s3.{s3_region}.amazonaws.com/{object_key}"


@router.delete(
    "/{media_url}",
    dependencies=[Depends(current_admin)],
    status_code=status.HTTP_200_OK,
)
async def delete_media(media_url: str):
    s3_bucket = aws_settings.AWS_S3_BUCKET
    object_key = media_url

    session = get_session()
    async with session.create_client("s3") as client:
        await client.delete_object(Bucket=s3_bucket, Key=object_key)

    return {"detail": "MEDIA_DELETED"}
