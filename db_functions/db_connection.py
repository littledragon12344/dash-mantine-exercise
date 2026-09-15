from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_functions.db_tables import Base

import os


DB_PATH = "/db/test_database.db"

DB_PATH = os.path.join(
    os.getcwd(),
    'db',
    'test_database.db'

)


os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

DATABASE_URL = f"sqlite:///{DB_PATH}"


engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# create the tables
Base.metadata.create_all(bind=engine)
