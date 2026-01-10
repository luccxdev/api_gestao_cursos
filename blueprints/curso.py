from flask import Blueprint, jsonify, request
from db import cursos

# Criar blueprint
curso_bp = Blueprint('cursos', __name__, url_prefix='/cursos')

# GET - Listar todos
@curso_bp.route('', methods=['GET'])
def listar():
    return jsonify(list(cursos.values()))

# POST - Criar novo
@curso_bp.route('', methods=['POST'])
def criar():
    novo_id = max(cursos.keys(), default=0) + 1
    novo_curso = request.get_json()
    novo_curso['id'] = novo_id
    cursos[novo_id] = novo_curso
    return jsonify(novo_curso), 201

# GET - Obter por ID
@curso_bp.route('/<int:id>', methods=['GET'])
def obter(id):
    if id not in cursos:
        return jsonify({"erro": "Curso não encontrado"}), 404
    return jsonify(cursos[id])

# PUT - Atualizar
@curso_bp.route('/<int:id>', methods=['PUT'])
def atualizar(id):
    if id not in cursos:
        return jsonify({"erro": "Curso não encontrado"}), 404
    cursos[id].update(request.get_json())
    return jsonify(cursos[id])

# DELETE - Deletar
@curso_bp.route('/<int:id>', methods=['DELETE'])
def deletar(id):
    if id not in cursos:
        return jsonify({"erro": "Curso não encontrado"}), 404
    del cursos[id]
    return '', 204
