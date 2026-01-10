from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas.curso import CursoSchema, CursoSchemaUpdate

blp = Blueprint('cursos', __name__, url_prefix='/cursos', description='Operações relacionadas a cursos')

# Dicionário para armazenar os cursos (em memória)
cursos = {}

@blp.route('/')
class ListaCursos(MethodView):
    @blp.response(200, CursoSchema(many=True))
    def get(self):
        """Lista todos os cursos"""
        return list(cursos.values())

    @blp.arguments(CursoSchema)
    @blp.response(201, CursoSchema)
    def post(self, novo_curso):
        """Cria um novo curso"""
        novo_id = max(cursos.keys(), default=0) + 1
        novo_curso['id'] = novo_id
        cursos[novo_id] = novo_curso
        return novo_curso

@blp.route('/<int:curso_id>')
class DetalheCurso(MethodView):
    @blp.response(200, CursoSchema)
    def get(self, curso_id):
        """Obtém um curso por ID"""
        if curso_id not in cursos:
            abort(404, message=f'Curso {curso_id} não encontrado')
        return cursos[curso_id]

    @blp.arguments(CursoSchemaUpdate)
    @blp.response(200, CursoSchema)
    def put(self, dados_atualizacao, curso_id):
        """Atualiza um curso"""
        if curso_id not in cursos:
            abort(404, message=f'Curso {curso_id} não encontrado')
        cursos[curso_id].update(dados_atualizacao)
        return cursos[curso_id]

    @blp.response(204)
    def delete(self, curso_id):
        """Deleta um curso"""
        if curso_id not in cursos:
            abort(404, message=f'Curso {curso_id} não encontrado')
        del cursos[curso_id]
