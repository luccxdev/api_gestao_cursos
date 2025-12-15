from flask import Flask, jsonify, request

app = Flask(__name__)
cursos = []

@app.route('/cursos', methods=['GET'])
def listar_cursos():
    return jsonify(cursos), 200

@app.route('/cursos', methods=['POST'])
def criar_curso():
    dados = request.get_json()
    if not dados or 'nome' not in dados:
        return jsonify({"erro": "Nome obrigatório"}), 400
    novo_curso = {"id": len(cursos) + 1, "nome": dados['nome'], "descricao": dados.get('descricao', ''), "instrutor": dados.get('instrutor', '')}
    cursos.append(novo_curso)
    return jsonify(novo_curso), 201

@app.route('/cursos/<int:id>', methods=['GET'])
def obter_curso(id):
    for curso in cursos:
        if curso['id'] == id:
            return jsonify(curso), 200
    return jsonify({"erro": "Não encontrado"}), 404

@app.route('/cursos/<int:id>', methods=['PUT'])
def atualizar_curso(id):
    dados = request.get_json()
    for curso in cursos:
        if curso['id'] == id:
            curso.update({k: v for k, v in dados.items() if k in ['nome', 'descricao', 'instrutor']})
            return jsonify(curso), 200
    return jsonify({"erro": "Não encontrado"}), 404

@app.route('/cursos/<int:id>', methods=['DELETE'])
def deletar_curso(id):
    for i, curso in enumerate(cursos):
        if curso['id'] == id:
            return jsonify({"mensagem": "Deletado", "curso": cursos.pop(i)}), 200
    return jsonify({"erro": "Não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
