from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# Секретный ключ для подписи токенов (в реальном проекте хранить в .env!)
SECRET_KEY = "supersecretkey"
# Алгоритм шифрования токена
ALGORITHM = "HS256"
# Время жизни токена (в минутах)
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# FastAPI-обёртка для работы с OAuth2 (парсим токен из заголовка)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    Генерируем JWT-токен для пользователя
    data — словарь с полезной нагрузкой (например, {'sub': username})
    expires_delta — сколько времени токен будет жить
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str = Depends(oauth2_scheme)):
    """
    Проверяем валидность токена. Если всё ок — возвращаем username
    Если нет — выбрасываем ошибку 401
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token") 