from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from wolfram_sigma_backend.app.auth.auth import auth_backend, fastapi_users
from wolfram_sigma_backend.app.domain.auth import UserCreate, UserRead
from wolfram_sigma_backend.app.web_api.routers import routers

app = FastAPI()

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


app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth/jwt",
    tags=["auth"],
)

for router in routers:
    app.include_router(router)


origins = [
    "http://localhost:8000",
    "http://localhost",
    "http://127.0.0.1",
    "http://127.0.0.1:4200",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Access-Control-Allow-Headers",
        "Content-Type",
        "Authorization",
        "Access-Control-Allow-Origin",
        "Set-Cookie",
    ],
)
