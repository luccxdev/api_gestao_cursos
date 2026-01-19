# resource/professor.py
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import db
from models import ProfessorModel
from schemas.professor import ProfessorSchema, ProfessorUpdateSchema

blp = Blueprint("Professores", "professores", description="Operações com professores")


@blp.route("/professores")
class ProfessoresResource(MethodView):
    @blp.response(200, ProfessorSchema(many=True))
    def get(self):
        professores = ProfessorModel.query.all()
        return professores

      @blp.arguments(ProfessorSchema)
    @blp.response(201, ProfessorSchema)
    def post(self, data):
        if ProfessorModel.query.filter_by(nome=data["nome"]).first():
            abort(409, message="Já existe um professor com esse nome.")

        professor = ProfessorModel(**data)

        try:
            db.session.add(professor)
            db.session.commit()
        except Exception:
            db.session.rollback()
            abort(500, message="Erro ao salvar professor no banco de dados.")

        return professor


@blp.route("/professores/<int:professor_id>")
class ProfessorResource(MethodView):
    @blp.response(200, ProfessorSchema)
    def get(self, professor_id):
        professor = ProfessorModel.query.get(professor_id)
        if not professor:
            abort(404, message="Professor não encontrado.")
        return professor

    @blp.arguments(ProfessorUpdateSchema)
    @blp.response(200, ProfessorSchema)
    def put(self, data, professor_id):
        professor = ProfessorModel.query.get(professor_id)
        if not professor:
            abort(404, message="Professor não encontrado.")

        if "nome" not in data or "especialidade" not in data:
            abort(400, message="Campos 'nome' e 'especialidade' são obrigatórios para PUT.")

        if "nome" in data:
            outro = ProfessorModel.query.filter_by(nome=data["nome"]).first()
            if outro and outro.id != professor_id:
                abort(409, message="Já existe outro professor com esse nome.")
            professor.nome = data["nome"]

        professor.especialidade = data["especialidade"]

        try:
            db.session.add(professor)
            db.session.commit()
        except Exception:
            db.session.rollback()
            abort(500, message="Erro ao atualizar professor no banco de dados.")

        return professor

    @blp.arguments(ProfessorUpdateSchema)
    @blp.response(200, ProfessorSchema)
    def patch(self, data, professor_id):
        professor = ProfessorModel.query.get(professor_id)
        if not professor:
            abort(404, message="Professor não encontrado.")

        if "nome" in data:
            outro = ProfessorModel.query.filter_by(nome=data["nome"]).first()
            if outro and outro.id != professor_id:
                abort(409, message="Já existe outro professor com esse nome.")
            professor.nome = data["nome"]

        if "especialidade" in data:
            professor.especialidade = data["especialidade"]

        try:
            db.session.add(professor)
            db.session.commit()
        except Exception:
            db.session.rollback()
            abort(500, message="Erro ao atualizar professor no banco de dados.")

        return professor

    def delete(self, professor_id):
        professor = ProfessorModel.query.get(professor_id)
        if not professor:
            abort(404, message="Professor não encontrado.")

        try:
            db.session.delete(professor)
            db.session.commit()
        except Exception:
            db.session.rollback()
            abort(500, message="Erro ao deletar professor no banco de dados.")

        return {"message": "Professor deletado com sucesso."}, 200
