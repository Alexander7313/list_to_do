from BaseDatos import Base, engine
import Tablas  # Esto importa las clases para que Base las conozca

# Crear las tablas en la base de datos SQLite
Base.metadata.create_all(engine)
print("✅ Tablas creadas correctamente.")
