
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Find the backend directory regardless of where FastAPI is launched.
BACKEND_DIR = Path(__file__).resolve().parents[2]

# Keep the existing database in the backend directory.
DATABASE_PATH = BACKEND_DIR / "newstalk.db"

DATABASE_URL = f"sqlite:///{DATABASE_PATH.as_posix()}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

sessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()
