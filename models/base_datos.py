"""Módulo para configurar la base de datos y habilitar claves foráneas en SQLite."""

from sqlalchemy import create_engine, event
from sqlalchemy.orm import declarative_base

# Base para las clases de modelo ORM
Base = declarative_base()

# Crear engine para la base de datos SQLite
DATABASE_URL = "sqlite:///app.db"
engine = create_engine(DATABASE_URL, echo=True)

# Habilitar claves foráneas en SQLite
@event.listens_for(engine, "connect")
def enable_foreign_keys(dbapi_connection, _):
    """Activa el soporte de claves foráneas en SQLite."""
    dbapi_connection.execute("PRAGMA foreign_keys=ON")
