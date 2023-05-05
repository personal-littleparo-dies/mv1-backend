# import dataclasses
# import uuid
# from datetime import datetime
#
# from sqlalchemy import Column, String, DateTime, Text, func, UUID
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database import Base


class Lobby(Base):
    __tablename__ = "lobby"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, nullable=False)
    owner = Column(String(255), index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    rooms = relationship("Room", back_populates="lobby")


class Room(Base):
    __tablename__ = "room"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, nullable=False)
    password = Column(String(255), nullable=False)

    # queue = relationship("MusicQueue", back_populates="room")


class MusicQueue(Base):
    __tablename__ = "song_queue"

    id = Column(Integer, primary_key=True, index=True)
    song_name = Column(String(255), index=True, nullable=False)
    song_url = Column(String(255), nullable=False)
    added_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    room_id = Column(Integer, ForeignKey("room.id"), nullable=False)

    room = relationship("Room", back_populates="queue")


# class Track(Base):
#     __tablename__ = "track"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     artist = Column(String, index=True)
#     room_id = Column(Integer, ForeignKey("rooms.id"))
#
#     room = relationship("Room", back_populates="tracks")
