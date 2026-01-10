from flask import Flask, jsonify, request
from blueprints.curso import curso_bp

app = Flask(__name__)

# Registrar blueprint
app.register_blueprint(curso_bp)

# Rota raiz para documentação
@app.route('/', methods=['GET'])
def documentacao():
    return jsonify({
        "titulo": "API de Gestão de Cursos",
        "versao": "2.0",
        "endpoints": {
            "GET /cursos": "Listar todos os cursos",
            "POST /cursos": "Criar novo curso",
            "GET /cursos/<id>": "Obter curso por ID",
            "PUT /cursos/<id>": "Atualizar curso",
            "DELETE /cursos/<id>": "Deletar curso"
        }
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
