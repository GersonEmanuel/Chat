from .db import database
from .models import users, messages
from sqlalchemy import select


async def create_user(username:str):
    insert_query = users.insert().values(username=username)
    user_id = await database.execute(insert_query)
    return {"id": user_id, "username": username}



async def get_user(username:str):
    query = users.select().where(users.c.username == username)
    user = await database.fetch_one(query)
    if user:
        return user
    

async def get_users():
    query = select(users)
    users = await database.fethc_all(query)
    return users
