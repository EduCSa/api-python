
def routes(app):
    # importa e registra seu blueprint
    from src.controllers.usuario_controller import usuario_bp
    app.register_blueprint(usuario_bp)

    from src.controllers.compras_controller import compra_bp
    app.register_blueprint(compra_bp)
