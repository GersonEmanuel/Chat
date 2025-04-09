from fastapi import FastAPI, HTTPException, APIRouter
from .models import users
from .crud import get_or_create_user


route = APIRouter(prefix="/users", tags=["Users"])

@route.post("/")
async def create_user(user):
    try:
        await get_or_create_user(user.username)
        return {"message": f"User {user.username} created"}
    
    except Exception as e:
        raise HTTPException(status_code = 500, detail=str(e))


@route.get("/"):
async def get_users()