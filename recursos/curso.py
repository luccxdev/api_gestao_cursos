from flask_restx import Namespace, Resource, fields
from marshmallow import ValidationError
from schemas.curso import CursoSchema, CursoSchemaUpdate
from db import cursos
import uuid

api = Namespace('cursos', description='Operações relacionadas a cursos')

# Model para documentação Swagger
curso_model = api.model('Curso', {
    'id': fields.Integer(description='ID do curso'),
    'nome': fields.String(required=True, description='Nome do curso'),
    'descricao': fields.String(description='Descrição do curso'),
    'carga_horaria': fields.Integer(required=True, description='Carga horária do curso')
})

schema = CursoSchema()
schema_update = CursoSchemaUpdate()

@api.route('')
class ListaCursos(Resource):
    @api.marshal_with(curso_model)
    def get(self):
        """Lista todos os cursos"""
        return list(cursos.values()), 200
    
    @api.expect(curso_model)
    @api.marshal_with(curso_model, code=201)
    def post(self):
        """Cria um novo curso"""
        try:
            dados_validados = schema.load(api.payload)
            novo_curso = {**dados_validados, "id": len(cursos) + 1}
            cursos[novo_curso['id']] = novo_curso
            return novo_curso, 201
        except ValidationError as e:
            api.abort(400, str(e.messages))

@api.route('/<int:id_curso>')
class RecursoCurso(Resource):
    @api.marshal_with(curso_model)
    def get(self, id_curso):
        """Obtém um curso por ID"""
        if id_curso not in cursos:
            api.abort(404, f'Curso {id_curso} não encontrado')
        return cursos[id_curso], 200
    
    @api.expect(curso_model)
    @api.marshal_with(curso_model)
    def put(self, id_curso):
        """Atualiza um curso"""
        if id_curso not in cursos:
            api.abort(404, f'Curso {id_curso} não encontrado')
        try:
            dados_validados = schema_update.load(api.payload)
            cursos[id_curso].update(dados_validados)
            return cursos[id_curso], 200
        except ValidationError as e:
            api.abort(400, str(e.messages))
    
    def delete(self, id_curso):
        """Deleta um curso"""
        if id_curso not in cursos:
            api.abort(404, f'Curso {id_curso} não encontrado')
        del cursos[id_curso]
        return '', 204
