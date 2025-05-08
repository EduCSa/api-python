from src.db        import db   # <— aqui!
from datetime import datetime

class Compras(db.Model):
    __tablename__ = 'compras'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    data_compra = db.Column(db.DateTime, default=db.func.current_timestamp())
    valor = db.Column(db.Float, nullable=False)
    status_pagamento = db.Column(db.String(20), nullable=False)
    forma_pagamento = db.Column(db.String(20), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"<compras {self.data_compra}>"
