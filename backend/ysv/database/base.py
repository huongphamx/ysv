# Import all the models, so that Alembic can read from memory
# and auto generate migration
# https://stackoverflow.com/questions/15660676/alembic-autogenerate-producing-empty-migration
from ysv.database.base_model import Base  # noqa:F401
from ysv.user.models import User  # noqa:F401
from ysv.collection.models import Collection  # noqa:F401
from ysv.product.size.models import ClothesSize, ProductSizeVariant  # noqa:F401
from ysv.product.models import Product, ProductPicture  # noqa:F401
