"""Importaciones de los repósitorios, modelos de las tablas , servicios """
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.tablas import Base, Tarea
from repositories.user_repository import UserRepository
from services.user_service import UserService

class TestTaskOperations(unittest.TestCase):
    """
    Pruebas unitarias para las operaciones CRUD relacionadas con tareas.

    Se utiliza una base de datos SQLite en memoria para pruebas aisladas,
    y se prueba la integración entre el repositorio y el servicio de usuarios
    y tareas.
    """

    def setUp(self):
        """
        Configura el entorno de prueba inicial.

        - Crea la base de datos en memoria.
        - Inicializa la sesión de SQLAlchemy.
        - Crea un usuario de prueba para asociar las tareas.
        """
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        self.repository = UserRepository(self.session)
        self.service = UserService(self.repository)

        # Crear un usuario de prueba
        self.user = self.service.create_user("Task User", "taskuser@example.com")

    def tearDown(self):
        """
        Cierra la sesión de base de datos tras cada prueba para limpiar el estado.
        """
        self.session.close()

    def test_add_task(self):
        """
        Prueba la creación de una nueva tarea.

        Verifica que los campos título y estado sean asignados correctamente.
        """
        tarea = self.repository.add_task(
            user_id=self.user.id,
            titulo="Nueva tarea",
            descripcion="Descripción",
            categoria_id=None,
            prioridad="Alta",
            estado="Pendiente"
        )
        self.assertEqual(tarea.titulo, "Nueva tarea")
        self.assertEqual(tarea.estado, "Pendiente")

    def test_edit_task(self):
        """
        Prueba la edición de una tarea existente.

        Verifica que los campos título y estado se actualicen correctamente.
        """
        tarea = self.repository.add_task(
            user_id=self.user.id,
            titulo="Editar tarea",
            descripcion="Vieja desc",
            categoria_id=None,
            prioridad="Media",
            estado="Pendiente"
        )
        editada = self.repository.edit_task(
            task_id=tarea.idTarea,
            titulo="Tarea editada",
            descripcion="Descripción nueva",
            prioridad="Alta",
            estado="En progreso"
        )
        self.assertEqual(editada.titulo, "Tarea editada")
        self.assertEqual(editada.estado, "En progreso")

    def test_complete_task(self):
        """
        Prueba marcar una tarea como completada.

        Verifica que el estado cambie a "Completado".
        """
        tarea = self.repository.add_task(
            user_id=self.user.id,
            titulo="Completar tarea",
            descripcion="",
            categoria_id=None,
            prioridad="Baja",
            estado="Pendiente"
        )
        completada = self.repository.complete_task(tarea.idTarea)
        self.assertEqual(completada.estado, "Completado")

    def test_delete_task(self):
        """
        Prueba la eliminación de una tarea.

        Verifica que la operación retorne True indicando éxito.
        """
        tarea = self.repository.add_task(
            user_id=self.user.id,
            titulo="Eliminar tarea",
            descripcion="",
            categoria_id=None,
            prioridad="Baja",
            estado="Pendiente"
        )
        resultado = self.repository.delete_task(tarea.idTarea)
        self.assertTrue(resultado)

    # --- Tests negativos ---

    def test_edit_task_invalid_id(self):
        """
        Prueba la edición de tarea con un ID inválido.

        Verifica que el resultado sea None.
        """
        result = self.repository.edit_task("invalid_id", titulo="Nada")
        self.assertIsNone(result)

    def test_complete_task_invalid_id(self):
        """
        Prueba completar una tarea con un ID inválido.

        Verifica que el resultado sea None.
        """
        result = self.repository.complete_task("invalid_id")
        self.assertIsNone(result)

    def test_delete_task_invalid_id(self):
        """
        Prueba eliminar una tarea con un ID inválido.

        Verifica que el resultado sea False.
        """
        result = self.repository.delete_task("invalid_id")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
