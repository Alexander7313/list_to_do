import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.Tablas import Base, Tarea
from repositories.user_repository import UserRepository
from services.user_service import UserService

class TestTaskOperations(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        self.repository = UserRepository(self.session)
        self.service = UserService(self.repository)

        # Crear un usuario de prueba
        self.user = self.service.create_user("Task User", "taskuser@example.com")

    def tearDown(self):
        self.session.close()

    def test_add_task(self):
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
        result = self.repository.edit_task("invalid_id", titulo="Nada")
        self.assertIsNone(result)

    def test_complete_task_invalid_id(self):
        result = self.repository.complete_task("invalid_id")
        self.assertIsNone(result)

    def test_delete_task_invalid_id(self):
        result = self.repository.delete_task("invalid_id")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

