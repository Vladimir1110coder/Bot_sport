from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncEngine
import os
from Database.models import Base

engine = create_async_engine(os.getenv("db"), echo = True)

session_maker = async_sessionmaker(engine, expire_on_commit = False)

async def on_create():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def on_drop():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
