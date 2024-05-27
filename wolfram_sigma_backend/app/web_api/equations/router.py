from fastapi import APIRouter, Depends

from wolfram_sigma_backend.app.auth.auth import current_user

equations_router = APIRouter(tags=["equation"], dependencies=[Depends(current_user)])
