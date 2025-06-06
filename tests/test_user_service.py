import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.BaseDatos import Base
from repositories.user_repository import UserRepository
from services.user_service import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        # Usamos una base de datos en memoria para pruebas (no crea archivos)
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        self.user_repository = UserRepository(self.session)
        self.user_service = UserService(self.user_repository)

    def tearDown(self):
        self.session.close()

    def test_create_user(self):
        user = self.user_service.create_user("Alice Smith", "alice@example.com")
        self.assertIsNotNone(user.id)
        self.assertEqual(user.name, "Alice Smith")
        self.assertEqual(user.email, "alice@example.com")

    def test_get_user_by_id(self):
        user = self.user_service.create_user("Bob Johnson", "bob@example.com")
        retrieved = self.user_service.get_user_by_id(user.id)
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.name, "Bob Johnson")

    def test_get_all_users(self):
        self.user_service.create_user("User One", "one@example.com")
        self.user_service.create_user("User Two", "two@example.com")
        all_users = self.user_service.get_all_users()
        self.assertEqual(len(all_users), 2)

    def test_update_user(self):
        user = self.user_service.create_user("Old Name", "old@example.com")
        updated = self.user_service.update_user(user.id, "New Name", "new@example.com")
        self.assertEqual(updated.name, "New Name")
        self.assertEqual(updated.email, "new@example.com")

    def test_delete_user(self):
        user = self.user_service.create_user("To Delete", "delete@example.com")
        deleted = self.user_service.delete_user(user.id)
        self.assertTrue(deleted)
        self.assertIsNone(self.user_service.get_user_by_id(user.id))

if __name__ == '__main__':
    unittest.main()