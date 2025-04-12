from datetime import datetime, timedelta, timezone

from fastapi import HTTPException
import jwt
from passlib.context import CryptContext

from conf import SETTINGS


class AuthService:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(
            SETTINGS.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            payload=to_encode,
            key=SETTINGS.JWT_SECRET_KEY,
            algorithm=SETTINGS.JWT_ALGORITHM,
        )
        return encoded_jwt

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def decode_access_token(self, token):
        try:
            return jwt.decode(
                jwt=token,
                key=SETTINGS.JWT_SECRET_KEY,
                algorithms=[SETTINGS.JWT_ALGORITHM],
            )
        except jwt.exceptions.DecodeError:
            raise HTTPException(401, detail="Неверный токен.")
