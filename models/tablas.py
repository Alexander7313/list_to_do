# pylint: disable=too-few-public-methods
"""Definición de modelos de base de datos para usuarios, tareas, categorías y notificaciones."""

import uuid
import enum
from datetime import datetime

from sqlalchemy import Column, String, DateTime, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship

from models.base_datos import Base

class NotificationStatus(str, enum.Enum):
    """Enum para el estado de una notificación."""
    UNREAD = 'Unread'
    READ = 'Read'

class User(Base):
    """Modelo de usuario."""
    __tablename__ = 'users'

    id = Column(String(12), primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)

    tareas = relationship('Tarea', back_populates='user', cascade="all, delete")
    notifications = relationship('Notification', back_populates='user', cascade="all, delete")


class Categoria(Base):
    """Modelo de categoría de tareas."""
    __tablename__ = 'categorias'

    idCat = Column(String(12), primary_key=True, nullable=False)
    nombre = Column(String(20), nullable=False, unique=True)
    fecha = Column(DateTime, default=datetime.utcnow)

    tareas = relationship('Tarea', back_populates='categoria_obj', cascade="all, delete")


class Tarea(Base):
    """Modelo de tarea."""
    __tablename__ = 'tareas'

    idTarea = Column(String(36), primary_key=True,
                     default=lambda: str(uuid.uuid4()), nullable=False)
    user_id = Column(String(12), ForeignKey('users.id'), nullable=False)
    titulo = Column(String(120), nullable=False)
    descripcion = Column(Text)
    categoria_id = Column(String(12), ForeignKey('categorias.idCat'), nullable=True)
    prioridad = Column(String(255), nullable=False)
    estado = Column(String(255), nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='tareas')
    categoria_obj = relationship('Categoria', back_populates='tareas')
    notifications = relationship(
        'Notification', back_populates='tarea',
                                 cascade="all, delete")


class Notification(Base):
    """Modelo de notificación de tareas."""
    __tablename__ = 'notifications'

    idNot = Column(String(12), primary_key=True, nullable=False)
    user_id = Column(String(12), ForeignKey('users.id'), nullable=False)
    task_id = Column(String(36), ForeignKey('tareas.idTarea', ondelete='CASCADE'), nullable=False)
    message = Column(Text, nullable=False)
    status = Column(Enum(NotificationStatus, native_enum=False), default=NotificationStatus.UNREAD)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='notifications')
    tarea = relationship('Tarea', back_populates='notifications', passive_deletes=True)
