import uuid
from models.Tablas import User

class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def _generate_id(self):
        return str(uuid.uuid4())[:12]

    # --- Usuarios ---
    def create_user(self, name, email):
        user_id = self._generate_id()
        new_user = User(id=user_id, name=name, email=email, password_hash="hashed_password")
        return self.user_repository.add_user(new_user)

    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def update_user(self, user_id, name, email):
        return self.user_repository.update_user(user_id, name, email)

    def delete_user(self, user_id):
        return self.user_repository.delete_user(user_id)

    # --- Tareas ---
    def add_task(self, user_id, titulo, descripcion, categoria_id, prioridad, estado):
        task_id = self._generate_id()
        return self.user_repository.add_task(
            idTarea=task_id,
            user_id=user_id,
            titulo=titulo,
            descripcion=descripcion,
            categoria_id=categoria_id,
            prioridad=prioridad,
            estado=estado
        )

    def edit_task(self, task_id, titulo=None, descripcion=None, prioridad=None, estado=None):
        return self.user_repository.edit_task(
            task_id=task_id,
            titulo=titulo,
            descripcion=descripcion,
            prioridad=prioridad,
            estado=estado
        )

    def complete_task(self, task_id):
        return self.user_repository.complete_task(task_id)

    def delete_task(self, task_id):
        return self.user_repository.delete_task(task_id)
