from datetime import datetime
from typing import Optional

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, TIMESTAMP, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from wolfram_sigma_backend.app.database.database import Base


class Role(Base):
    __tablename__ = "role"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    permission: Mapped[Optional[str]]


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    username: Mapped[str]
    registered_at: Mapped[Optional[datetime]] = mapped_column(default=datetime.utcnow)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey("role.id"))
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
