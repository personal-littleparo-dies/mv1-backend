import dataclasses
import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime, Text, func, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


@dataclasses.dataclass
class MusicLoungeRoom(Base):
    __tablename__ = "music_lounge_room"

    roomCode: uuid.UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    roomName: str = Column(String(255), nullable=False)
    description: str = Column(Text, nullable=False, default="a placeholder description")


@dataclasses.dataclass
class MusicQueue(Base):
    __tablename__ = "music_queue"

    # id: uuid.UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # roomCode: uuid.UUID = Column(UUID(as_uuid=True), nullable=False)
    songName: str = Column(String(255), nullable=False)
    # artistName: str = Column(String(255), nullable=False)
    # albumName: str = Column(String(255), nullable=False)
    # albumArtUrl: str = Column(String(255), nullable=False)
    songUrl: str = Column(String(255), nullable=False)
    # duration: float = Column(Double, nullable=False)
    addedAt: datetime = Column(DateTime, nullable=False, default=func.now())
    # addedBy: str = Column(String(255), nullable=False)

# @dataclasses.dataclass
# class User(Base):
#     __tablename__ = "user"
#
#     id: uuid.UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     username: str = Column(String(255), nullable=False)
#     email: str = Column(String(255), nullable=False)
#     password: str = Column(String(255), nullable=False)
#     created_at: datetime = Column(DateTime, nullable=False, default=func.now())
#     updated_at: datetime = Column(DateTime, nullable=False, default=func.now())
#     last_login: datetime = Column(DateTime, nullable=False, default=func.now())
#     is_active: bool = Column(DateTime, nullable=False, default=True)
