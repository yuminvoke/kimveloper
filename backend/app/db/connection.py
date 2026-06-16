from collections.abc import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, AsyncConnection


engine = create_async_engine("postgresql+asyncpg://kim:developer!@localhost:5432/dev")
metadata = MetaData(schema="chat")

async def get_db_connection() -> AsyncGenerator[AsyncConnection, None]:
    async with engine.connect() as connection:
        yield connection