from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.models import Room
from app.core.schemas import RoomCreate, RoomOut
from . import router


@router.post("/rooms", response_model=RoomOut, status_code=status.HTTP_201_CREATED)
def create_room(room_data: RoomCreate, db: Session = Depends(get_db)
                # current_user: User = Depends(get_current_user)
                ):
    room = Room(**room_data.dict())#, owner_id=current_user.id)
    db.add(room)
    db.commit()
    db.refresh(room)
    return room


@router.get("/rooms", response_model=List[RoomOut])
def read_rooms(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    rooms = db.query(Room).offset(skip).limit(limit).all()
    return rooms


@router.get("/rooms/{room_id}", response_model=RoomOut)
def read_room(room_id: int, db: Session = Depends(get_db)):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room not found")
    return room


@router.put("/rooms/{room_id}", response_model=RoomOut)
def update_room(room_id: int, room_data: RoomCreate, db: Session = Depends(get_db),
                #current_user: User = Depends(get_current_user)
                ):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room not found")
    # if room.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only the room owner can update the room")

    for field, value in room_data:
        setattr(room, field, value)
    db.commit()
    db.refresh(room)
    return room


@router.delete("/rooms/{room_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_room(room_id: int, db: Session = Depends(get_db),
                # current_user: User = Depends(get_current_user)
                ):
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room not found")
    # if room.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Only the room owner can delete the room")

    db.delete(room)
    db.commit()
