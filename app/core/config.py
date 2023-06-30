import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


# PROJECT_NAME = "Music Lounge"
# PROJECT_VERSION = "0.1.0"
# API_PREFIX = "/api/v1"
# ...

class Config:
    DEBUG = False
    TESTING = False
    # SECRET_KEY = os.getenv("SECRET_KEY")
    SECRET_KEY = "A Super Secret Key"
    DATABASE_URL = f"sqlite:///{Path(__file__).parent.parent.absolute()}/db.sqlite3"


class ProdConfig(Config):
    # SECRET_KEY = os.getenv("SECRET_KEY")
    # DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_DATABASE_KEY = "EUnndoEnhWm37ieu"
    DATABASE_URL = f"postgresql+psycopg2://postgres:{SECRET_DATABASE_KEY}@db.oxvpyxqfidicuyvanjhd.supabase.co:5432/muzevird"


class DevConfig(Config):
    DEBUG = True
    DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/dev_db"


class TestConfig(Config):
    TESTING = True
    DATABASE_URL = "sqlite:///:memory:"


# Set the environment configuration based on the `ENVIRONMENT` environment variable
if os.getenv("ENVIRONMENT") == "production":
    CONFIG = ProdConfig()
elif os.getenv("ENVIRONMENT") == "development":
    CONFIG = DevConfig()
else:
    CONFIG = TestConfig()
