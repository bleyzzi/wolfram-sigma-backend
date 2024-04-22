from typing import Any, Dict

from fastapi import APIRouter, HTTPException, Depends

from wolfram_sigma_backend.app.auth.auth import current_user
from wolfram_sigma_backend.app.auth.models import User

test_router = APIRouter()


@test_router.get("/unprotected-route")
async def unprotected_route():
    return {'name': 'Ivan'}


@test_router.get("/protected-route")
async def protected_route(user: User = Depends(current_user)):
    return f'{user.id}\n{user.username}\n{user.email}'


