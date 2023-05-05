from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.schemas import LobbyCreate, LobbyInDB, LobbyUpdate
from app.core.database import get_db
from . import router


@router.post("/lobbies", response_model=LobbyInDB, status_code=status.HTTP_201_CREATED)
def create_lobby_api(
    lobby: LobbyCreate,
    db: Session = Depends(get_db),
):
    """
    Create a new lobby.
    """
    lobby_in_db = get_lobby(db, lobby_name=lobby.lobby_name)
    if lobby_in_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Lobby with this name already exists.",
        )
    return create_lobby(db, lobby=lobby)


@router.get("/lobbies", response_model=List[LobbyInDB])
def get_lobbies_api(db: Session = Depends(get_db)):
    """
    Get all lobbies.
    """
    return get_lobbies(db)


@router.get("/lobbies/{lobby_id}", response_model=LobbyInDB)
def get_lobby_api(lobby_id: int, db: Session = Depends(get_db)):
    """
    Get a lobby by ID.
    """
    lobby = get_lobby(db, lobby_id=lobby_id)
    if not lobby:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lobby not found.",
        )
    return lobby


@router.put("/lobbies/{lobby_id}", response_model=LobbyInDB)
def update_lobby_api(
    lobby_id: int,
    lobby_update: LobbyUpdate,
    db: Session = Depends(get_db),
):
    """
    Update a lobby.
    """
    lobby = get_lobby(db, lobby_id=lobby_id)
    if not lobby:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lobby not found.",
        )
    return update_lobby(db, lobby=lobby, lobby_update=lobby_update)
