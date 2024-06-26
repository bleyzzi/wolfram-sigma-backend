import uuid
from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Boolean, ForeignKey, Integer, String, types
from sqlalchemy.orm import Mapped, mapped_column

from wolfram_sigma_backend.app.persistence.database_config import Base


class Role(Base):
    __tablename__ = "role"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    permission: Mapped[str | None]


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"

    id: Mapped[uuid.UUID] = mapped_column(types.Uuid, primary_key=True, default=uuid.uuid4)
    email: Mapped[str]
    username: Mapped[str]
    registered_at: Mapped[datetime | None] = mapped_column(default=datetime.utcnow)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey("role.id"))
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)


class UserVerify(Base):
    __tablename__ = "user_verify"

    user_id: Mapped[uuid.UUID] = mapped_column(types.Uuid, ForeignKey("user.id"), primary_key=True)
    token: Mapped[str] = mapped_column(String, default="0000")
    is_token_active: Mapped[bool] = mapped_column(Boolean, default=False)
