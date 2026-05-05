from flask import Flask, render_template
from flask_cors import CORS
from routes.routes import register_routes

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    
    # Habilitar CORS para requisições frontend
    CORS(app)

    # Registrar rotas da API
    register_routes(app)
    
    # Rota para servir o frontend
    @app.route('/')
    def index():
        return render_template('index.html')

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)