from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://odoo:odoo@localhost/db_gdc"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True,#connect_args={"check_same_thread": True}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

# metadata_obj = MetaData()

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)