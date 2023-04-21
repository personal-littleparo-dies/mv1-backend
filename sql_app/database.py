from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://postgres:test@localhost:5432/rgay"

SECRET = "TCVNJXCcFhK6UaiB"
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://postgres:{SECRET}@https://nuuikzhrsocnmmngwyfx.supabase.co:5432/muzevird"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=600,
    pool_size=10,
)
SessionLocal = sessionmaker(autoflush=True, bind=engine)
