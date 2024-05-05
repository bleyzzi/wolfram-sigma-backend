import uuid

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: uuid.UUID
    email: str
    username: str
    role_id: int

    class Config:
        from_attributes = True


class UserEditSchema(BaseModel):
    username: str
    email: str


class UserGetSchema(BaseModel):
    id: uuid.UUID
