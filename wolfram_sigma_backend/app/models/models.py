import uuid

from datetime import datetime
from typing import Optional

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, String, Boolean, ForeignKey, types
from sqlalchemy.orm import Mapped, mapped_column

from wolfram_sigma_backend.app.database.database import Base


class Equation(Base):
    __tablename__ = "equation"

    id: Mapped[int] = mapped_column(primary_key=True)
    expression: Mapped[str]
    result: Mapped[str]
    params: Mapped[str]
    created_at: Mapped[Optional[datetime]] = mapped_column(default=datetime.utcnow)


class Equation_User(Base):
    __tablename__ = "equation_user"

    user_id: Mapped[int] =  mapped_column(Integer, ForeignKey("user.id"))
    equation_id: Mapped[int] = mapped_column(Integer, ForeignKey("equation.id"))