import uuid

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.services import security
from app.core.database import get_db
from app.core.services import room as room_service
from app.core.schemas import Room, RoomCreate, RoomUpdate, Track, TrackCreate, TrackResponse

from . import router


@router.post("/", response_model=Room)
def create_room(
    room: RoomCreate,
    db: Session = Depends(get_db),
    # current_user: str = Depends(security.get_current_user),
) -> Room:
    """Create a new music room"""
    # check if the room name is unique
    if room_service.get_room_by_name(db, room.name):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The room name is already taken.",
        )
    # create the new room
    return room_service.create_room(db, room)


@router.get("/rooms", response_model=List[Room])
def get_rooms(
    db: Session = Depends(get_db),
    # current_user: str = Depends(security.get_current_user),
) -> List[Room]:
    """Get a list of music rooms"""
    return room_service.get_rooms(db)


@router.get("/{room_id}")
# def enter_room(
#     room_id: uuid.UUID,
#     db: Session = Depends(get_db),
#     current_user: str = Depends(security.get_current_user)
# ):
#     # get the room
#     room = room_service.get_room(db, room_id)
#     # check if the user is authorized to access the room
#     if not security.is_authorized(room.password, current_user):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="You are not authorized to access this room.",
#         )
#     return {"message": "Welcome to the room!"}
def enter_room(
    room_id: uuid.UUID,
    db: Session = Depends(get_db),
    # current_user: str = Depends(security.get_current_user)
):
    # get the room
    room = room_service.get_room_by_uuid(db, room_id)
    return {"message": "Welcome to the room!"}


@router.put("/{room_id}", response_model=RoomUpdate)
# def update_room(
#     room_id: uuid.UUID,
#     room: RoomUpdate,
#     db: Session = Depends(get_db),
#     current_user: str = Depends(security.get_current_user),
# ) -> Room:
#     """Update details of a music room"""
#     existing_room = room_service.get_room(db, room_id)
#     # check if the user is authorized to modify the room
#     if not security.is_authorized(existing_room.password, current_user):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="You are not authorized to modify this room.",
#         )
#     return room_service.update_room(db, existing_room, room)
def update_room(
    room_id: uuid.UUID,
    room: RoomUpdate,
    db: Session = Depends(get_db),
    # current_user: str = Depends(security.get_current_user),
) -> Room:
    """Update details of a music room"""
    existing_room = room_service.get_room_by_uuid(db, room_id)
    return room_service.update_room(db, existing_room, room)


@router.get("/{room_id}/queue", response_model=List[TrackResponse])
def get_queue(
    room_id: uuid.UUID,
    db: Session = Depends(get_db),
    # current_user: str = Depends(security.get_current_user),
) -> List[TrackResponse]:
    """Get the current music queue of a music room"""
    room = room_service.get_room_by_uuid(db, room_id)
    if not room:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The room does not exist.",
        )
    # check if the user is authorized to access the room
    # if not security.is_authorized(room.password, current_user):
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="You are not authorized to access this room.",
    #     )
    return room_service.get_tracks(db, room)


@router.post("/{room_id}/queue", response_model=TrackCreate)
def add_music_to_queue(
    room_id: uuid.UUID,
    track: TrackCreate,
    db: Session = Depends(get_db),
    # current_user: str = Depends(security.get_current_user),
) -> TrackCreate:
    """Add a new music to the queue of a music room"""
    room = room_service.get_room_by_uuid(db, room_id)
    # check if the user is authorized to modify the room
    # if not security.is_authorized(room.password, current_user):
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="You are not authorized to modify this room.",
    #     )
    # create the new music and add it to the queue
    new_track = Track(
        title=track.title,
        # artist=track.artist,
        uri=track.uri,
    )
    return room_service.add_track(db, room, new_track)

