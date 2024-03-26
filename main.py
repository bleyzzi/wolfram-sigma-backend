from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers

from wolfram_sigma_backend.app.auth.auth import auth_backend, current_user
from wolfram_sigma_backend.app.auth.manager import get_user_manager
from wolfram_sigma_backend.app.auth.models import User
from wolfram_sigma_backend.app.auth.schemas import UserRead, UserCreate

app = FastAPI()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"
