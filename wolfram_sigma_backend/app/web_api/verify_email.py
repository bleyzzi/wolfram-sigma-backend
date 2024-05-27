from fastapi import APIRouter

verify_router = APIRouter(tags=["verify_email"])


@verify_router.get("/verify")
def verify(token: str):
    return {"message": "Email verified successfully"}
