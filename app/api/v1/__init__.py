from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1",
    tags=["v1"],
)

from . import auth, lobby, room
