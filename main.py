from fastapi import Depends
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_users import FastAPIUsers

from wolfram_sigma_backend.app.auth.auth import auth_backend
from wolfram_sigma_backend.app.auth.auth import current_user
from wolfram_sigma_backend.app.auth.manager import get_user_manager
from wolfram_sigma_backend.app.auth.models import User
from wolfram_sigma_backend.app.auth.schemas import UserCreate
from wolfram_sigma_backend.app.auth.schemas import UserRead

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

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:8080",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"
