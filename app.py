from flask import Flask
from flask_smorest import Api

from db import db
from resource.curso import blp as CursoBlueprint


def create_app():
    app = Flask(__name__)

    app.config["API_TITLE"] = "API Gestão de Cursos"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    api = Api(app)
    api.register_blueprint(CursoBlueprint)

    @app.route("/")
    def index():
        return {"message": "API de Gestão de Cursos - veja a documentação em /docs"}, 200

    return app


if __name__ == "__main__":
    app = create_app()

    with app.app_context():
        db.create_all()

    app.run(debug=True)
