import uuid
from typing import List, Type

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.services.security import verify_password
from app.core.schemas import Room, RoomCreate, RoomUpdate, Track, RoomWithPwd, TrackCreate, TrackResponse

from app.core.models import Room as RoomModel, Track as TrackModel


def create_room(db: Session, room: RoomCreate) -> Room:
    """
    Creates a new room and returns it
    """
    db_room = RoomModel(name=room.name, password=room.password)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return Room.from_orm(db_room)


def get_rooms(db: Session, skip: int = 0, limit: int = 100) -> List:
    """
    Returns a list of all rooms
    """
    return db.query(RoomModel).offset(skip).limit(limit).all()


def get_room_by_uuid(db: Session, room_id: uuid.UUID) -> Room:
    """
    Returns the room with the specified ID, or raises an HTTPException if the room is not found
    """
    return db.query(RoomModel).filter(RoomModel.id == room_id).first()


def get_room_by_name(db: Session, name: str) -> Room:
    """
    Returns the room with the specified name
    """
    return db.query(RoomModel).filter(RoomModel.name == name).first()


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
    Deletes a room and its tracks
    """
    db.query(TrackModel).filter(TrackModel.room_id == room.id).delete()
    db.delete(room)
    db.commit()


# def join_room(db: Session, room: Room, password: str) -> Room:
#     """
#     Joins a room and returns it
#     """
#     if not verify_password(password, room.password):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
#     return room


def get_tracks(db: Session, room: Room) -> List:
    """
    Returns a list of all tracks in a room
    """
    tracks = db.query(TrackModel).filter(TrackModel.room_id == room.id).all()
    return [TrackResponse.from_orm(track) for track in tracks]


def add_track(db: Session, room: Room, track: Track) -> TrackCreate:
    """
    Adds a track to a room and returns it
    """
    added_track = TrackModel(
        title=track.title,
        # artist=track.artist,
        uri=track.uri,
        room_id=room.id
    )
    db.add(added_track)
    db.commit()
    db.refresh(added_track)
    return TrackCreate.from_orm(added_track)
