from models.Tablas import User, Tarea

class UserRepository:
    def __init__(self, session):
        self.session = session

    def add_user(self, user):
        self.session.add(user)
        self.session.commit()
        return user

    def get_user_by_id(self, user_id):
        return self.session.query(User).filter_by(id=user_id).first()

    def get_all_users(self):
        return self.session.query(User).all()

    def update_user(self, user_id, name, email):
        user = self.get_user_by_id(user_id)
        if user:
            user.name = name
            user.email = email
            self.session.commit()
        return user

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False

    def add_task(self, user_id, titulo, descripcion, categoria_id, prioridad, estado):
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

    def edit_task(self, task_id, titulo=None, descripcion=None, categoria_id=None, prioridad=None, estado=None):
        tarea = self.session.query(Tarea).filter_by(idTarea=task_id).first()
        if not tarea:
            return None

        if titulo:
            tarea.titulo = titulo
        if descripcion:
            tarea.descripcion = descripcion
        if categoria_id is not None:
            tarea.categoria_id = categoria_id
        if prioridad:
            tarea.prioridad = prioridad
        if estado:
            tarea.estado = estado

        self.session.commit()
        return tarea

    def delete_task(self, task_id):
        tarea = self.session.query(Tarea).filter_by(idTarea=task_id).first()
        if not tarea:
            return False
        self.session.delete(tarea)
        self.session.commit()
        return True

    def complete_task(self, task_id):
        tarea = self.session.query(Tarea).filter_by(idTarea=task_id).first()
        if not tarea:
            return None
        tarea.estado = "Completado"
        self.session.commit()
        return tarea
