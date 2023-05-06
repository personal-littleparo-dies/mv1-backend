from datetime import datetime, timedelta
from typing import Optional

from fastapi import HTTPException, status
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import Config
from app.core.schemas import TokenData


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, Config.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> TokenData:
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
        token_data = TokenData(username=username)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    return token_data


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


# from here
def is_authorized(password: str, username: str) -> bool:
    return verify_password(username, password)


def get_current_user(token: str) -> str: # OAuth??
    """Get the current user from the access token"""
    token_data = decode_access_token(token)
    return token_data.username
