


def routes(app):
    # importa e registra seu blueprint
    from src.controllers.usuario_controller import usuario_bp
    app.register_blueprint(usuario_bp)
