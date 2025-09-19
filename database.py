from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
import time

DATABASE_URL = "postgresql://studentuser:I15Vwe5P7ZuDyrE3gRrilTHQirBhXMwj@dpg-d35tu03ipnbc739q3kk0-a.singapore-postgres.render.com/studentdb_og9a"

# Add sslmode=require for Render
DATABASE_URL += "?sslmode=require"

# Retry DB connection (Render free tier sometimes sleeps)
for attempt in range(5):
    try:
        engine = create_engine(DATABASE_URL)
        print("✅ Database connection successful")
        break
    except OperationalError as e:
        print(f"⚠️ Database connection failed (attempt {attempt+1}/5): {e}")
        time.sleep(5)
else:
    raise Exception("❌ Could not connect to the database after 5 attempts.")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
