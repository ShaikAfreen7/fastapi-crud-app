from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://studentuser:I15Vwe5P7ZuDyrE3gRrilTHQirBhXMwj@dpg-d35tu03ipnbc739q3kk0-a.singapore-postgres.render.com/studentdb_og9a?sslmode=require"

# Create engine
engine = create_engine(DATABASE_URL)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


# Dependency (use in FastAPI routes)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
