from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados em memória - Lista de cursos
cursos = []

# Rota GET - Lista todos os cursos
@app.route('/cursos', methods=['GET'])
def listar_cursos():
    return jsonify(cursos), 200


# Rota POST - Criar novo curso
@app.route('/cursos', methods=['POST'])
def criar_curso():
    dados = request.get_json()
    if not dados or 'nome' not in dados:
        return jsonify({"erro": "Nome do curso é obrigatório"}), 400
    
    novo_curso = {
        "id": len(cursos) + 1,
        "nome": dados['nome'],
        "descricao": dados.get('descricao', ''),
        "instrutor": dados.get('instrutor', '')
    }
    cursos.append(novo_curso)
    return jsonify(novo_curso), 201

# Rota GET - Obter curso por ID
@app.route('/cursos/<int:id>', methods=['GET'])
def obter_curso(id):
    for curso in cursos:
        if curso['id'] == id:
            return jsonify(curso), 200
    return jsonify({"erro": "Curso não encontrado"}), 404

# Rota PUT - Atualizar curso
@app.route('/cursos/<int:id>', methods=['PUT'])
def atualizar_curso(id):
    dados = request.get_json()
    for curso in cursos:
        if curso['id'] == id:
            curso['nome'] = dados.get('nome', curso['nome'])
            curso['descricao'] = dados.get('descricao', curso['descricao'])
            curso['instrutor'] = dados.get('instrutor', curso['instrutor'])
            return jsonify(curso), 200
    return jsonify({"erro": "Curso não encontrado"}), 404

# Rota DELETE - Deletar curso
@app.route('/cursos/<int:id>', methods=['DELETE'])
def deletar_curso(id):
    for i, curso in enumerate(cursos):
        if curso['id'] == id:
            deletado = cursos.pop(i)
            return jsonify({"mensagem": "Curso deletado", "curso": deletado}), 200
    return jsonify({"erro": "Curso não encontrado"}), 404
if __name__ == '__main__':
    app.run(debug=True, port=5000)
