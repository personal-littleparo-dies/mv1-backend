from typing import List, Optional
from pydantic import BaseModel


class MusicQueue(BaseModel):
    id: str
    name: str
    artist: str


class RoomCreate(BaseModel):
    pass

class RoomUpdate:
    pass

class RoomIn(BaseModel):
    name: str
    password: str


class RoomOut(BaseModel):
    id: str
    name: str


class Room(BaseModel):
    id: str
    name: str
    password: Optional[str] = None
    music_queue: List[MusicQueue] = []


class LobbyCreate(BaseModel):
    name: str
    password: str


class LobbyUpdate(BaseModel):
    name: Optional[str] = None
    password: Optional[str] = None


class Lobby(BaseModel):
    id: str
    name: str
    password: Optional[str] = None
    rooms: List[Room] = []


