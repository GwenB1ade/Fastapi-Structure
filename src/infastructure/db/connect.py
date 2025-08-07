from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


from src.config import settings

# engine = create_engine(settings.database_url)
# session_creater = sessionmaker(engine, class_=Session, expire_on_commit=False)


engine = create_async_engine(
    settings.async_database_url,
    echo=False,
    pool_size=20,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=3600,
)

AsyncSessionLocal = sessionmaker(
    engine,  # pyright: ignore[reportCallIssue, reportArgumentType]
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)


async def get_db() -> AsyncSessionLocal:
    async with AsyncSessionLocal() as db:
        try:
            yield db
            await db.commit()
        except Exception:
            await db.rollback()
            raise
        finally:
            await db.close()
