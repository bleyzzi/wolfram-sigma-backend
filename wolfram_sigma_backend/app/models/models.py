import uuid

from datetime import datetime
from typing import Optional

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, String, Boolean, ForeignKey, types
from sqlalchemy.orm import Mapped, mapped_column

from wolfram_sigma_backend.app.database.database import Base


class Params(Base):
    __tablename__ = "params"

    id: Mapped[int] = mapped_column(primary_key=True)
    language: Mapped[str] = mapped_column(String, nullable=False)
    threads: Mapped[int] = mapped_column(Integer, default=1, nullable=False)


class Equation(Base):
    __tablename__ = "equation"

    id: Mapped[int] = mapped_column(primary_key=True)
    expression: Mapped[str] = mapped_column(String, nullable=False)
    result: Mapped[str] = mapped_column(String, nullable=False)
    params: Mapped[int] = mapped_column(Integer, ForeignKey("params.id"))
    created_at: Mapped[Optional[datetime]] = mapped_column(default=datetime.utcnow)


class Equation_User(Base):
    __tablename__ = "equation_user"

    user_id: Mapped[int] =  mapped_column(Integer, ForeignKey("user.id"))
    equation_id: Mapped[int] = mapped_column(Integer, ForeignKey("equation.id"))