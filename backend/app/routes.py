from fastapi import FastAPI, HTTPException, APIRouter
from .models import users
from .crud import create_user, get_users
from .schemas import User


route = APIRouter(prefix="/users", tags=["Users"])

@route.post("/")
async def create_user_route(user: User):
    try:
        print(user)
        await create_user(user)
        return {"message": f"User {user} created"}
    
    except Exception as e:
        raise HTTPException(status_code = 500, detail=str(e))


@route.get("/")
async def get_users_route():
    try:
        users = await get_users()
        if not users:
            return {"no users":"without user at moment"}
        return users
    
    except Exception as e:
        raise HTTPException(status_code = 500, detail=str(e))

        