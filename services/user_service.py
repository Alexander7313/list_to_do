"""
Módulo UserService.

Define la clase UserService, que proporciona la lógica de negocio para la gestión
de usuarios, incluyendo creación, consulta, actualización y eliminación.

Este módulo utiliza un repositorio para acceder y manipular los datos de usuarios.
"""

import uuid
from models.Tablas import User

class UserService:
    """
    Servicio para la gestión de usuarios.

    Proporciona métodos para crear, obtener, actualizar y eliminar usuarios,
    utilizando un repositorio para la persistencia de datos.
    """

    def __init__(self, user_repository):
        """
        Inicializa el servicio con un repositorio de usuarios.

        Args:
            user_repository: Instancia del repositorio que maneja la persistencia de usuarios.
        """
        self.user_repository = user_repository

    def _generate_id(self):
        """
        Genera un ID único para un usuario.

        Utiliza UUID4 y toma los primeros 12 caracteres para crear un identificador.

        Returns:
            str: ID generado único para el usuario.
        """
        return str(uuid.uuid4())[:12]

    # --- Usuarios ---
    def create_user(self, name, email):
        """
        Crea un nuevo usuario con un ID generado, nombre y correo electrónico.

        Args:
            name (str): Nombre del usuario.
            email (str): Correo electrónico del usuario.

        Returns:
            User: Objeto usuario creado y almacenado mediante el repositorio.
        """
        user_id = self._generate_id()
        new_user = User(id=user_id, name=name, email=email, password_hash="hashed_password")
        return self.user_repository.add_user(new_user)

    def get_user_by_id(self, user_id):
        """
        Obtiene un usuario por su ID.

        Args:
            user_id (str): Identificador del usuario.

        Returns:
            User o None: Usuario encontrado o None si no existe.
        """
        return self.user_repository.get_user_by_id(user_id)

    def get_all_users(self):
        """
        Obtiene la lista de todos los usuarios almacenados.

        Returns:
            list: Lista de objetos User.
        """
        return self.user_repository.get_all_users()

    def update_user(self, user_id, name, email):
        """
        Actualiza la información de un usuario existente.

        Args:
            user_id (str): Identificador del usuario a actualizar.
            name (str): Nuevo nombre para el usuario.
            email (str): Nuevo correo electrónico para el usuario.

        Returns:
            User o None: Usuario actualizado o None si no se encontró.
        """
        return self.user_repository.update_user(user_id, name, email)

    def delete_user(self, user_id):
        """
        Elimina un usuario por su ID.

        Args:
            user_id (str): Identificador del usuario a eliminar.

        Returns:
            bool: True si la eliminación fue exitosa, False en caso contrario.
        """
        return self.user_repository.delete_user(user_id)
