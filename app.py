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
if __name__ == '__main__':
    app.run(debug=True, port=5000)
