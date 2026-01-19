# models/curso.py
from db import db


class CursoModel(db.Model):
    __tablename__ = "cursos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False, unique=True)
    carga_horaria = db.Column(db.Integer, nullable=False)
        
    # Foreign Key para Professor (relacionamento N-1)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
