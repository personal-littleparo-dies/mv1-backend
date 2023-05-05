from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.services.security import verify_password
from app.core.schemas import RoomCreate, RoomUpdate
from app.core.models import Room


def create_room(db: Session, room: RoomCreate) -> Room:
    """
    Creates a new room and returns it
    """
    db_room = Room(name=room.name, password=room.password)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room


def get_rooms(db: Session, skip: int = 0, limit: int = 100) -> List[Room]:
    """
    Returns a list of all rooms
    """
    return db.query(Room).offset(skip).limit(limit).all()


def get_room_by_id(db: Session, room_id: int) -> Room:
    """
    Returns the room with the specified ID, or raises an HTTPException if the room is not found
    """
    room = db.query(Room).filter(Room.id == room_id).first()
    if not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room not found")
    return room


def update_room(db: Session, room: Room, room_update: RoomUpdate) -> Room:
    """
    Updates a room and returns it
    """
    if room_update.password:
        room.password = room_update.password
    db.commit()
    db.refresh(room)
    return room


def delete_room(db: Session, room: Room):
    """
    Deletes a room
    """
    db.delete(room)
    db.commit()


def join_room(room_id: int, password: str):
    """
    Joins a room if the password is correct
    """
    db = next(get_db())
    room = get_room_by_id(db, room_id)
    if not verify_password(password, room.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    return room
