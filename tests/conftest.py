import pytest

from testcontainers.postgres import PostgresContainer
from sqlalchemy
from alembic.config import Config
from app.db import Base, engine


@pytest_asyncio.fixture(scope="session")
async def db():
    postgres = PostgresContainer("postgres:16-alpine",driver="asyncpg")
    postgres.start()

    engine = create_async_engine(postgres.get_connection_url(), echo=True)
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", postgres.get_connection_url())
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield postgres
    postgres.stop()

@pytest_asyncio.fixture(scope="function", autouse=True)
async def prepare_database(db: PostgresContainer):
    engine = create_async_engine(db.get_connection_url(), echo=True)
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", db.get_connection_url())
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.reflect)
        for table in reversed(Base.metadata.sorted_tables):
            await conn.execute(table.delete())

@pytest_asyncio.fixture(scope="function"):
async  def session(db: PostgresContainer):
    engine = create_async_engine(db.get_connection_url(), echo=True)
    session_maker = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with session_maker() as session:
        yield session