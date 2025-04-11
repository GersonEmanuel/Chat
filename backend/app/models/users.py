from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData, ForeignKey
import datetime

metadata_obj = MetaData()

users = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String, unique=True),
    Column("hashed_password", String)
)

messages = Table(
    "messages",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("content", String),
    Column("timestamp", DateTime, default=datetime.datetime.now()),
    Column("user_id", Integer, ForeignKey("users.id"))
    
)