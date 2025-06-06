# main.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.BaseDatos import Base
from repositories.user_repository import UserRepository
from services.user_service import UserService

DATABASE_FILE = './database.db'
DATABASE_URL = f"sqlite:///{DATABASE_FILE}"

def initialize_database():
    """Initializes the database and creates tables if they don't exist."""
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    return engine

def main():
    engine = initialize_database()
    Session = sessionmaker(bind=engine)
    session = Session()

    user_repository = UserRepository(session)
    user_service = UserService(user_repository)

    # --- Database Interaction Examples ---

    # 1. Create a new user
    print("Creating a new user...")
    new_user = user_service.create_user("Alice Smith", "alice@example.com")
    print(f"Created user: {new_user.name} ({new_user.email}) with ID: {new_user.id}")

    # 2. Get a user by ID
    print("\nGetting user by ID...")
    user_by_id = user_service.get_user_by_id(new_user.id)
    if user_by_id:
        print(f"Found user: {user_by_id.name} ({user_by_id.email})")
    else:
        print("User not found.")

    # 3. Get all users
    print("\nGetting all users...")
    all_users = user_service.get_all_users()
    if all_users:
        for user in all_users:
            print(f"- {user.name} ({user.email})")
    else:
        print("No users found.")

    # 4. Update a user
    print("\nUpdating a user...")
    updated_user = user_service.update_user(new_user.id, "Alicia Smith", "alicia.smith@example.com")
    if updated_user:
        print(f"Updated user: {updated_user.name} ({updated_user.email})")
    else:
        print("User not found for update.")

    # 5. Delete a user
    print("\nDeleting a user...")
    if user_service.delete_user(new_user.id):
        print(f"User with ID {new_user.id} deleted successfully.")
    else:
        print("User not found for deletion.")

    print("\nVerifying deletion...")
    remaining_users = user_service.get_all_users()
    if remaining_users:
        for user in remaining_users:
            print(f"- {user.name} ({user.email})")
    else:
        print("No users found after deletion.")

    session.close()
    print("\nDatabase operations completed.")

if __name__ == "__main__":
    # Ensure the 'data' directory exists for the database file
    os.makedirs(os.path.dirname(DATABASE_FILE), exist_ok=True)
    main()