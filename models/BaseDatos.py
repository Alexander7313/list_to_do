from sqlalchemy import create_engine, event
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Crear engine
DATABASE_URL = "sqlite:///app.db"
engine = create_engine(DATABASE_URL, echo=True)

# Habilitar claves foráneas en SQLite
@event.listens_for(engine, "connect")
def enable_foreign_keys(dbapi_connection, connection_record):
    dbapi_connection.execute("PRAGMA foreign_keys=ON")
