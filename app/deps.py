# Create Dependency to Get DB Session
# backend/app/deps.py

from app.database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# This function creates a new database session for each request and ensures that the session is closed after the request is completed.
# This is important for managing database connections and resources efficiently.