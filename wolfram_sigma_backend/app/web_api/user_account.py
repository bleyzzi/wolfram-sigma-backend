from typing import Dict, Any

from fastapi import APIRouter, Depends

from wolfram_sigma_backend.app.auth.auth import current_user
from wolfram_sigma_backend.app.domain.user_account import UserEditSchema, UserSchema, UserGetSchema
from wolfram_sigma_backend.app.models.auth_models import User
from wolfram_sigma_backend.app.persistence.service.user import UserService

user_account_page = APIRouter(
    tags=["user-account"],
    dependencies=[Depends(current_user)]
)


@user_account_page.get('/get_user_account_info')
async def get_user_account_info(
        user: User = Depends(current_user)
) -> UserSchema:
    user_get = await UserService.get_user(user.id)
    return user_get


@user_account_page.put('/edit_user_account')
async def edit_user_account(
        user_schema: UserEditSchema,
        user: User = Depends(current_user)
) -> UserSchema:
    user_put = await UserService.edit_user(user.id, user_schema)
    return user_put
