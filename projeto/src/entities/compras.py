# src/entities/compras.py
from src.db import db
from sqlalchemy import text

class Compras(db.Model):
    __tablename__ = 'compras'
    id               = db.Column(db.Integer, primary_key=True)
    usuario_id       = db.Column(db.Integer, nullable=False)
    valor            = db.Column(db.Numeric(10,2), nullable=False)
    status_pagamento = db.Column(db.String(20), nullable=False)
    forma_pagamento  = db.Column(db.String(20), nullable=False)
    descricao        = db.Column(db.String(200), nullable=False)
    data_compra      = db.Column(
        db.DateTime(timezone=True),
        server_default=text("TIMEZONE('America/Sao_Paulo', NOW())")
    )

    def to_dict(self):
        return {
            "id":               self.id,
            "usuario_id":       self.usuario_id,
            "valor":            float(self.valor),
            "status_pagamento": self.status_pagamento,
            "forma_pagamento":  self.forma_pagamento,
            "descricao":        self.descricao,
            "data_compra":      self.data_compra.isoformat() if self.data_compra else None,
        }
