from .db import database, get_db_connection, close_db_connection
from .models import users, messages
from sqlalchemy import select


async def create_user(username:str):
    await get_db_connection()
    insert_query = users.insert().values(username=username)
    user_id = await database.execute(insert_query)
    await close_db_connection()
    return {"id": user_id, "username": username}




async def get_user(username:str):
    await get_db_connection()
    query = users.select().where(users.c.username == username)
    user = await database.fetch_one(query)
    close_db_connection()
    if user:
        return user
    

async def get_users():
    get_db_connection()
    query = select(users)
    users = await database.fethc_all(query)
    close_db_connection()
    return users
