"""
Módulo principal de la aplicación.

Este módulo inicializa la base de datos SQLite, configura las dependencias de los servicios
y ejecuta operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre usuarios como ejemplo
de interacción con la base de datos utilizando SQLAlchemy y una arquitectura en capas.

Componentes clave:
- Inicialización del motor de base de datos y sesión ORM.
- Creación de tablas a partir de los modelos definidos.
- Ejemplos de uso de `UserService` para manejar datos de usuario.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.BaseDatos import Base
from repositories.user_repository import UserRepository
from services.user_service import UserService

# Ruta del archivo de base de datos
DATABASE_FILE = './database.db'
DATABASE_URL = f"sqlite:///{DATABASE_FILE}"

def initialize_database():
    """
    Inicializa la base de datos y crea las tablas si no existen.

    Returns:
        engine (Engine): Motor de base de datos de SQLAlchemy.
    """
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    return engine

def main():
    """
    Función principal de la aplicación.


    Realiza una serie de operaciones CRUD sobre la tabla de usuarios:
    - Crea un nuevo usuario.
    - Consulta un usuario por ID.
    - Lista todos los usuarios.
    - Actualiza un usuario.
    - Elimina un usuario.
    """
    engine = initialize_database()
    Session = sessionmaker(bind=engine)
    session = Session()

    # Configurar repositorio y servicio
    user_repository = UserRepository(session)
    user_service = UserService(user_repository)

    # --- Ejemplos de interacción con la base de datos ---

    # 1. Crear un nuevo usuario
    print("Creating a new user...")
    new_user = user_service.create_user("Alice Smith", "alice@example.com")
    print(f"Created user: {new_user.name} ({new_user.email}) with ID: {new_user.id}")

    # 2. Obtener usuario por ID
    print("\nGetting user by ID...")
    user_by_id = user_service.get_user_by_id(new_user.id)
    if user_by_id:
        print(f"Found user: {user_by_id.name} ({user_by_id.email})")
    else:
        print("User not found.")

    # 3. Obtener todos los usuarios
    print("\nGetting all users...")
    all_users = user_service.get_all_users()
    if all_users:
        for user in all_users:
            print(f"- {user.name} ({user.email})")
    else:
        print("No users found.")

    # 4. Actualizar un usuario
    print("\nUpdating a user...")
    updated_user = user_service.update_user(new_user.id, "Alicia Smith", "alicia.smith@example.com")
    if updated_user:
        print(f"Updated user: {updated_user.name} ({updated_user.email})")
    else:
        print("User not found for update.")

    # 5. Eliminar un usuario
    print("\nDeleting a user...")
    if user_service.delete_user(new_user.id):
        print(f"User with ID {new_user.id} deleted successfully.")
    else:
        print("User not found for deletion.")

    # Verificación final
    print("\nVerifying deletion...")
    remaining_users = user_service.get_all_users()
    if remaining_users:
        for user in remaining_users:
            print(f"- {user.name} ({user.email})")
    else:
        print("No users found after deletion.")

    # Cerrar sesión de base de datos
    session.close()
    print("\nDatabase operations completed.")

if __name__ == "__main__":
    # Asegurarse de que el directorio para la base de datos exista
    os.makedirs(os.path.dirname(DATABASE_FILE), exist_ok=True)
    main()
