from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = ''
ALGORITHM = ''
ACCESS_TOKEN_EXPIRES_MINUTES = 15

def create_access_token(data:dict, expires_delta: timedelta | None):
    to_encode = data.copy()
    expire = datetime.now() + expires_delta or timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.decode(to_encode, SECRET_KEY, algorithms=[ALGORITHM])



def decode_access_token(token:str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None