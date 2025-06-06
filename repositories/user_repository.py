"""
Módulo user_repository

Este módulo contiene la clase UserRepository que maneja las operaciones CRUD
para usuarios y tareas en la base de datos mediante una sesión proporcionada.
"""
from models.tablas import User, Tarea

class UserRepository:
    """
    Repositorio para manejar operaciones CRUD sobre usuarios y tareas relacionadas.

    Attributes:
        session: Sesión de base de datos para realizar operaciones.
    """

    def __init__(self, session):
        """
        Inicializa el repositorio con una sesión de base de datos.

        Args:
            session: Sesión de base de datos.
        """
        self.session = session

    def add_user(self, user):
        """
        Añade un nuevo usuario a la base de datos.

        Args:
            user (User): Objeto usuario a agregar.

        Returns:
            User: El usuario agregado.
        """
        self.session.add(user)
        self.session.commit()
        return user

    def get_user_by_id(self, user_id):
        """
        Obtiene un usuario por su ID.

        Args:
            user_id (int): ID del usuario.

        Returns:
            User o None: El usuario encontrado o None si no existe.
        """
        return self.session.query(User).filter_by(id=user_id).first()

    def get_all_users(self):
        """
        Obtiene todos los usuarios registrados.

        Returns:
            list[User]: Lista con todos los usuarios.
        """
        return self.session.query(User).all()

    def update_user(self, user_id, name, email):
        """
        Actualiza los datos de un usuario existente.

        Args:
            user_id (int): ID del usuario a actualizar.
            name (str): Nuevo nombre del usuario.
            email (str): Nuevo correo electrónico del usuario.

        Returns:
            User o None: Usuario actualizado o None si no existe.
        """
        user = self.get_user_by_id(user_id)
        if user:
            user.name = name
            user.email = email
            self.session.commit()
        return user

    def delete_user(self, user_id):
        """
        Elimina un usuario de la base de datos.

        Args:
            user_id (int): ID del usuario a eliminar.

        Returns:
            bool: True si se eliminó el usuario, False si no se encontró.
        """
        user = self.get_user_by_id(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False

    def add_task(self,
                 user_id,
                 *,
                 titulo,
                 descripcion,
                 categoria_id,
                 prioridad,
                 estado):

        """
        Añade una tarea asociada a un usuario.

        Args:
            user_id (int): ID del usuario que crea la tarea.
            titulo (str): Título de la tarea.
            descripcion (str): Descripción de la tarea.
            categoria_id (int): ID de la categoría.
            prioridad (str): Prioridad de la tarea.
            estado (str): Estado de la tarea.

        Returns:
            Tarea: La tarea creada.
        """
        tarea = Tarea(
            user_id=user_id,
            titulo=titulo,
            descripcion=descripcion,
            categoria_id=categoria_id,
            prioridad=prioridad,
            estado=estado
        )
        self.session.add(tarea)
        self.session.commit()
        return tarea

    def edit_task(self, task_id, *, titulo=None, descripcion=None, categoria_id=None,
                  prioridad=None, estado=None):
        """
        Edita los detalles de una tarea existente.

        Args:
            task_id (int): ID de la tarea a editar.
            titulo (str, optional): Nuevo título.
            descripcion (str, optional): Nueva descripción.
            categoria_id (int, optional): Nueva categoría.
            prioridad (str, optional): Nueva prioridad.
            estado (str, optional): Nuevo estado.

        Returns:
            Tarea o None: Tarea actualizada o None si no existe.
        """
        tarea = self.session.query(Tarea).filter_by(idTarea=task_id).first()
        if not tarea:
            return None

        if titulo is not None:
            tarea.titulo = titulo
        if descripcion is not None:
            tarea.descripcion = descripcion
        if categoria_id is not None:
            tarea.categoria_id = categoria_id
        if prioridad is not None:
            tarea.prioridad = prioridad
        if estado is not None:
            tarea.estado = estado

        self.session.commit()
        return tarea

    def delete_task(self, task_id):
        """
        Elimina una tarea por su ID.

        Args:
            task_id (int): ID de la tarea a eliminar.

        Returns:
            bool: True si se eliminó la tarea, False si no se encontró.
        """
        tarea = self.session.query(Tarea).filter_by(idTarea=task_id).first()
        if not tarea:
            return False
        self.session.delete(tarea)
        self.session.commit()
        return True

    def complete_task(self, task_id):
        """
        Marca una tarea como completada.

        Args:
            task_id (int): ID de la tarea a marcar como completada.

        Returns:
            Tarea o None: La tarea actualizada o None si no se encontró.
        """
        tarea = self.session.query(Tarea).filter_by(idTarea=task_id).first()
        if not tarea:
            return None
        tarea.estado = "Completado"
        self.session.commit()
        return tarea
