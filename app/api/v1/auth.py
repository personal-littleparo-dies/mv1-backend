from fastapi import Depends, HTTPException, status
from app.core.services.security import create_room_access_token
from app.core.database import get_db
from . import router


@router.post("/room_token")
async def get_room_token(room_password: str, db: Session = Depends(get_db)):
    """
    Endpoint to generate a room access token for a given room password.
    """
    room = db.query(Room).filter(Room.password == room_password).first()
    if not room:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid room password")
    room_token = create_room_access_token(room.id)
    return {"room_token": room_token, "token_type": "bearer"}
