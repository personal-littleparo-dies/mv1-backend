# import dataclasses
# import uuid
# from datetime import datetime
#
# from sqlalchemy import Column, String, DateTime, Text, func, UUID
# from sqlalchemy.ext.declarative import declarative_base
import uuid

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base


# class Lobby(Base):
#     __tablename__ = "lobbies"
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, index=True)
#     password = Column(String)
#
#     # Define one-to-many relationship with Room model
#     rooms = relationship("Room", back_populates="lobby")


class Room(Base):
    __tablename__ = "rooms"

    id = Column(UUID(as_uuid=True), primary_key=True, unique=True, default=str(uuid.uuid4()))
    name = Column(String, unique=True, index=True)
    password = Column(String)

    # Define one-to-many relationship with Track model
    tracks = relationship("Track", back_populates="room")


# class MusicQueue(Base):
#     __tablename__ = "queue_in_rooms"
#
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     room_id = Column(UUID, ForeignKey("rooms.id"))
#     user_id = Column(Integer)
#     song = Column(String)
#     artist = Column(String)
#     created_at = Column(DateTime(timezone=True), server_default=func.now())
#
#     # Define many-to-one relationship with Room model
#     rooms = relationship("Room", back_populates="queue_items")
#
#     # Define one-to-many relationship with Track model
#     track = relationship("Track", back_populates="queue_items")


class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    # artist = Column(String, index=True)
    uri = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    room_id = Column(UUID, ForeignKey("rooms.id"))

    # Define many-to-one relationship with Room model
    room = relationship("Room", back_populates="tracks")
