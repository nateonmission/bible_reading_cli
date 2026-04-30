from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DB_PATH = Path("bible_tracker.db")

DATABASE_URL = f"sqlite:///{DB_PATH}"


class Base(DeclarativeBase):
    pass


engine = create_engine(
    DATABASE_URL,
    echo=False,
    future=True,
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True,
)


def init_db() -> None:
    """
    Create database tables.
    Import models here so SQLAlchemy knows about them.
    """
    from bible_tracker import models  # noqa: F401

    Base.metadata.create_all(bind=engine)


def get_session():
    """
    Use this when you need a database session.
    """
    with SessionLocal() as session:
        yield session