import stripe
from fastapi import APIRouter, HTTPException, status

from ysv.config import stripe_settings, common_settings

stripe.api_key = stripe_settings.STRIPE_API_KEY

router = APIRouter()


@router.post("/create-checkout-session")
async def create_checkout_session():
    # todo: get total price from items id and shipping fee
    # todo: create order, or create after payment success? maybe need to add id to verify payment success
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": "Payment YSV",
                            "description": "Description",
                            "images": [
                                "https://b.stripecdn.com/docs-statics-srv/assets/e9d184fcb37d32f21df2171a070f5fbc.png"
                            ],
                        },
                        "unit_amount": 300 * 100,
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=common_settings.FRONTEND_DOMAIN + "/payment-success",
            cancel_url=common_settings.FRONTEND_DOMAIN + "/payment-cancel",
        )
        checkout_url = checkout_session.url
        return {"detail": checkout_url}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
