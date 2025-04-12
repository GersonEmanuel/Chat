from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orms import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..models.users import users
from database import get_db
from ..core.passwordhashing import hash_password, verify_password
from ..core.jwt import create_access_token



auth_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokeUrl="token")


#rotas
@auth_router.post("/register")
def register(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    existing_user = db.query(users).filter(users.username == form_data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="username already registered")
    
    hashed = hash_password(form_data.password)
    new_user = users(username=form_data.username, password=form_data.password)
    db.add(new_user)
    db.commit()
    return {"message": "User registered"}



@auth_router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(users).filter(users.username == form_data.username).first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail = "invalid")
    
    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
    



