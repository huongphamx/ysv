import stripe
from fastapi import APIRouter, Depends, Header, HTTPException, Query, Request, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from ysv.cart.models import Cart
from ysv.config import common_settings, stripe_settings
from ysv.database.session import get_async_db
from ysv.product.models import Product
from ysv.product.size.models import ProductSizeVariant
from ysv.user.deps import current_admin

from .models import Order, OrderItem
from .schemas import OrderCreate, OrderRead, OrderUpdate

router = APIRouter()

stripe.api_key = stripe_settings.STRIPE_API_KEY


@router.post("/")
async def create_order(
    *, db: AsyncSession = Depends(get_async_db), order_in: OrderCreate
):
    # create order
    order_obj = Order(
        fname=order_in.fname,
        lname=order_in.lname,
        country=order_in.country,
        city=order_in.city,
        state=order_in.state,
        street_address=order_in.street_address,
        zip_code=order_in.zip_code,
        phone_number=order_in.phone_number,
        cart_id=order_in.cart_id,
        is_paid=False,
        is_delivered=False,
    )
    cart_db = await db.scalar(
        select(Cart)
        .where(Cart.id == order_in.cart_id)
        .options(selectinload(Cart.cart_items))
    )
    for cart_item in cart_db.cart_items:  # type:ignore
        # add order item
        order_item_obj = OrderItem(
            product_size_variant_id=cart_item.product_size_variant_id,
            quantity=cart_item.quantity,
        )
        order_obj.order_items.append(order_item_obj)

    db.add(order_obj)
    await db.commit()
    await db.refresh(order_obj)

    # create checkout session
    total_price = 0
    for cart_item in cart_db.cart_items:  # type:ignore
        # calculate total price
        product_size_variant_id = cart_item.product_size_variant_id
        product_size_variant_db = await db.scalar(
            select(ProductSizeVariant).where(
                ProductSizeVariant.id == product_size_variant_id
            )
        )
        if product_size_variant_db is None:
            continue
        product_db = await db.scalar(
            select(Product)
            .where(Product.id == product_size_variant_db.product_id)
            .options(selectinload(Product.collection))
        )
        if product_db is None:
            continue
        total_price += product_db.price * cart_item.quantity

    shipping_fee = 5 if order_in.country == "United Arab Emirates" else 20
    pay_amount = total_price + shipping_fee
    try:
        checkout_session = stripe.checkout.Session.create(
            client_reference_id=order_obj.id,
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": "Payment YSV",
                            "description": "YSV Order",
                        },
                        "unit_amount": pay_amount * 100,
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=common_settings.FRONTEND_DOMAIN + "/payment-success",
            cancel_url=common_settings.FRONTEND_DOMAIN + "/payment-cancel",
        )
        checkout_url = checkout_session.url
        return {"checkout_url": checkout_url}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/", dependencies=[Depends(current_admin)], response_model=list[OrderRead])
async def get_order_list(*, db: AsyncSession = Depends(get_async_db)):
    orders = (await db.scalars(select(Order).order_by(Order.created_at.desc()))).all()
    return orders


@router.put(
    "/{order_id}", dependencies=[Depends(current_admin)], status_code=status.HTTP_200_OK
)
async def update_order(
    *, db: AsyncSession = Depends(get_async_db), order_id: str, order_data: OrderUpdate
):
    order_db = await db.scalar(select(Order).where(Order.id == order_id))
    if order_db is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="ORDER_NOT_EXISTED"
        )
    order_db.is_delivered = order_data.is_delivered
    db.add(order_db)
    await db.commit()
    return {"detail": "ORDER_UPDATED"}


@router.post("/stripe-webhook")
async def stripe_webhook(
    *,
    request: Request,
    STRIPE_SIGNATURE: str | None = Header(default=None),
    db: AsyncSession = Depends(get_async_db),
):
    endpoint_secret = stripe_settings.STRIPE_ENDPOINT_SECRET
    payload = await request.body()
    try:
        event = stripe.Webhook.construct_event(
            payload, STRIPE_SIGNATURE, endpoint_secret
        )
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="INVALID_PAYLOAD"
        )
    except stripe.error.SignatureVerificationError as e:
        # raise HTTPException(

        #     status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid signature"
        # )
        raise e
    if event["type"] == "checkout.session.async_payment_failed":
        session = event["data"]["object"]
    elif event["type"] == "checkout.session.async_payment_succeeded":
        session = event["data"]["object"]
        # order_id = session["client_reference_id"]
        # order_db = await db.scalar(select(Order).where(Order.id == order_id))
        # order_db.is_paid = True  # type:ignore
        # db.add(order_db)

        # remove cart item
        # cart_db = await db.scalar(
        #     select(Cart).where(Cart.id == order_db.cart_id)  # type:ignore
        # )
        # cart_db.cart_items = []  # type:ignore
        # db.add(cart_db)
        await db.commit()
    elif event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        order_id = session["client_reference_id"]
        order_db = await db.scalar(select(Order).where(Order.id == order_id))
        order_db.is_paid = True  # type:ignore
        db.add(order_db)
        # remove cart item
        cart_db = await db.scalar(
            select(Cart)
            .where(Cart.id == order_db.cart_id)  # type:ignore
            .options(selectinload(Cart.cart_items))
        )
        cart_db.cart_items = []  # type:ignore
        db.add(cart_db)
        await db.commit()
    elif event["type"] == "checkout.session.expired":
        session = event["data"]["object"]
