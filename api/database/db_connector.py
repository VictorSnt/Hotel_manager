#std
from contextlib import asynccontextmanager
from os import getenv
from typing import AsyncGenerator
#ext
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from dotenv import load_dotenv


load_dotenv()
class SessionMaker:

    engine = create_async_engine(
        getenv(
            'DATABASE_URL', 
            'sqlite+aiosqlite:///database.db'
        )
    )

    @classmethod
    async def create_tables(cls):
        async with cls.engine.begin() as engine:
            await engine.run_sync(SQLModel.metadata.create_all)

    @classmethod
    @asynccontextmanager
    async def get_session_async(cls) -> AsyncGenerator[AsyncSession, None]:
        session = AsyncSession(cls.engine)
        yield session
