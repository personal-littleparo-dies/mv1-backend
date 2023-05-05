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
    __tablename__ = "lobbies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    password = Column(String)

    # Define one-to-many relationship with Room model
    rooms = relationship("Room", back_populates="lobby")


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    password = Column(String)

    # Define one-to-many relationship with QueueItem model
    queue_items = relationship("QueueItem", back_populates="room")


class MusicQueue(Base):
    __tablename__ = "queue_items"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.id"))
    user_id = Column(Integer)
    song = Column(String)
    artist = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Define many-to-one relationship with Room model
    room = relationship("Room", back_populates="queue_items")



# class Track(Base):
#     __tablename__ = "track"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     artist = Column(String, index=True)
#     room_id = Column(Integer, ForeignKey("rooms.id"))
#
#     room = relationship("Room", back_populates="tracks")
