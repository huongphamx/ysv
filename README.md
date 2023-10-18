## 1. Create S3 PUBLIC Bucket, with:
- Access control list (ACL): Everyone - can Read
- Bucket policy:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:PutObject",
                "s3:PutObjectAcl",
                "s3:GetObject",
                "s3:GetObjectAcl",
                "s3:AbortMultipartUpload"
            ],
            "Resource": [
                "arn:aws:s3:::ysv-dev",
                "arn:aws:s3:::ysv-dev/*"
            ]
        }
    ]
}

then fisrt upload the pics in frontend/public/img to this Bucket.
Note that you need to upload folder: upload all `img` folder at a time.
By that, pic in S3 will have object name with prefix `/img/`

## 2. Create Cloudfront distribution: origin is the bucket above

## 3. Clone the repo, install `docker`, `docker compose` then continue config

## 4. Config docker-compose.env file:

FRONTEND_DOMAIN - the domain of frontend

POSTGRES_URL=postgresql+asyncpg://<user>:<password>@<server>:5432/<db-name>
POSTGRES_USER=<user>
POSTGRES_PASSWORD=<password>
POSTGRES_SERVER=<server>
POSTGRES_DB=<db-name>

FIRST_ADMIN_EMAIL=<email> - this will be client admin email to login
FIRST_ADMIN_PASSWORD=<password> - this will be password to login to admin site. Admin can change password later

AWS_ACCESS_KEY_ID=<aws-access-key-id>
AWS_SECRET_ACCESS_KEY=<aws-secret-access-key>
AWS_S3_REGION=<s3-region>
AWS_S3_BUCKET=<s3-bucket> - bucket name, not whole url
AWS_CLOUDFRONT_DISTRIBUTION_DOMAIN - cloudfront domain
NUXT_PUBLIC_CLOUDFRONT_DISTRIBUTION_DOMAIN - cloudfront domain, same as above but for frontend
NUXT_PUBLIC_API_BASE - the domain where host API. please create a DNS record with name `api`, so we will have for example https://api.domain.com. 
NUXT_PUBLIC_S3_BASE_URL - S3 whole url, for example https://ysv-dev.s3.ap-northeast-1.amazonaws.com

STRIPE_API_KEY=<stripe_api_key>
STRIPE_ENDPOINT_SECRET=<stripe-endpoint-secret>

MAIL_USERNAME=admin-ysv@gmail.com - for SMTP gmail
MAIL_PASSWORD=<app-password> - app password from gmail
MAIL_FROM=admin-ysv@gmail.com - gmail name
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
MAIL_FROM_NAME=<admin-name> - admin name


## 5. Config Caddy server:
Simple replace `pxh-dev.online` in my Caddy file by your domain, and use your email in `tls`
You have to add a DNS record with name `api`, before doing this step.

## 5. Run: 
`docker compose up -d --build`