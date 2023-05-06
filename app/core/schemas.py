import uuid
from typing import List, Optional
from pydantic import BaseModel


# Schema for a music track
class TrackBase(BaseModel):
    title: str
    # artist: str

    class Config:
        orm_mode = True


# Schema for a music track with an id
class Track(TrackBase):
    uri: str


# Schema for creating a music track
class TrackCreate(Track):
    room_id: uuid.UUID


class TrackResponse(Track):
    id: int


# Schema for a room
class RoomBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


# Schema for creating a room
class RoomCreate(RoomBase):
    password: str


# Schema for updating a room
class RoomUpdate(RoomBase):
    password: Optional[str] = None


# Schema for a room with tracks
class Room(RoomBase):
    id: uuid.UUID
    tracks: List[Track] = []


class RoomWithPwd(Room):
    password: str


# Schema for a list of rooms
class Rooms(List[Room]):
    pass


class TokenData(BaseModel):
    username: Optional[str] = None
