from flask import Flask
from flask_restx import Api
from recursos.curso import api as ns_curso

app = Flask(__name__)
app.config['RESTX_MASK_SWAGGER'] = False
app.config['JSON_SORT_KEYS'] = False

api = Api(
    app,
    version='1.0',
    title='API de Gestão de Cursos',
    description='API RESTful para gerenciar cursos com Blueprints, OpenAPI e Schemas',
    doc='/docs',
    prefix='/api/v1'
)

# Registrar namespaces (blueprints)
api.add_namespace(ns_curso)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
