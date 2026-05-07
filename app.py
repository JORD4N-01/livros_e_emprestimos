from flask import Flask
from routes.routes import register_routes

def create_app():
    app = Flask(__name__)

    # Registrar rotas (os devs vão implementar depois)
    register_routes(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)