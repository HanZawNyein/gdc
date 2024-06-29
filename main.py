from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

db = SessionLocal()