from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.responses import JSONResponse

from app.core.schemas import RoomWithPwd
from app.core.services.security import verify_password, create_access_token
from secrets import compare_digest

router = APIRouter()

security = HTTPBasic()


@router.post("/auth")
# def generate_jwt(room_id: int, password: str):
#     # Validate the password here, and raise an HTTPException if it's invalid
#     is_valid_password = True
#     if not is_valid_password:
#         raise HTTPException(status_code=401, detail="Invalid password")
#
#     # Generate the JWT here
#     payload = {"room_id": room_id}
#     jwt_token = create_access_token(payload)
#
#     # Return the JWT as a JSON response
#     return JSONResponse({"jwt": jwt_token})

# def authenticate(
#         credentials: HTTPBasicCredentials = Depends(security)
# ):
#     if not verify_password(credentials.username, credentials.password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#         )
#     return {"access_token": create_access_token(credentials.username)}
# async def authenticate(room: RoomWithPwd):
#     target = get_room_by_id(room.id)
#     if room.id in target and compare_digest(room.password, target.password):
#         return True
async def authenticate(room: RoomWithPwd):
    pass
