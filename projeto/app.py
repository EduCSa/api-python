
from flask import Flask
from src.config.config import Config
from src.db  import db, migrate
from src.router.routes import routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    routes(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
