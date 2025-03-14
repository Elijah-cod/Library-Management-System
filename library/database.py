from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite Database Connection
DATABASE_URL = "sqlite:///library.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    return SessionLocal()

def create_tables():
    """Create all tables in the database."""
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")