from fastapi import FastAPI, HTTPException, APIRouter
from .models import users
from .crud import create_user, get_users


route = APIRouter(prefix="/users", tags=["Users"])

@route.post("/")
async def create_user(user):
    try:
        await create_user(user)
        return {"message": f"User {user} created"}
    
    except Exception as e:
        raise HTTPException(status_code = 500, detail=str(e))


@route.get("/")
async def get_users():
    try:
        users = await get_users()
        return users
    
    except Exception as e:
        raise HTTPException(status_code = 500, detail=str(e))

        