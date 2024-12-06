from database import db
from datetime import datetime

class Tarefas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    titulo = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, unique=False, nullable=False, default=False)

    