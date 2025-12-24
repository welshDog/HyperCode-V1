# Async database helpers sharing the canonical Base/config.

import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from .db import DatabaseConfig
from .models import Base


def _normalize_url(url: str) -> str:
    """Ensure SQLite URLs use aiosqlite for async engines."""
    if url.startswith("sqlite:///"):
        return url.replace("sqlite:///", "sqlite+aiosqlite:///")
    return url


ASYNC_DATABASE_URL = _normalize_url(DatabaseConfig.DATABASE_URL)

connect_args = {"check_same_thread": False} if "sqlite" in ASYNC_DATABASE_URL else {}

engine_kwargs = {
    "echo": DatabaseConfig.ECHO_SQL,
    "connect_args": connect_args,
    "pool_pre_ping": True,
    "pool_recycle": getattr(DatabaseConfig, "POOL_RECYCLE", 3600),
}
if "sqlite" not in ASYNC_DATABASE_URL:
    engine_kwargs["pool_size"] = getattr(DatabaseConfig, "POOL_SIZE", 10)
    engine_kwargs["max_overflow"] = getattr(DatabaseConfig, "MAX_OVERFLOW", 20)

async_engine = create_async_engine(ASYNC_DATABASE_URL, **engine_kwargs)

AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)


@asynccontextmanager
async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    """Async DB session context manager that commits/rolls back automatically."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise


__all__ = [
    "async_engine",
    "AsyncSessionLocal",
    "get_async_db",
    "ASYNC_DATABASE_URL",
]
