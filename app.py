from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados em memória - Lista de cursos
cursos = []

# Rota GET - Lista todos os cursos
@app.route('/cursos', methods=['GET'])
def listar_cursos():
    return jsonify(cursos), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
