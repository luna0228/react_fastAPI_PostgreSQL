from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./homework.db"
# for github (postgresql)
SQLALCHEMY_DATABASE_URL = "postgresql://default:8RUjDA7dBQoC@ep-red-dawn-83306951.us-east-1.postgres.vercel-storage.com:5432/verceldb"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()