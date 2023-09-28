from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from ysv.database.base_model import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    pass
