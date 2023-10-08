from fastapi import APIRouter

from ysv.collection.router import router as collection_router
from ysv.media.router import router as media_router
from ysv.product.router import router as product_router
from ysv.product.size.router import router as size_router
from ysv.cart.router import router as cart_router
from ysv.user.router import router as user_router
from ysv.order.router import router as order_router

router = APIRouter()

router.include_router(collection_router, prefix="/collections", tags=["collections"])
router.include_router(product_router, prefix="/products", tags=["products"])
router.include_router(size_router, prefix="/sizes", tags=["sizes"])
router.include_router(cart_router, prefix="/carts", tags=["carts"])
router.include_router(media_router, prefix="/media", tags=["media"])
router.include_router(order_router, prefix="/orders", tags=["orders"])
router.include_router(user_router, prefix="/auth", tags=["auth"])
