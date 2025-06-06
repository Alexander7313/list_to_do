"""test de servicio de usuario"""
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.base_datos import Base
from repositories.user_repository import UserRepository
from services.user_service import UserService

class TestUserService(unittest.TestCase):
    """
    Pruebas unitarias para el servicio de usuarios.

    Utiliza una base de datos SQLite en memoria para garantizar pruebas aisladas
    sin afectar archivos físicos.
    """

    def setUp(self):
        """
        Configura el entorno de prueba.

        - Inicializa la base de datos en memoria.
        - Crea la sesión de SQLAlchemy.
        - Inicializa el repositorio y el servicio de usuario.
        """
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        self.user_repository = UserRepository(self.session)
        self.user_service = UserService(self.user_repository)

    def tearDown(self):
        """
        Limpia el entorno tras cada prueba cerrando la sesión.
        """
        self.session.close()

    def test_create_user(self):
        """
        Prueba la creación de un usuario.

        Verifica que el usuario creado tenga un ID asignado
        y que los campos nombre y correo sean correctos.
        """
        user = self.user_service.create_user("Alice Smith", "alice@example.com")
        self.assertIsNotNone(user.id)
        self.assertEqual(user.name, "Alice Smith")
        self.assertEqual(user.email, "alice@example.com")

    def test_get_user_by_id(self):
        """
        Prueba la recuperación de un usuario por ID.

        Verifica que el usuario recuperado exista y tenga el nombre esperado.
        """
        user = self.user_service.create_user("Bob Johnson", "bob@example.com")
        retrieved = self.user_service.get_user_by_id(user.id)
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.name, "Bob Johnson")

    def test_get_all_users(self):
        """
        Prueba la obtención de todos los usuarios.

        Verifica que la cantidad de usuarios devueltos sea la esperada.
        """
        self.user_service.create_user("User One", "one@example.com")
        self.user_service.create_user("User Two", "two@example.com")
        all_users = self.user_service.get_all_users()
        self.assertEqual(len(all_users), 2)

    def test_update_user(self):
        """
        Prueba la actualización de un usuario existente.

        Verifica que los campos nombre y correo sean actualizados correctamente.
        """
        user = self.user_service.create_user("Old Name", "old@example.com")
        updated = self.user_service.update_user(user.id, "New Name", "new@example.com")
        self.assertEqual(updated.name, "New Name")
        self.assertEqual(updated.email, "new@example.com")

    def test_delete_user(self):
        """
        Prueba la eliminación de un usuario.

        Verifica que la eliminación retorne True y que el usuario ya no exista.
        """
        user = self.user_service.create_user("To Delete", "delete@example.com")
        deleted = self.user_service.delete_user(user.id)
        self.assertTrue(deleted)
        self.assertIsNone(self.user_service.get_user_by_id(user.id))

if __name__ == '__main__':
    unittest.main()
