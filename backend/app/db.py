from databases import Database
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

database = Database(DATABASE_URL)

async def get_db_connection():
    await database.connect()

async def close_db_connection():
    await database.disconnect()