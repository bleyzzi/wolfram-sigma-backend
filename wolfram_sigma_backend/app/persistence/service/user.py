from wolfram_sigma_backend.app.domain.user_account import UserEditSchema, UserSchema
from wolfram_sigma_backend.app.persistence.database_config import get_async_session
from wolfram_sigma_backend.app.persistence.repository.user import UserRepository


class UserService:
    @staticmethod
    async def edit_user(user_id: int, user: UserEditSchema) -> UserSchema:
        user_dict = user.model_dump()
        session = get_async_session()
        res = await UserRepository(await anext(session)).edit_one(user_id, user_dict)
        return UserSchema.model_validate(res)

    @staticmethod
    async def get_user(user_id) -> UserSchema:
        session = get_async_session()
        res = await UserRepository(await anext(session)).find_one(id=user_id)
        return UserSchema.model_validate(res)
