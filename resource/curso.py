# resource/curso.py
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import db
from models import CursoModel
from schemas.curso import CursoSchema, CursoUpdateSchema

blp = Blueprint("Cursos", "cursos", description="Operações com cursos")


@blp.route("/cursos")
class CursosResource(MethodView):
    @blp.response(200, CursoSchema(many=True))
    def get(self):
        cursos = CursoModel.query.all()
        return cursos

    @blp.arguments(CursoSchema)
    @blp.response(201, CursoSchema)
    def post(self, data):
        if CursoModel.query.filter_by(nome=data["nome"]).first():
            abort(409, message="Curso com esse nome já existe.")

        curso = CursoModel(**data)

        try:
            db.session.add(curso)
            db.session.commit()
        except Exception:
            db.session.rollback()
            abort(500, message="Erro ao salvar curso no banco de dados.")

        return curso


@blp.route("/cursos/<int:curso_id>")
class CursoResource(MethodView):
    @blp.response(200, CursoSchema)
    def get(self, curso_id):
        curso = CursoModel.query.get(curso_id)
        if not curso:
            abort(404, message="Curso não encontrado.")
        return curso

    @blp.arguments(CursoUpdateSchema)
    @blp.response(200, CursoSchema)
    def put(self, data, curso_id):
        curso = CursoModel.query.get(curso_id)
        if not curso:
            abort(404, message="Curso não encontrado.")

        if "nome" not in data or "carga_horaria" not in data:
            abort(400, message="Campos 'nome' e 'carga_horaria' são obrigatórios para PUT.")

        if (
            curso.nome != data["nome"]
            and CursoModel.query.filter_by(nome=data["nome"]).first()
        ):
            abort(409, message="Já existe outro curso com esse nome.")

        curso.nome = data["nome"]
        curso.carga_horaria = data["carga_horaria"]

        try:
            db.session.add(curso)
            db.session.commit()
        except Exception:
            db.session.rollback()
            abort(500, message="Erro ao atualizar curso no banco de dados.")

        return curso

    @blp.arguments(CursoUpdateSchema)
    @blp.response(200, CursoSchema)
    def patch(self, data, curso_id):
        curso = CursoModel.query.get(curso_id)
        if not curso:
            abort(404, message="Curso não encontrado.")

        if "nome" in data:
            if (
                curso.nome != data["nome"]
                and CursoModel.query.filter_by(nome=data["nome"]).first()
            ):
                abort(409, message="Já existe outro curso com esse nome.")
            curso.nome = data["nome"]

        if "carga_horaria" in data:
            curso.carga_horaria = data["carga_horaria"]

        try:
            db.session.add(curso)
            db.session.commit()
        except Exception:
            db.session.rollback()
            abort(500, message="Erro ao atualizar curso no banco de dados.")

        return curso

    def delete(self, curso_id):
        curso = CursoModel.query.get(curso_id)
        if not curso:
            abort(404, message="Curso não encontrado.")

        try:
            db.session.delete(curso)
            db.session.commit()
        except Exception:
            db.session.rollback()
            abort(500, message="Erro ao deletar curso no banco de dados.")

        return {"message": "Curso deletado com sucesso."}, 200
