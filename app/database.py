from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Use SQLite database located inside the /app folder
DATABASE_URL = "sqlite:///./app/feedback.db"

# Create SQLAlchemy engine with SQLite-specific argument
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our ORM models to inherit from
Base = declarative_base()
