# models/professor.py
from db import db


class ProfessorModel(db.Model):
    __tablename__ = "professores"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False, unique=True)
    especialidade = db.Column(db.String(80), nullable=False)
    
    # Relacionamento 1-N: Um professor pode ter vários cursos
    cursos = db.relationship('CursoModel', backref='professor', lazy=True, cascade='all, delete-orphan')
