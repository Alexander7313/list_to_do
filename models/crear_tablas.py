"""Módulo para crear las tablas en la base de datos a partir de las clases definidas."""
from base_datos import Base, engine

# Crear las tablas en la base de datos SQLite
Base.metadata.create_all(engine)
print("✅ Tablas creadas correctamente.")
